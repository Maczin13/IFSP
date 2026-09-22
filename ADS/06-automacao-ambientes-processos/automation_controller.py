"""Controlador IoT determinístico com histerese, validação e fail-safe."""
from __future__ import annotations
import argparse, json, logging, math
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

class ActuatorState(str,Enum): OFF='OFF'; ON='ON'; SAFE='SAFE'
@dataclass(frozen=True)
class ControllerConfig:
    turn_on_c: float=30.0
    turn_off_c: float=28.0
    max_sensor_age_s: float=5.0
    def __post_init__(self):
        if self.turn_off_c>=self.turn_on_c: raise ValueError('histerese inválida')
        if self.max_sensor_age_s<=0: raise ValueError('idade máxima inválida')
@dataclass(frozen=True)
class SensorReading:
    sensor_id:str; temperature_c:float|None; timestamp:str; quality:str='good'
    def age_seconds(self,now:datetime)->float:
        t=datetime.fromisoformat(self.timestamp.replace('Z','+00:00')); return (now-t).total_seconds()
@dataclass(frozen=True)
class Decision:
    sensor_id:str; previous:str; state:str; reason:str; temperature_c:float|None; timestamp:str

class ThermalController:
    def __init__(self,config:ControllerConfig,logger=None):
        self.config=config; self.state=ActuatorState.OFF; self.logger=logger or logging.getLogger('automation')
    def update(self,reading:SensorReading,now:datetime|None=None)->Decision:
        now=now or datetime.now(timezone.utc)
        prev=self.state.value; reason='within_hysteresis'
        invalid=reading.temperature_c is None or reading.quality!='good' or not isinstance(reading.temperature_c,(int,float)) or not math.isfinite(reading.temperature_c)
        stale=False
        try: stale=reading.age_seconds(now)>self.config.max_sensor_age_s
        except (ValueError,TypeError): invalid=True; reason='invalid_timestamp'
        if invalid or stale:
            self.state=ActuatorState.SAFE; reason='invalid_reading' if invalid else 'stale_reading'
        elif self.state in (ActuatorState.OFF,ActuatorState.SAFE) and reading.temperature_c>=self.config.turn_on_c:
            self.state=ActuatorState.ON; reason='above_turn_on_threshold'
        elif self.state==ActuatorState.ON and reading.temperature_c<=self.config.turn_off_c:
            self.state=ActuatorState.OFF; reason='below_turn_off_threshold'
        elif self.state==ActuatorState.SAFE:
            self.state=ActuatorState.OFF; reason='recovered_to_safe_off'
        decision=Decision(reading.sensor_id,prev,self.state.value,reason,reading.temperature_c,reading.timestamp)
        self.logger.info(json.dumps(asdict(decision),ensure_ascii=False)); return decision

def load_readings(path:Path):
 for line in path.read_text(encoding='utf8').splitlines():
  if line.strip():
   raw=json.loads(line); yield SensorReading(raw['sensor_id'],raw.get('temperature_c'),raw['timestamp'],raw.get('quality','good'))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--now',type=str,help='instante ISO-8601 para execução reproduzível'); a=ap.parse_args()
 reference=datetime.fromisoformat(a.now.replace('Z','+00:00')) if a.now else datetime.now(timezone.utc)
 logging.basicConfig(level=logging.INFO,format='%(message)s'); c=ThermalController(ControllerConfig()); out=[]
 for r in load_readings(a.input): out.append(asdict(c.update(r,reference)))
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8'); print(json.dumps({'readings':len(out),'final_state':c.state.value}))
if __name__=='__main__': main()
