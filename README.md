# Weather Station
CSC 453 Final Project
### Broker Instructions
* Computer #1 runs Mosquitto locally and acts as the MQTT broker server. It handles all messages from the clients and then routes the messages to the appropriate destination clients.
### Compile Instructions
* Pago MQTT, BME280, SMBUS2
* Before running, update the information on lines 16 and 17 of weatherstation.py to reflect the address of your MQTT broker (host and port).
* To run, use the following command: **python weatherstation.py**.
* Compiled and tested on Raspberry Pi, Python 2.7.
