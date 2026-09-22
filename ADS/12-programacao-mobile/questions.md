# Perguntas e respostas de defesa

**Por que gravar localmente antes de sincronizar?**  
Para que a ação do usuário não dependa de conectividade. A outbox transforma a intenção em evento persistente e permite reprocessamento após reconexão.

**Por que remover da fila só depois do ACK?**  
Antes do ACK, a operação pode ter sido perdida. Remover cedo causa perda silenciosa; remover depois permite retry. O servidor real deve aceitar idempotency key para evitar duplicação.

**Como o UDF evita estado arbitrário?**  
A ação entra pelo StateHolder, regras passam pelo Repository e a nova leitura do store forma o estado observado. A UI não muta diretamente uma lista compartilhada.

**Como conflitos local/remoto são tratados?**  
A versão é enviada como metadado para permitir detecção. O laboratório para antes de escolher uma política automática; em produto eu definiria merge, last-write-wins ou revisão humana conforme o domínio.

**Por que o MASVS é relevante?**  
Dados locais, tokens, logs e comunicação são superfícies de ataque mobile. SQLite simula persistência, mas não deve guardar segredo sem proteção de plataforma, criptografia e controle de backup.
