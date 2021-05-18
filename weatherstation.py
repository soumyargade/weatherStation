import bme280
import smbus2
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from time import sleep
    
def main():
    #code to set up BME280 Temp/Humidity Sensor
    BMEport = 1
    address = 0x77 
    bus = smbus2.SMBus(BMEport)
    bme280.load_calibration_params(bus,address)
    #code to set up MQTT client connection
    client = mqtt.Client()
    host = "98.121.22.98"
    port = 1883
    client.will_set("Status/WeatherStation", "offline", retain=True)
    client.connect(host, port, 5)
    client.subscribe("Status/WeatherStation")
    client.subscribe("Temperature/F")
    client.subscribe("Temperature/C")
    client.subscribe("Humidity")
    client.publish("Status/WeatherStation", "online", retain=True)
    lastTemp = 0
    lastHumidity = 0
    
    while True:
        bme280_Data = bme280.sample(bus,address)
        humidity  = round(bme280_Data.humidity,2) #percentage/100
        #pressure  = bme280_data.pressure
        cTemperature = round(bme280_Data.temperature, 2)#celcius
        fTemperature = round((cTemperature * 9/5) + 32 ,2) #fahrenhiet
        if abs(lastTemp - fTemperature) > .2 :
            client.publish("Temperature/F", fTemperature, retain=True)
            client.publish("Temperature/C", cTemperature, retain=True)
            print("temp sent: " + str(fTemperature))
            lastTemp = fTemperature
        if abs(lastHumidity - humidity) > .2 :
            client.publish("Humidity", humidity, retain=True)
            print("humidity sent: " + str(humidity))
            lastHumidity = humidity
        sleep(2)
        #keep connection alive
        client.publish("Status/WeatherStation", "online")
    
#Handles keyboard interrupt
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("")
        print("Weather Station Closing.")
