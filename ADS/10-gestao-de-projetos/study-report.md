# Relatório técnico — Gestão de Projetos

## Planeamento e CPM

Eu modelei o plano como um grafo dirigido acíclico de atividades. A passagem para frente calcula ES e EF; a passagem para trás calcula LF e LS a partir da duração do projeto. A folga é LS−ES. Atividades com folga zero formam o caminho crítico e qualquer atraso nelas altera a data prevista, sob as hipóteses do modelo.

Antes do cálculo, o motor valida identificadores únicos e predecessores existentes. A ordenação topológica usa indegree; se nem todas as tarefas forem processadas, há ciclo e a execução falha explicitamente. Isso evita produzir uma programação falsa em um grafo inválido.

## EVM

A análise de valor agregado separa PV (valor planeado), EV (valor agregado) e AC (custo real). CV=EV−AC e SV=EV−PV indicam variações absolutas; CPI=EV/AC e SPI=EV/PV indicam eficiência de custo e prazo. A projeção implementada usa EAC=BAC/CPI, ETC=EAC−AC e VAC=BAC−EAC. Divisões sem base recebem `None` ou erro de domínio, em vez de um número inventado.

## Resultado observado

No fixture, o CPM produz duração 10 e caminho A–B–D. C possui folga de 1 unidade. No EVM, PV=80, EV=72, AC=90 e BAC=120 produzem CV=-18, SV=-8, CPI=0,8, SPI=0,9, EAC=150, ETC=60 e VAC=-30. A interpretação é atraso e sobrecusto relativos à baseline sintética.

## PMI, ISO 21502 e riscos

Estruturei o trabalho de acordo com práticas de escopo, cronograma, custo, riscos, monitorização e controlo discutidas no PMBOK e na ISO 21502. Esses referenciais orientam processos e princípios; o pequeno script não afirma certificação nem conformidade formal. Em projeto real eu ligaria a WBS, calendário, baseline de mudanças, registo de riscos, responsáveis e governança de decisões.

## Limitações

CPM assume durações determinísticas, relações finish-to-start simples e recursos ilimitados. EVM depende de baseline e medição confiáveis; SPI e CPI podem ser enganadores com pouco trabalho medido ou mudança de escopo. Não implementei nivelamento de recursos, Monte Carlo, calendários, dependências externas ou integração de custos.
