# Perguntas e respostas de defesa

**Por que usar sockets em vez de `http.server` ou Flask?**  
Porque o objetivo desta disciplina é tornar observável a fronteira entre transporte e aplicação. A implementação mostra `socket`, `bind`, `listen`, `accept`, `recv` e `sendall`, além do formato HTTP. Frameworks seriam adequados para produto, mas esconderiam as decisões estudadas.

**O que o backlog representa?**  
É a fila associada ao socket de escuta para conexões pendentes, sujeita aos limites e políticas do sistema operacional. Não representa número de requisições processadas nem garante absorção ilimitada. Sob saturação, clientes podem esperar, sofrer timeout ou receber recusa.

**Quem executa o three-way handshake?**  
O kernel TCP, depois que o processo escuta na porta. O código não monta SYN, SYN-ACK ou ACK manualmente. Posso observar esses segmentos com captura de pacotes; no processo, `accept` entrega uma conexão já estabelecida.

**Por que existe timeout no cliente?**  
Para evitar que uma thread permaneça indefinidamente bloqueada em conexão ou leitura incompleta. Timeout é uma decisão de disponibilidade, não substituto de parsing seguro ou controle de recursos.

**Por que a requisição HTTP é separada por CRLF?**  
HTTP/1.1 define a separação de linhas por CRLF e dos cabeçalhos do corpo por uma linha vazia. Ainda assim, o parser é parcial: não implementa chunked encoding, keep-alive, trailers ou todas as regras de RFC 9112.

**Por que `Content-Length` é importante?**  
Ele delimita o corpo em mensagens sem outra codificação de framing. O servidor valida tamanho e grava o valor em bytes, não em caracteres. Uma implementação de produção teria de tratar mais combinações de framing e rejeitar ambiguidades.

**Como a concorrência foi testada?**  
Abri 20 conexões usando `ThreadPoolExecutor` e verifiquei respostas 200 e o contador de conexões concluídas. Isso demonstra comportamento no laboratório; não é benchmark de throughput, latência p95 ou disponibilidade.

**Por que não há TLS?**  
Para manter o foco no TCP/HTTP cru. Sem TLS, conteúdo e credenciais seriam observáveis na rede. Exposição real exigiria `ssl`, certificados, política de versões/cifras, validação de hostname e normalmente um proxy reverso. O projeto ESTER reforça que dados potencialmente sensíveis não devem trafegar sem proteção.
