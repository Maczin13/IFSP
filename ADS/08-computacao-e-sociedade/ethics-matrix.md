# Matriz ética e de governança

| Risco | Controle implementado | Evidência | Limite e próxima ação |
|---|---|---|---|
| Exposição de PII | Redação de email, CPF e telefone antes da saída | `ethics_lab.py` e testes | Regex não cobre todos os formatos; usar detector validado e revisão |
| Falso negativo em risco | Vocabulário explícito e encaminhamento humano | `risk_flags` e `human_review` | Termos não capturam contexto; avaliação humana é obrigatória |
| Aconselhamento indevido | Disclaimer incondicional | campo `disclaimer` | Não substitui protocolo institucional de crise |
| Uso secundário | Dados sintéticos e sem persistência | fixtures e CLI | Em produção exigir finalidade, retenção e controle de acesso |
| Decisão automatizada | O resultado não decide sobre pessoa | rota limitada/humana | Proibir uso em saúde, emprego ou crédito sem governança específica |

A **LGPD (Lei 13.709/2018)** orienta finalidade, necessidade, transparência, segurança e tratamento reforçado para dados pessoais sensíveis. O laboratório minimiza a saída e não tenta inferir identidade. O **NIST AI RMF** é refletido nas funções Govern, Map, Measure e Manage: documentei contexto e limites, identifiquei riscos de PII e dano, medi casos por testes e encaminhei eventos críticos para revisão humana.

A recomendação da **UNESCO sobre Ética da IA** reforça direitos humanos, proporcionalidade, segurança, explicabilidade e supervisão humana. O projeto **ESTER** é usado como contexto acadêmico para discutir IA em situações de vulnerabilidade; ele não valida este classificador nem autoriza diagnóstico automático. A matriz separa demonstração técnica de alegação clínica.
