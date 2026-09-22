from pathlib import Path
import json, subprocess, sys
R=Path(__file__).parent
subprocess.run([sys.executable,'classificador.py','--data','data/classificacao.json','--out','results/metrics.json'],cwd=R,check=True)
from busca import demo
(R/'results/astar-demo.json').write_text(json.dumps(demo(),indent=2),encoding='utf8')
print('artefatos gerados em results/')
