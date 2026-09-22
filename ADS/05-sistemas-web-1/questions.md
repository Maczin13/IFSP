# Perguntas e respostas de defesa

**Por que o POST responde 303?**  
Uso o padrão Post/Redirect/Get: após persistir, o navegador recebe redirecionamento e faz GET. Isso evita reenviar o POST ao atualizar a página e separa comando de leitura.

**Por que validar no servidor se o HTML tem `required`?**  
A validação do navegador é uma melhoria de experiência, não uma fronteira de segurança. Clientes podem ignorá-la; por isso Flask e SQLite repetem as invariantes.

**Como o MVC aparece no código?**  
As rotas são controllers, SQLite é a camada de modelo/persistência e `templates/index.html` é a view. O cliente HTTP testa a integração sem depender de um navegador real.

**Por que usar query parametrizada?**  
Para separar código SQL de dados e evitar concatenar entrada do usuário. Ainda seriam necessários autenticação, autorização e controles adicionais em sistema real.

**O que o teste de acessibilidade comprova?**  
Ele verifica propriedades concretas do HTML, como associação label/input e role de alerta. Não substitui teste manual com teclado, leitor de tela, contraste e usuários.

**Qual o limite desta aplicação?**  
É uma aplicação didática local: não possui login, CSRF, TLS, rate limiting, observabilidade distribuída ou garantia de concorrência de produção. Essas lacunas são parte da análise crítica, não ocultadas.
