# Relatório técnico — Governança e Gestão de TI

## Motor de auditoria

Eu implementei uma matriz de controles orientada a objetos. Cada controle possui objetivo, framework, proprietário, evidência, status e efetividade. A regra PASS exige status implementado, evidência não vazia e efetividade mínima 3. Caso contrário, o relatório marca FAIL e preserva os campos para análise.

A maturidade sintética converte controles implementados aprovados em nível 5, parciais em nível 2 e ausentes em nível 0; uma falha nunca recebe pontuação superior a 2. A média normalizada fornece um indicador comparável da fixture, mas não é uma avaliação oficial CMMI ou COBIT.

## Marcos de referência

Usei COBIT 2019 para relacionar governança a Evaluate, Direct and Monitor (EDM) e objetivos de alinhamento/planejamento APO. Usei ITIL 4 para contextualizar acordos de serviço, incidentes e mudanças. A ISO/IEC 38500 orienta princípios de responsabilidade, estratégia, aquisição, desempenho, conformidade e comportamento humano. O código transforma esses marcos em campos e regras verificáveis, sem alegar que uma linha CSV cobre a complexidade institucional.

## Resultado observado

A matriz possui cinco controles: três frameworks COBIT/ITIL, dois aprovados e três com lacunas ou evidência parcial. A suíte em `results/pytest-run.log` cobre PASS/FAIL, pontuação, agregação por framework, campos inválidos e matriz vazia. `results/audit.json` registra o relatório completo e permite rastrear cada decisão ao CSV.

## Limites de compliance

Uma auditoria real exigiria escopo aprovado, independência, amostragem, entrevistas, evidência original, período, critérios, exceções, plano de ação e revisão. Este laboratório não verifica autenticidade de documentos, operação contínua, segregação de funções ou eficácia real. A pontuação é um instrumento de aprendizagem e não uma certificação.
