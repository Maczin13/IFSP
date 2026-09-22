# Automação de Ambientes e Processos — controlador IoT

O artefato principal é `automation_controller.py`. Ele modela telemetria, configuração, atuador e decisão como objetos imutáveis/estado explícito. A máquina térmica usa histerese: liga em 30°C ou mais, desliga em 28°C ou menos e mantém o estado entre os limites. Leitura inválida, qualidade ruim ou sensor atrasado leva o atuador a `SAFE`.

```bash
python3 -m pip install -r requirements.txt
python3 automation_controller.py --input data/readings.jsonl --output results/decisions.json --now 2026-09-21T10:00:05+00:00
python3 -m pytest -q tests
```

O parâmetro `--now` torna a avaliação de idade do sensor reproduzível. O módulo simula o sensor e o atuador; não aciona hardware nem conecta a MQTT.
