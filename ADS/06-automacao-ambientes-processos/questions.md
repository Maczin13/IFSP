# Perguntas e respostas de defesa

**Por que um único limiar causa chattering?**  
Ruído em torno do limite alterna a comparação a cada amostra. A histerese cria limites diferentes para ligar e desligar, reduzindo comandos repetidos e tornando o estado dependente do histórico de forma explícita.

**Por que `SAFE` não é simplesmente `OFF`?**  
`OFF` pode significar decisão normal de não acionar; `SAFE` registra que a decisão ocorreu por falha/risco. Essa distinção permite telemetria, alerta e política de recuperação sem esconder problema de sensor.

**O que acontece se o sensor ficar atrasado?**  
Comparo o timestamp com o instante de avaliação. Acima da idade configurada, a leitura é `stale_reading` e o estado passa para SAFE. Em sistema distribuído real, relógios, latência e sincronização precisariam ser tratados.

**O que o NISTIR 8259A acrescenta?**  
Ele organiza capacidades de cibersegurança de dispositivos IoT, como identidade, configuração, proteção de dados, controle de acesso, atualização e conhecimento do estado. Meu código implementa somente uma parte didática e deixa rede, credenciais e atualização como limitações explícitas.

**Por que não afirmar que MQTT está implementado?**  
O módulo não abre broker nem publica mensagens. A decisão técnica correta é separar o controlador puro de um adaptador MQTT futuro, que exigiria autenticação, TLS, ACL, QoS, reconexão e testes de perda/duplicidade.
