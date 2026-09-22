# Computação e Sociedade — laboratório de IA responsável

O laboratório processa texto sintético com três controles: anonimização de email, CPF e telefone; detecção explicável de termos de risco; e roteamento para `human_review` quando há sinal crítico. O disclaimer é injetado em toda resposta, inclusive quando não há alerta.

```bash
python3 -m pytest -q tests
printf 'Contato ana@example.com; CPF 123.456.789-09; há risco de suicídio' > /tmp/input.txt
python3 ethics_lab.py --input /tmp/input.txt --output results/evaluation.json
```

O código não diagnostica, não classifica pessoas, não recomenda tratamento e não substitui avaliação humana. Os dados deste módulo são sintéticos.
