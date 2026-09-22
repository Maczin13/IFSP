# Relatório técnico — Metodologias Ágeis

## Modelo de trabalho

Eu implementei um tracker de backlog que representa itens como objetos com identificador, título, pontos, estado e datas de fluxo. A transição Todo → In Progress → Done é explícita e mantém invariantes: item concluído não retrocede, item Done exige data de conclusão e datas não podem violar a ordem temporal.

## Scrum e Kanban

Relaciono pontos à capacidade estimada do item, não a horas reais. A velocity soma pontos concluídos em uma janela de sprint; ela é uma medida histórica para planejamento, não uma meta de produtividade individual. A visão Kanban aparece no limite WIP: quando a quantidade de itens em andamento atinge o limite, nova entrada é rejeitada para favorecer foco e fluxo.

## Métricas de fluxo

Lead Time mede criação até conclusão; Cycle Time mede início de trabalho até conclusão. A implementação calcula médias somente para itens com datas completas e distribui o backlog por estado. Em um produto real eu também observaria percentis, throughput, aging do WIP e work item age, pois médias escondem caudas e bloqueios.

## Resultado e testes

O backlog contém histórias de autenticação, API, acessibilidade, observabilidade e carga. A suíte pytest cobre velocity, filtros, limite WIP, pontos inválidos, datas obrigatórias, transições proibidas, item inexistente e cálculo temporal. O resultado em `results/pytest-run.log` é a evidência executada; `results/metrics.json` registra as métricas do CSV.

## Limitações

Pontos são relativos e não comparáveis entre equipes. O tracker não modela dependências, bloqueios, classes de serviço, feriados ou mudanças de escopo. Também não substitui facilitação, revisão, retrospectiva ou julgamento do Product Owner. A validade das métricas depende de uma Definition of Done consistente e de dados de fluxo honestos.
