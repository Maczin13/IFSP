# Relatório técnico — Qualidade de Software

## Problema

Eu abandonei o cenário artificial de uma calculadora e modelei um Processador de Vendas. O objetivo foi testar um fluxo com decisões de negócio e falhas relevantes: uma venda precisa conter itens válidos, cada quantidade deve ser compatível com o estoque, o cupom precisa estar ativo e seu percentual deve respeitar o domínio definido. O processamento utiliza `Decimal` para evitar erros de representação binária em valores monetários.

## Estratégia de testes

A suíte é organizada com pytest. A fixture `valid_items` fornece uma venda base independente para cada teste; `pytest.raises` verifica que exceções específicas são lançadas; `pytest.mark.parametrize` cobre partições de quantidade e percentuais inválidos sem duplicar a lógica dos testes. Os testes incluem caminho feliz, estoque insuficiente, venda vazia, cupom inativo, subtotal mínimo, tipos inválidos, arredondamento HALF_UP e não mutação da entrada.

Eu não trato cobertura de linhas como sinônimo de qualidade. A matriz de testes começa por requisitos e riscos: erro de tipo pode quebrar o contrato da API; quantidade acima do estoque pode gerar venda impossível; cupom inativo pode causar perda financeira; arredondamento incorreto pode gerar divergência contábil. Cada risco possui um caso verificável.

## Resultado observado

A execução registrada em `results/pytest-run.log` aprovou os testes da pasta. A execução do fixture `data/sale-valid.json` produz subtotal de 320,00, desconto de 32,00 e total de 288,00. O caso de estoque inválido termina com exceção `StockError`, como definido no contrato.

## Análise crítica

O domínio ainda não possui banco, API, concorrência, integração de pagamento ou testes de contrato HTTP. Portanto não afirmo segurança, desempenho de produção ou conformidade financeira. Uma evolução responsável incluiria testes de mutação, property-based testing com Hypothesis, persistência transacional, idempotência do pedido, auditoria de alterações e testes de integração.
