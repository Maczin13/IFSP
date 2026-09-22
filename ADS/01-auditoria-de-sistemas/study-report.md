# Relatório técnico — Auditoria de Sistemas

## Problema e método
Auditar logs sintéticos com validação de esquema, integridade SHA-256, detecção temporal, correlação por usuário/IP e operações privilegiadas.

Implementei um cenário delimitado, com entrada versionada, processamento determinístico, saída estruturada e testes. A documentação distingue resultado observado de hipótese futura.

## Resultado observado
A execução sobre 7 registros identificou 4 eventos fora do horário, 1 operação sensível sem aprovação e 1 indício de força bruta; o resumo e o hash estão em results/.

## Análise crítica
SHA-256 detecta divergência, mas não prova autoria, imutabilidade ou cadeia de custódia. O dataset é sintético e a regra é um indício, não prova de ataque.

## Rastreabilidade
O código-fonte, os dados sintéticos, os testes e os logs em `results/` formam a cadeia de evidência. Para repetir: execute os comandos do README em um ambiente Python compatível e compare o código de saída e os arquivos gerados.
