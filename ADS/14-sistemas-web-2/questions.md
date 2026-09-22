# Perguntas e respostas de defesa

**Por que 422 e não 400 para payload inválido?**  
O FastAPI/Pydantic usa 422 para indicar que a requisição tem formato interpretável, mas viola o contrato semântico do modelo. Um JSON malformado poderia ser tratado como 400; a escolha deve ser documentada.

**O que o OpenAPI comprova?**  
Ele descreve rotas, métodos, modelos e respostas do código. Não prova segurança, disponibilidade ou persistência; é contrato de integração e documentação executável.

**Por que o TestClient é teste de integração?**  
Ele envia uma requisição ao aplicativo ASGI, atravessa roteamento, validação, handler e serialização. Não abre uma porta TCP, então um teste end-to-end ainda seria necessário para servidor e proxy.

**Quais riscos OWASP permanecem?**  
Sem autenticação e autorização, qualquer cliente pode ler ou excluir itens. Sem quota, um cliente pode consumir recursos. A persistência em memória também perde dados e não oferece auditoria. Essas lacunas estão registradas como escopo.

**Como evoluiria a API?**  
Eu adicionaria banco com transação, autenticação OIDC/JWT, autorização por usuário, idempotency key, paginação, rate limiting, logs estruturados, validação de saída, migrações e testes de contrato.
