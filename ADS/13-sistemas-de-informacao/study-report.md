# Relatório técnico — Sistemas de Informação

## Problema e método
Esquema relacional com FK/CHECK e KPI operacional observável; limitações de amostra documentadas.

Implementei um cenário delimitado, com entrada versionada, processamento determinístico, saída estruturada e testes. A documentação distingue resultado observado de hipótese futura.

## Resultado observado
Os testes e o script principal foram executados localmente; o log em `results/` registra a saída, o código de retorno e o ambiente. A interpretação deve ser feita sobre esse log, não sobre uma afirmação narrativa.

## Análise crítica
A amostra é pequena e sintética. O código não demonstra escala, segurança de produção, implantação real ou experiência profissional.

## Rastreabilidade
O código-fonte, os dados sintéticos, os testes e os logs em `results/` formam a cadeia de evidência. Para repetir: execute os comandos do README em um ambiente Python compatível e compare o código de saída e os arquivos gerados.
