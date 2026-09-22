# Perguntas e respostas de defesa

**Por que `MultinomialNB` é diferente da regra lexical anterior?**  
A regra lexical apenas verificava a presença de palavras escolhidas manualmente. O Naive Bayes aprende parâmetros a partir de exemplos rotulados: estima a probabilidade de cada termo por classe e combina essas evidências sob uma hipótese de independência condicional. Ainda é um baseline simples, mas é um modelo supervisionado mensurável.

**O que significa `alpha=1.0`?**  
É a suavização de Laplace. Ela adiciona uma quantidade positiva às contagens para evitar probabilidades nulas quando uma palavra do teste não aparece em uma classe de treino. A escolha afeta o viés do modelo e deve ser comparada por validação, não tratada como universalmente ótima.

**Por que a acurácia não basta?**  
Uma classe desbalanceada pode produzir acurácia alta mesmo ignorando a classe minoritária. Por isso publico precision, recall, F1, suporte e matriz de confusão. Para um sistema de encaminhamento, falsos negativos e falsos positivos têm custos diferentes e precisam ser analisados separadamente.

**Por que separar treino e teste antes de avaliar?**  
Avaliar nos mesmos exemplos usados para ajustar o vocabulário e o classificador produz estimativa otimista. O holdout mede generalização apenas para a distribuição sintética definida. Com uma base maior, eu usaria validação cruzada estratificada e manteria um teste final intocado.

**Por que A* encontra o caminho ótimo neste mapa?**  
A prioridade é `f(n)=g(n)+h(n)`. Com custos unitários e movimentos ortogonais, a Manhattan é admissível e consistente: nunca superestima o número mínimo de movimentos restantes. Assim, quando o destino é retirado da fila de prioridade, o custo encontrado é ótimo para esse domínio.

**O que aconteceria com uma heurística superestimada?**  
Ela poderia fazer A* encontrar rapidamente um caminho que não é ótimo. O algoritmo ainda pode ser útil como busca aproximada, mas eu não poderia afirmar optimalidade sem a propriedade de admissibilidade ou sem uma prova específica para o domínio.

**Como você tratou ética e saúde mental?**  
Usei somente frases sintéticas, não persistentes como dados pessoais. A saída é um sinal para revisão humana e contém limite explícito; não diagnostica, não recomenda tratamento e não substitui atendimento profissional. O artigo ESTER é utilizado apenas como contexto de pesquisa e ética, não como validação do modelo.

**Qual é o principal erro esperado do classificador?**  
Negação, ironia, contexto e variações linguísticas. O vetor de contagem representa palavras e n-gramas, não a semântica completa. Por isso a análise deve incluir exemplos de erro, avaliação por fenômeno linguístico e revisão humana.
