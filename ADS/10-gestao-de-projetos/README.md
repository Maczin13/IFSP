# Gestão de Projetos — CPM e Earned Value

O motor calcula o caminho crítico com datas mais cedo (ES/EF), datas mais tarde (LS/LF), folga e duração do projeto. Também calcula PV, EV, AC, BAC, CV, SV, CPI, SPI, EAC, ETC e VAC.

`wbs.csv` organiza o laboratório em pacotes de trabalho, entregáveis, critérios de aceitação e papéis. `risk-register.csv` complementa a WBS com probabilidade, impacto, resposta e gatilho.

```bash
python3 project_control.py --input data/project.json --output results/metrics.json
python3 -m pytest -q tests
```

O fixture é sintético e usa unidades de tempo/custo abstratas. As métricas não representam projeto real nem substituem baseline aprovada.
