# Perguntas e respostas de defesa

**Anonimização por regex garante anonimização?**  
Não. Ela cobre formatos delimitados de email, CPF e telefone nos fixtures. Pode falhar com texto ofuscado, imagens, identificadores indiretos e combinações de dados. Em produção eu usaria inventário de campos, tokenização controlada, revisão e testes de reidentificação.

**Por que encaminhar para humano em vez de responder?**  
Termos como suicídio, violência e diagnóstico têm potencial de dano. O sistema não tem contexto, competência clínica nem autorização para decidir. `human_review` é uma barreira de segurança e não uma conclusão sobre a pessoa.

**Como a LGPD aparece no código?**  
Minimizo a saída removendo PII, não persisto a entrada, explicito a finalidade didática e não alego base legal ou conformidade integral. Um produto real ainda precisaria controlador, operador, retenção, direitos do titular, segurança e avaliação jurídica.

**O disclaimer impede dano?**  
Não. Ele comunica limites e reduz ambiguidade, mas não substitui guardrails, protocolo de atendimento ou supervisão. Por isso é acompanhado de flags e rota humana.

**Qual a relação com ESTER?**  
ESTER fornece contexto acadêmico para discutir ética de IA em situações de vulnerabilidade. Eu não apresento o laboratório como implementação ou validação do projeto, apenas como experimento técnico coerente com a necessidade de supervisão e limites.
