# Sistemas Web 1 — aplicação Flask MVC

A aplicação demonstra o ciclo completo de uma requisição web: navegador envia formulário HTTP, rota Flask valida a entrada, serviço grava em SQLite parametrizado, resposta 303 redireciona para GET e o template Jinja renderiza o estado. Também existe uma API mínima para listar e excluir tarefas.

```bash
python3 -m pip install -r requirements.txt
flask --app app run --debug
python3 -m pytest -q tests
```

A aplicação usa `instance/tasks.sqlite` por padrão. Para teste, a fixture cria um banco temporário por caso. Os templates usam label associado, foco padrão de controles, mensagem `role=alert`, linguagem clara e operação por teclado como parte do escopo WCAG 2.2.
