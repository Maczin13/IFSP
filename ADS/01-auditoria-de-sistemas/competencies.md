# Competências demonstradas — Auditoria de Sistemas

Demonstrei a capacidade de modelar o problema, definir entradas e saídas, implementar uma solução executável, testar casos normais e de erro, interpretar métricas e reconhecer limites. A evidência está nos arquivos do módulo, não em uma afirmação genérica.

**Escopo:** Auditar logs sintéticos com validação de esquema, integridade SHA-256, detecção temporal, correlação por usuário/IP e operações privilegiadas.

**Resultado:** A execução sobre 7 registros identificou 4 eventos fora do horário, 1 operação sensível sem aprovação e 1 indício de força bruta; o resumo e o hash estão em results/.

**Limites:** SHA-256 detecta divergência, mas não prova autoria, imutabilidade ou cadeia de custódia. O dataset é sintético e a regra é um indício, não prova de ataque.
