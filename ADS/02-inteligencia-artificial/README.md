# Inteligência Artificial — experimento supervisionado e busca informada

Este módulo contém dois experimentos executáveis. `classificador.py` treina um pipeline `CountVectorizer + MultinomialNB` sobre frases **sintéticas** e produz métricas de classificação. `busca.py` implementa A* em uma grade com obstáculos, usando a distância Manhattan como heurística admissível para custos uniformes.

```bash
python3 -m pip install -r requirements.txt
python3 classificador.py --data data/classificacao.json --out results/metrics.json
python3 busca.py
python3 -m pytest -q tests
```

A classe `sinal` não é diagnóstico, triagem clínica nem recomendação de tratamento. Ela representa apenas um rótulo didático para encaminhamento a revisão humana. Não inserir relatos pessoais ou dados sensíveis reais no repositório.
