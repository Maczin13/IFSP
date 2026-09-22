# Metodologias Ágeis — fluxo de backlog

Este módulo modela um backlog executável com estados, pontos, datas e regras de fluxo. O tracker calcula velocity do período, Lead Time (criação até Done), Cycle Time (In Progress até Done), distribuição por status e limite WIP.

```bash
python3 agile_tracker.py --input backlog.csv --start 2026-09-01 --end 2026-09-30 --wip 3 --output results/metrics.json
python3 -m pytest -q tests
```

O modelo não transforma velocity em meta individual. As métricas são sinais para inspeção e adaptação e dependem da qualidade das datas, do refinamento e da Definition of Done.
