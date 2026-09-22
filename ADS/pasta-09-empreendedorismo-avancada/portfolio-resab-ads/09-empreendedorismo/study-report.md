# Relatório técnico — Empreendedorismo

## Problema e MVP

Eu transformei um organizador de estudos em um laboratório de decisão empreendedora. Cada iniciativa possui alcance, impacto, confiança, esforço, horas, valor esperado e status da hipótese. O MVP não tenta resolver todo o planejamento: sua fatia vertical é priorizar o próximo investimento de tempo e produzir uma saída auditável.

## Modelos de priorização

RICE é calculado como Reach × Impact × Confidence / Effort. A confiança reduz a pontuação de ideias atraentes, mas pouco evidenciadas. Também implementei WSJF simplificado como (Cost of Delay + Impact) / Effort e ROI de tempo como valor esperado / horas. Os modelos não são verdades concorrentes; são lentes para comparar iniciativas e tornar premissas discutíveis.

O método de portfólio ordena por RICE e seleciona itens enquanto não ultrapassa o orçamento de horas. Essa escolha é deliberadamente gulosa e não afirma otimização global; um produto real poderia usar programação inteira ou restrições de dependência.

## Hipóteses e tração

O CSV separa hipóteses não testadas, em teste e validadas. A métrica `validation_rate` é apenas a razão entre hipóteses marcadas como validadas e o total; não confundo esse rótulo com evidência de mercado. Validação exigiria experimento com critério anterior, amostra, observação e decisão. Métricas de tração relevantes seriam ativação, retenção semanal, conclusão de tarefas, tempo até primeiro valor, conversão e disposição a pagar.

## Resultado observado

A suíte em `results/pytest-run.log` testa ranking, ROI, orçamento, tração, limites de confiança e esforço e métodos inválidos. `results/metrics.json` registra a execução do backlog sintético. A análise Canvas e SWOT explicita segmentos, proposta, canais, custos, ameaças e critérios de pivotar.

## Limitações

RICE, WSJF e ROI dependem de estimativas subjetivas e podem criar falsa precisão. O código não tem usuários, entrevistas, receita, cohortes ou telemetria de produto. Portanto eu não afirmo product-market fit. O próximo experimento de baixo custo seria uma landing page e entrevistas com critério de sucesso definido antes da coleta.
