# Auditoria de Sistemas

## Objetivo
Auditar logs sintéticos com validação de esquema, integridade SHA-256, detecção temporal, correlação por usuário/IP e operações privilegiadas.

## Execução reproduzível

```bash
python3 -m pytest -q tests
python3 auditoria.py
```

Os dados em `data/` são fixtures sintéticas. Os arquivos em `results/` foram gerados por execução local e devem ser lidos junto com o código e os testes. Este módulo é um laboratório acadêmico: não representa ambiente de produção, cliente, emprego, certificação ou conformidade formal.
