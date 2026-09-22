# Relatório técnico — Redes de Computadores

## Objetivo e transição arquitetural

Eu substituí a implementação baseada em `http.server` por um servidor construído sobre a API de sockets Berkeley/POSIX. O objetivo é observar a fronteira entre transporte e aplicação: o sistema cria um endpoint TCP, aceita conexões, recebe bytes, interpreta uma mensagem HTTP/1.1 e devolve uma resposta formatada manualmente.

## Implementação

O socket é criado com `AF_INET` e `SOCK_STREAM`. Depois de `setsockopt(SO_REUSEADDR)`, o servidor executa `bind`, `listen(backlog)` e `accept`. O valor de backlog representa a fila pendente do socket de escuta; não é uma garantia de que qualquer volume de tráfego será absorvido. Cada conexão aceita é encaminhada a uma thread e recebe timeout de dois segundos.

O parser separa a linha inicial dos cabeçalhos pelo delimitador CRLF, normaliza nomes de cabeçalho para minúsculas e interpreta `Content-Length` com limite de 8192 bytes. A camada de aplicação implementa GET e HEAD para `/healthz` e `/info`, retorna 404 para rota inexistente, 405 com `Allow` para método não permitido e 400 para mensagem malformada. A resposta inclui status, Content-Length, Content-Type e Connection: close.

## Modelo OSI e observabilidade

Na camada de transporte, TCP fornece conexão, ordenação, controle de fluxo e retransmissão; na camada de aplicação, HTTP define método, alvo, cabeçalhos, status e corpo. O código não implementa o three-way handshake — o kernel TCP o faz —, mas o tráfego pode ser observado com `tcpdump`/Wireshark. O servidor registra conexões aceitas, concluídas, erros, bytes e duração, permitindo relacionar comportamento de socket à resposta HTTP.

## Resultado observado

A suíte em `results/pytest-run.log` testa parsing, erro de protocolo, health check, `/info`, 404, 405, HEAD e 20 conexões concorrentes. A execução local confirma que o servidor responde em loopback e que as rotas produzem os status documentados. Os números de métricas do servidor devem ser lidos do log da execução, não inferidos como capacidade de produção.

## Limitações de segurança e escala

O servidor não possui TLS/HTTPS, autenticação, autorização, rate limiting, proteção contra slowloris, HTTP/2, pool de threads ou limites avançados de cabeçalhos. `Connection: close` simplifica o laboratório, mas reduz eficiência. Em tráfego intenso, o backlog pode saturar e o sistema operacional pode recusar conexões; um servidor real exigiria observabilidade, limites, TLS, proxy reverso e testes de carga. A implementação demonstra conhecimento acadêmico de sockets e protocolos, não serviço pronto para Internet.
