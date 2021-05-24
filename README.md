# Weather Station
CSC 453 Final Project
### Objectives
* Create a system which can provide temperature and humidity statistics.
* Use the weather station's statistics to compare against local weather.
* Provide a meaningful message about the state of the weather.
* Convey the weather station and the local weather using an attractive webpage.
### System Design
* Connected a temperature and humidity sensor to a Raspberry Pi (Device A) to collect the temperature and humidity data. Device A collects the sensor information, and then connects to the broker to publish updates of temperature and humidity values.
* The MQTT broker oversees transmission of data from Device A (which collects sensor data) and Device B (which analyzes sensor data). When the broker is online, Device B subscribes to the temperature and humidity topics to analyze the data.
* Device B analyzes the data to provide weather descriptions based off temperature and humidity thresholds. It then sends over all of this information to the front-end app which displays it to the user. The front-end app also gets the local weather station information based on the zip code entered by the user.
<p float="left">
  <img src="https://github.com/soumyargade/weatherStation/blob/main/images/systemdesign.png" width="390">
  <img src="https://github.com/soumyargade/weatherStation/blob/main/images/sensordiagram.png" width="280">
</p>

### Broker ReadMe
* Computer #1 runs Mosquitto locally and acts as the MQTT broker server. It handles all messages from the clients and then routes the messages to the appropriate destination clients.
* **Prerequisites & Dependencies**: Mosquitto from their website. Update config file for broker to CSC 453 requirements, and store in \mosquitto folder. Port forward port 1883 on broker's router to host that broker is run on. Disable any firewalls for stuff coming from port 1883.
* **To Run**: On cmd, navigate to folder where mosquitto was installed ('cd c:\Program Files\mosquitto'). Run 'mosquitto -v -c csc453.conf'. Broker is now running: use ctrl-C to kill.
### WeatherStation.py ReadMe
* Paho MQTT, BME280, SMBUS2
* Before running, update the information on lines 16 and 17 of weatherstation.py to reflect the address of your MQTT broker (host and port).
* To run, use the following command: **python weatherstation.py**.
* Compiled and tested on Raspberry Pi, Python 2.7.
### Device B Implementation
* If the temperature is above 80 degrees, it is warm.
* If the temperature is between 60 and 80 degrees, it is comfortable.
* If the temperature is between 45 and 60 degrees, it is chilly.
* If the temperature is below 45 degrees, it is cold.
* If the temperature is above 75 degrees and the humidity is above 55%, it is muggy.
<img src="https://github.com/soumyargade/weatherStation/blob/main/images/webpage.png" width="500">
