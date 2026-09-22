# Sistemas de Informação

## Objetivo
Esquema relacional com FK/CHECK e KPI operacional observável; limitações de amostra documentadas.

## Execução reproduzível

```bash
python3 -m pytest -q tests
python3 demo.py
```

Os dados em `data/` são fixtures sintéticas. Os arquivos em `results/` foram gerados por execução local e devem ser lidos junto com o código e os testes. Este módulo é um laboratório acadêmico: não representa ambiente de produção, cliente, emprego, certificação ou conformidade formal.
