from datetime import datetime,timezone
import pytest
from automation_controller import ActuatorState,ControllerConfig
def now(): return datetime.fromisoformat('2026-09-21T10:00:05+00:00')
def test_hysteresis_sequence(controller,reading):
 assert controller.update(reading(31),now()).state=='ON'
 assert controller.update(reading(29),now()).state=='ON'
 assert controller.update(reading(27),now()).state=='OFF'
def test_invalid_sensor_is_fail_safe(controller,reading):
 assert controller.update(reading(None,'bad'),now()).state=='SAFE'
 assert controller.update(reading(24),now()).reason=='recovered_to_safe_off'
def test_stale_sensor_is_safe(controller,reading):
 old=reading(31); assert controller.update(old,datetime.fromisoformat('2026-09-21T10:00:30+00:00')).reason=='stale_reading'
def test_config_rejects_inverted_hysteresis():
 with pytest.raises(ValueError): ControllerConfig(turn_on_c=28,turn_off_c=30)
def test_nan_is_safe(controller,reading):
 assert controller.update(reading(float('nan')),now()).state=='SAFE'
