# Sistemas Web 2 — API RESTful FastAPI

A aplicação expõe uma API HTTP real com Pydantic e contrato OpenAPI automático. Rotas: `GET /items`, `POST /items` com 201, `GET /items/{id}`, `DELETE /items/{id}` com 204, 404 para recurso ausente, 422 para payload inválido e `GET /docs` para Swagger.

```bash
python3 -m pip install -r requirements.txt
uvicorn api:app --reload
python3 -m pytest -q tests
```

A persistência é em memória para manter o laboratório determinístico. Não há JWT, rate limiting, banco ou autorização; essas limitações não são ocultadas.
