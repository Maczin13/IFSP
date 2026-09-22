# Relatório técnico — Computação e Sociedade

## Problema e abordagem

Eu implementei um laboratório determinístico para demonstrar que uma aplicação de texto responsável precisa tratar privacidade e limites antes de produzir orientação. A entrada é anonimizada para remover padrões de email, CPF e telefone; depois termos críticos recebem flags semânticas e a saída escolhe entre orientação limitada ou encaminhamento humano.

## Decisões técnicas

Usei expressões regulares separadas por tipo de PII para tornar a transformação auditável. O resultado preserva a estrutura textual, mas substitui o valor por marcadores. A detecção usa um vocabulário explícito e `casefold`, de modo que a decisão possa ser inspecionada. Não há modelo opaco nem inferência de identidade. O disclaimer é uma constante injetada incondicionalmente, evitando que um caminho aparentemente seguro omita o limite.

## Ética aplicada

A matriz relaciona controles ao princípio de necessidade da LGPD, à governança e gestão de risco do NIST AI RMF e à supervisão humana defendida pela UNESCO. O ESTER entra como contexto acadêmico para refletir sobre tecnologia em situações de vulnerabilidade; não uso a pesquisa como licença para diagnosticar, classificar pessoas ou substituir profissionais.

## Resultado observado

A suíte em `results/pytest-run.log` cobre os três tipos de PII, quatro categorias de risco, texto sem alerta, disclaimer, tipo inválido e múltiplas flags. A evidência mede comportamento do código em fixtures sintéticas. Uma flag não significa que o texto seja verdadeiro nem que exista diagnóstico: significa apenas que a política conservadora exige revisão humana.

## Limitações

Regex pode falhar em formatos nacionais, ofuscações e contexto. Vocabulário pode gerar falso positivo e falso negativo, não entende ironia e não representa avaliação clínica. Em implantação real eu exigiria revisão de DPIA, controle de acesso, retenção mínima, auditoria, testes linguísticos, protocolo de crise, validação com partes afetadas e monitoramento de vieses.
