# Competências demonstradas — Redes de Computadores

Demonstrei criação e ciclo de vida de sockets TCP IPv4, associação de endereço e porta, backlog, aceitação de conexões, concorrência por threads, timeouts, parsing manual de HTTP/1.1, códigos de status, cabeçalhos e observabilidade de bytes/duração.

A implementação separa transporte (`socket`) de aplicação (parser e roteador), possui testes de protocolo e explicita limitações: o handshake TCP é realizado pelo kernel, TLS não está implementado e a escala não foi alegada sem benchmark. O diagrama em `network-flow.mmd` relaciona cliente, handshake, socket, HTTP, resposta e FIN.
