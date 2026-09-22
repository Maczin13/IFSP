# Arquitetura do controlador

Sensor simulado → validação de qualidade/timestamp → máquina de estados com histerese → decisão do atuador → log JSON. O laboratório não contém GPIO, relé físico, broker MQTT ou armazenamento remoto; esses componentes são fronteiras de extensão, não evidências atuais.
