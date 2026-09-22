# Programação para Dispositivos Móveis — Offline-first

O laboratório simula uma arquitetura Android moderna em Python: `StateHolder` expõe estado imutável, `Repository` coordena regras, `LocalStore` representa Room/SQLite e `SyncService` representa um worker de background. Escritas locais são imediatas e entram na Outbox; a sincronização confirma cada evento somente após sucesso remoto.

```bash
python3 -m pytest -q tests
python3 mobile_model.py --db results/mobile.sqlite --out results/state.json
```

Falha de rede não apaga estado local nem remove evento pendente. A sincronização pode ser chamada novamente quando houver conectividade. Não afirmo que este código seja um app Android nem que implemente WorkManager real.
