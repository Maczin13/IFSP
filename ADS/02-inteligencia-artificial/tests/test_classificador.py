import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from classificador import build_model, DEFAULT_DATA, evaluate
from busca import astar, manhattan

def test_naive_bayes_holdout_is_measurable():
    result = evaluate(DEFAULT_DATA)
    assert result['test_size'] == 4
    assert result['classification_report']['accuracy'] >= 0.5

def test_model_predicts_synthetic_signal():
    model = build_model()
    model.fit([x[0] for x in DEFAULT_DATA], [x[1] for x in DEFAULT_DATA])
    assert model.predict(['estou muito ansioso'])[0] == 'sinal'

def test_astar_optimal_uniform_grid():
    result = astar(['....', '.##.', '....'], (0, 0), (2, 3))
    assert result['found'] is True
    assert result['cost'] == 5

def test_manhattan_heuristic():
    assert manhattan((0, 0), (3, 4)) == 7
