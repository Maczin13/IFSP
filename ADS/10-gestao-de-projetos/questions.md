# Perguntas e respostas de defesa

**Por que detetar ciclos antes do CPM?**  
Datas mais cedo dependem de uma ordem topológica. Num ciclo não existe primeira atividade válida; continuar produziria datas sem significado. O algoritmo compara o número processado com o total e lança erro.

**O caminho crítico é sempre único?**  
Não. Podem existir vários caminhos com folga zero. O resultado retorna todos os itens críticos ordenados pelo grafo, não assume unicidade.

**O que significa CPI menor que 1?**  
EV/AC menor que 1 indica que o valor agregado é inferior ao custo real por unidade de baseline. No fixture CPI=0,8, sinalizando ineficiência de custo.

**SPI menor que 1 prova atraso?**  
Indica progresso agregado inferior ao planeado na data de medição, mas a interpretação depende da baseline, da regra de valor e da qualidade dos dados. No fixture SPI=0,9.

**Por que EAC=BAC/CPI é apenas uma projeção?**  
Ela assume que a eficiência de custo observada continuará. Outros cenários usam trabalho restante e premissas diferentes. Eu apresento a fórmula como previsão condicionada, não como orçamento definitivo.

**O que o CPM não representa?**  
Recursos, calendários, feriados, restrições, custos e incerteza probabilística não aparecem no grafo simples. Uma extensão usaria nivelamento, PERT/Monte Carlo e integração com baseline de custos.
