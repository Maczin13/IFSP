# Relatório técnico — Programação para Dispositivos Móveis

## Arquitetura

Eu organizei o laboratório em fluxo unidirecional de dados. A ação do usuário passa pelo `StateHolder`, o `Repository` aplica regras e grava no `LocalStore`, e o novo `AppState` é derivado do armazenamento. A UI hipotética observa estado; ela não escreve diretamente no banco. Essa separação reduz acoplamento e torna transições testáveis.

O `LocalStore` usa SQLite e duas tabelas: notas e outbox. Cada alteração recebe versão e uma operação serializada. O Repository garante título válido, cria identificador e incrementa versão no toggle. O `SyncService` lê eventos na ordem, chama o adaptador remoto e remove o item somente depois do ACK.

## Offline-first e resiliência

A escrita local não depende de rede. Se o adaptador lançar `NetworkUnavailable`, o evento permanece na fila e o contador de tentativas é incrementado. Uma nova execução pode reenviar o mesmo item. Em um app Android, esse papel seria associado a Room, ViewModel/StateFlow e WorkManager com restrições de rede e política de backoff.

## Conflitos e segurança

A versão local torna divergência detectável, mas este laboratório não implementa servidor de conflitos. Um produto real escolheria last-write-wins, merge por campo ou resolução humana, com idempotency key. O armazenamento local não contém dados sensíveis no fixture; seguindo o OWASP MASVS, credenciais não devem ser gravadas em texto puro e tokens devem usar armazenamento protegido.

## Resultado observado

A suíte em `results/pytest-run.log` verifica escrita offline, outbox, título inválido, versionamento, falha de rede, reconexão e preservação local. `results/state.json` registra o estado final da execução CLI. Os testes são evidência do modelo, não prova de comportamento em todas as versões Android ou redes móveis.
