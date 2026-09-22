# Governança e Gestão de TI — auditoria de controles

O laboratório lê uma matriz CSV, valida o domínio dos controles, avalia PASS/FAIL, calcula maturidade de 0 a 5 e gera relatório JSON auditável. A amostra relaciona objetivos COBIT 2019 EDM/APO e práticas de gestão de serviços ITIL 4.

```bash
python3 governance_lab.py --input controls.csv --output results/audit.json
python3 -m pytest -q tests
```

O resultado é uma avaliação acadêmica de evidências sintéticas, não uma auditoria de certificação ou opinião de compliance.
