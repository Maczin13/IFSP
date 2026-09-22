import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
import pytest
from automation_controller import ControllerConfig,ThermalController,SensorReading
@pytest.fixture
def controller(): return ThermalController(ControllerConfig(max_sensor_age_s=10))
@pytest.fixture
def reading(): return lambda temp,quality='good': SensorReading('s1',temp,'2026-09-21T10:00:00+00:00',quality)
