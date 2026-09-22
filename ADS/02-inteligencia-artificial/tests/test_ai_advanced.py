import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from busca import astar,manhattan
from classificador import build_model,DEFAULT_DATA,evaluate

def test_astar_finds_optimal_path_in_uniform_grid():
 r=astar(['....','.##.','....'],(0,0),(2,3)); assert r['found'] and r['cost']==5
 assert r['path'][0]==(0,0) and r['path'][-1]==(2,3)
def test_astar_reports_unreachable(): assert astar(['.#.','###','...'],(0,0),(2,2))['found'] is False
def test_heuristic_is_manhattan(): assert manhattan((0,0),(3,4))==7
def test_model_learns_holdout():
 r=evaluate(DEFAULT_DATA); assert r['test_size']==4 and r['classification_report']['accuracy']>=0.5
def test_model_handles_accented_text():
 m=build_model(); m.fit([x[0] for x in DEFAULT_DATA],[x[1] for x in DEFAULT_DATA]); assert m.predict(['estou com muita ansiedade'])[0]=='sinal'
