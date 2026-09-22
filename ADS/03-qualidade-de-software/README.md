# Qualidade de Software — Processador de Vendas

Substituí a calculadora elementar por um domínio com regras de negócio observáveis: validação de tipos, estoque, cupons ativos, percentual permitido, subtotal mínimo, arredondamento monetário e exceções específicas.

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -q tests
python3 processador_vendas.py data/sale-valid.json
```

A suíte utiliza `pytest.fixture` para dados compartilhados, `pytest.raises` para contratos de erro e `pytest.mark.parametrize` para partições de equivalência. O projeto é um laboratório acadêmico com dados sintéticos; não representa vendas reais.
