# Redes de Computadores — servidor TCP/HTTP manual

O artefato principal é `tcp_web_server.py`. Ele usa diretamente `socket.AF_INET` e `socket.SOCK_STREAM`, configura `SO_REUSEADDR`, faz `bind`, `listen(backlog)`, `accept` e cria uma thread por conexão. O parsing da linha inicial e dos cabeçalhos HTTP é feito no próprio módulo, sem `http.server`, Flask ou framework.

```bash
python3 -m pip install -r requirements.txt
python3 tcp_web_server.py --host 127.0.0.1 --port 8080 --backlog 16
curl -i http://127.0.0.1:8080/healthz
curl -i http://127.0.0.1:8080/info
python3 -m pytest -q tests
```

O servidor é intencionalmente local e didático. Ele não implementa TLS, autenticação, HTTP/2, persistência, rate limiting ou endurecimento para exposição pública.
