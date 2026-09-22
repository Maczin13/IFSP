# Desenvolvimento de Sistemas para Mainframes — batch posicional

O laboratório processa registros ASCII de largura fixa, simulando um arquivo sequencial QSAM e um copybook COBOL. O layout é: posições 1–6 ID, 7–14 data `YYYYMMDD`, 15–26 valor em centavos `PIC 9(12)` e 27–36 status `PIC X(10)`.

```bash
python3 -m pytest -q tests
python3 totaliza.py --input data/input.dat --accepted results/accepted.dat --rejected results/rejected.dat --report results/batch-report.json
```

O programa COBOL documenta o equivalente estrutural, enquanto `totaliza.py` é a execução local reproduzível. O processamento separa aceitos e rejeitados e exige reconciliação `lidos = aceitos + rejeitados`.
