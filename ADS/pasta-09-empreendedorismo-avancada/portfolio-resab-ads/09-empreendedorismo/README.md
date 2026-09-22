# Empreendedorismo — laboratório de MVP

Eu modelei um organizador de estudos como MVP e explicitei suas hipóteses de valor. O programa prioriza iniciativas por RICE, calcula WSJF simplificado e ROI de tempo, seleciona um portfólio dentro de um orçamento de horas e acompanha hipóteses `untested`, `testing` e `validated`.

```bash
python3 organizador.py --input backlog.csv --hours 10 --output results/metrics.json
python3 -m pytest -q tests
```

Os dados são sintéticos. O código calcula sinais de priorização; não prova product-market fit nem receita.
