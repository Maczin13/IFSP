import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from si_demo import init
def test_schema_and_kpi(): assert init().execute('pragma foreign_keys').fetchone()[0]==1
