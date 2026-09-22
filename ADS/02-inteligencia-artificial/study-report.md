# Relatório técnico — Inteligência Artificial

## 1. Problema e delimitação

Eu implementei dois artefatos para estudar representação, aprendizado supervisionado e busca informada. O primeiro classifica frases sintéticas em `sinal` e `sem_sinal`; o segundo encontra um caminho de menor custo em uma grade com obstáculos. O primeiro experimento não diagnostica saúde mental e não deve ser usado para decidir sobre pessoas.

## 2. Classificador Naive Bayes

Substituí a interseção de conjuntos por um pipeline de mercado do scikit-learn. O `CountVectorizer` transforma cada texto em uma matriz esparsa de contagens de unigramas e bigramas, removendo diferenças de caixa e normalizando acentos. O `MultinomialNB` estima a classe por Bayes ingênuo, assumindo independência condicional dos atributos dadas as classes. A suavização `alpha=1.0` evita probabilidade zero para termos ausentes no treinamento.

Separei os dados com `train_test_split(..., stratify=labels, random_state=42)`. O conjunto tem 16 frases sintéticas balanceadas. O script grava tamanho de treino/teste, matriz de confusão, precision, recall, F1 e exemplos de erro em `results/metrics.json`. As métricas são evidência do fixture escolhido, não desempenho clínico nem generalização para linguagem real.

## 3. Busca A*

A busca mantém uma fronteira de prioridade com `f(n)=g(n)+h(n)`. `g(n)` é o custo acumulado desde a origem e `h(n)` é a distância Manhattan até o destino. Como os movimentos têm custo unitário e não há movimentos diagonais, a heurística nunca superestima o custo restante; portanto é admissível e consistente nesse domínio. O mapa `came` reconstrói o caminho sem copiar a lista inteira em cada nó. A implementação retorna caminho, custo e número de nós expandidos e trata gra­des irregulares, posições inválidas e ausência de caminho.

## 4. Resultado observado

A execução da grade de demonstração encontra um caminho de custo 5 entre `(0, 0)` e `(2, 3)`, contornando os obstáculos. A execução do classificador gera `results/metrics.json` com as métricas do holdout e os quatro exemplos de teste. Os valores exatos devem ser lidos desse JSON gerado, pois não substituo uma saída gravada por uma alegação narrativa.

## 5. Limitações e ética

O conjunto é pequeno, sintético e construído para demonstração. Naive Bayes é um baseline probabilístico simples: não compreende contexto, negação, ironia ou causalidade. Uma frase como “não estou ansioso” pode ser classificada de maneira inadequada. A busca A* depende de um mapa correto e da hipótese de custos uniformes; com custos diferentes, a heurística e a função de custo precisam ser revistas. O projeto não usa API externa, não armazena dados pessoais e não oferece aconselhamento. A pesquisa ESTER é contexto acadêmico para discutir IA, saúde mental, privacidade e encaminhamento humano, não validação deste classificador.
