# Weather Station
CSC 453 Final Project
### Broker Instructions
* Computer #1 runs Mosquitto locally and acts as the MQTT broker server. It handles all messages from the clients and then routes the messages to the appropriate destination clients.
* **Prerequisites & Dependencies**: Mosquitto from their website. Update config file for broker to CSC 453 requirements, and store in \mosquitto folder. Port forward port 1883 on broker's router to host that broker is run on. Disable any firewalls for stuff coming from port 1883.
* **To Run**: On cmd, navigate to folder where mosquitto was installed ('cd c:\Program Files\mosquitto'). Run 'mosquitto -v -c csc453.conf'. Broker is now running: use ctrl-C to kill.
### Compile Instructions
* Paho MQTT, BME280, SMBUS2
* Before running, update the information on lines 16 and 17 of weatherstation.py to reflect the address of your MQTT broker (host and port).
* To run, use the following command: **python weatherstation.py**.
* Compiled and tested on Raspberry Pi, Python 2.7.
