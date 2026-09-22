# Relatório técnico — Sistemas Web 2

## Arquitetura e contrato

Eu implementei uma API FastAPI com separação inicial entre transporte, validação e repositório. O modelo Pydantic `ItemCreate` define título obrigatório de 1 a 120 caracteres e prioridade de 1 a 5; `Item` adiciona identificador. O framework converte o modelo em JSON Schema e publica OpenAPI, Swagger UI e ReDoc.

O fluxo POST valida o corpo antes do handler e cria um recurso com 201 Created. GET consulta o repositório, DELETE retorna 204 No Content e recurso ausente produz 404 Not Found. Falhas de contrato são 422 Unprocessable Entity. Isso é diferente de retornar dicionários: o TestClient injeta requisições HTTP no ASGI e observa status, headers e corpo.

## Segurança e OWASP API Security

A API não usa autenticação, então não afirmo proteção contra Broken Object Level Authorization, Broken Authentication ou Unrestricted Resource Consumption. Também não há rate limiting, auditoria, CORS restritivo ou persistência. O relatório explicita esses riscos e os controles necessários: identidade JWT/OIDC, autorização por objeto, limites de payload, quotas, validação de saída, logs e gestão de segredos.

## Resultado observado

A suíte em `results/pytest-run.log` cobre OpenAPI, criação 201, leitura, listagem, deleção 204, 404, validação 422 e health check. O contrato é verificável em `/openapi.json`. A aplicação é um laboratório acadêmico com repositório em memória; não representa API pronta para Internet.
