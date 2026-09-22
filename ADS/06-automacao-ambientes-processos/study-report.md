# Relatório técnico — Automação de Ambientes e Processos

## Modelo de domínio

Eu substituí a função global de nove linhas por um controlador orientado a objetos. `SensorReading` representa uma amostra com identidade, temperatura, timestamp e qualidade; `ControllerConfig` concentra os limites e a idade máxima; `ThermalController` mantém o estado do atuador e produz uma `Decision` auditável. A separação evita misturar parsing, política e efeito de atuação.

## Máquina de estados e histerese

A política possui estados `OFF`, `ON` e `SAFE`. Um sensor saudável acima de 30°C leva `OFF` a `ON`; abaixo de 28°C leva `ON` a `OFF`; na banda intermediária, o estado é mantido. Essa banda de 2°C reduz chattering causado por ruído perto de um único limiar. A função é determinística quando recebe a mesma leitura, configuração e estado anterior.

## Falhas e fail-safe

A leitura vai para `SAFE` quando temperatura é nula, não finita, qualidade não é `good`, timestamp é inválido ou a amostra excede cinco segundos. Ao receber uma leitura válida de recuperação, o controlador passa a `OFF`, não diretamente a `ON`; essa escolha conservadora evita acionamento sem nova avaliação acima do limite. Em hardware real, o estado seguro teria de ser definido pelo risco físico do processo.

## Observabilidade e NISTIR 8259A

Cada decisão gera JSON com sensor, estado anterior, estado novo, motivo e timestamp. O projeto é alinhado conceitualmente ao NISTIR 8259A: identificação do dispositivo, configuração, proteção de dados, controle de acesso, atualização e conscientização do estado de segurança são requisitos para uma implantação IoT; este laboratório implementa apenas identidade lógica, validação, política e logs. Não afirmo MQTT, TLS, firmware ou hardware.

## Resultado observado e limites

A fixture percorre 24→31→29→27→inválido. A suíte em `results/pytest-run.log` verifica histerese, recuperação, sensor atrasado, NaN e configuração inválida. O arquivo de decisões registra a transição. A solução não mede temperatura real, não garante segurança física, não persiste telemetria, não autentica dispositivos e não prova desempenho de uma rede IoT.
