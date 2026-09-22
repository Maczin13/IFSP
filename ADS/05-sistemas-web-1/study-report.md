# Relatório técnico — Sistemas Web 1

## Arquitetura MVC e ciclo HTTP

Eu implementei uma aplicação Flask de tarefas com separação entre roteamento/controlador, persistência e apresentação. A requisição POST do formulário chega à rota `/tasks`; o controlador extrai e normaliza `title`, aplica limites e rejeita dados inválidos com 400. Em caso válido, a camada de persistência usa SQLite e query parametrizada, confirma a transação e responde 303 para que o navegador faça GET em `/`. O GET consulta as tarefas, e Jinja renderiza HTML escapado.

A rota `/api/tasks` expõe representação JSON e DELETE retorna 204 ou 404. O fluxo demonstra diferenças entre corpo de formulário, status HTTP, redirecionamento, persistência e template. A tabela possui restrições `NOT NULL`, `CHECK`, chave primária e timestamp gerado pelo banco.

## Validação e qualidade

A validação ocorre no servidor, independentemente do atributo HTML `required`. Rejeito título vazio, apenas espaços e mais de 120 caracteres. O banco também impõe o limite estrutural do título. Os testes usam fixtures de app/client com banco temporário, verificam status, corpo, redirecionamento, persistência, toggle, API, exclusão e erro 404.

## Acessibilidade

O formulário tem `label` explicitamente associado ao input, `maxlength`, instrução auxiliar e mensagem de erro com `role=alert`. Os botões possuem texto e `aria-label` contextual para alternar tarefas. A interface é semântica, responsiva e operável por teclado. Isso é uma avaliação delimitada de critérios selecionados da WCAG 2.2, não uma declaração de conformidade integral.

## Resultado observado e limites

A suíte registrada em `results/pytest-run.log` exercita o fluxo HTML e JSON. A aplicação é local, usa servidor de desenvolvimento e não implementa autenticação, CSRF, rate limiting, migrações ou implantação multiusuário. Portanto não afirmo segurança, escalabilidade ou disponibilidade de produção; demonstro uma base web acadêmica reproduzível.
