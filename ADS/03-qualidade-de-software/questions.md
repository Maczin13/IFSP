# Perguntas e respostas de defesa

**Por que o Processador de Vendas é um caso melhor que a calculadora?**  
Porque contém regras de negócio com decisões e riscos reais de software: tipos inválidos, estoque insuficiente, cupom inativo, limites de desconto e arredondamento monetário. Isso permite demonstrar testes positivos, negativos, de fronteira e de exceção.

**Por que usar `pytest.fixture`?**  
A fixture centraliza dados válidos e fornece isolamento por teste. Se a fixture fosse mutada, o pytest cria uma nova instância para o teste seguinte. Isso reduz duplicação e evita dependência oculta entre casos.

**Por que `pytest.raises` é melhor que try/except manual?**  
Ele expressa diretamente o contrato: durante o bloco deve ocorrer uma exceção do tipo esperado, e `match` verifica parte da mensagem. Um teste que não lança a exceção falha automaticamente; não existe o risco de um `assert` depois de um `try` mascarar o comportamento.

**Por que parametrizar os testes?**  
Quantidade zero, negativa, booleana, decimal e texto pertencem a partições diferentes do contrato. `pytest.mark.parametrize` executa todos os exemplos contra a mesma regra e torna explícita a tabela de entradas inválidas.

**Por que Decimal em vez de float?**  
Valores monetários precisam de representação decimal previsível e arredondamento explícito. Uso `Decimal` e `ROUND_HALF_UP` para que o desconto de 33,333% sobre 10,05 seja arredondado de forma documentada. Ainda seria necessário definir política fiscal e de moeda em um sistema real.

**Qual a diferença entre ValidationError, CouponError e StockError?**  
`ValidationError` indica contrato estrutural ou tipo inválido; `CouponError` indica regra de elegibilidade do cupom; `StockError` indica impossibilidade operacional por quantidade. Exceções específicas permitem que uma camada superior trate cada falha de modo diferente.

**O que os testes ainda não provam?**  
Não provam integração com banco, concorrência, pagamento, segurança, desempenho, acessibilidade ou ausência de todos os defeitos. Também não provam cobertura total do espaço de valores; são evidências delimitadas pelos casos implementados.

**Como evoluiria a confiança na suíte?**  
Eu adicionaria Hypothesis para invariantes monetários, mutation testing para avaliar se os testes detectam defeitos semeados, testes de integração com persistência transacional e CI com versões suportadas do Python. Os resultados só seriam declarados depois de executar cada ferramenta.
