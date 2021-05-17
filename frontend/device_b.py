import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json

global status
global station_temp_f
global station_temp_c
global station_humidity
global station_feeling

# Occurs when connection to the broker is established
def on_connect(client, userdata, flags, rc):
    global status
    global station_temp_f
    global station_temp_c
    global station_humidity
    global station_feeling
    client.subscribe("Status/WeatherStation")
    client.subscribe("Temperature/F")
    client.subscribe("Temperature/C")
    client.subscribe("Humidity")
    status = ""
    station_temp_f = 0.0
    station_temp_c = 0.0
    station_humidity = 0.0
    station_feeling = ""

# Occurs when message is posted to any subscribed topic
def on_message(client, userdata, msg):
    global status
    global station_temp_f
    global station_temp_c
    global station_humidity
    global station_feeling
    data = {}
    data = []
    topic = msg.topic#.encode("ascii")
    message = str(msg.payload)#.encode("ascii")
    
    if topic == "Status/WeatherStation":
        if message == "online" or message == "b'online'":
            print("online")
            status = "Online"
        if message == "offline" or message == "b'offline'":
            print("offline")
            status = "Offline"
            
    if topic == "Temperature/F":
        print("RECEIVED: " + msg.topic + " " + str(float(msg.payload)))
        station_temp_f = float(msg.payload)
        
    if topic == "Temperature/C":
        print("RECEIVED: " + msg.topic + " " + str(float(msg.payload)))
        station_temp_c = float(msg.payload)
    
    if topic == "Humidity":
        print("RECEIVED: " + msg.topic + " " + str(float(msg.payload)))
        station_humidity = float(msg.payload)

    if station_temp_f > 80.0:
        station_feeling = "warm"    
    if station_temp_f <= 80.0:
        station_feeling = "comfortable"
    if station_temp_f > 75.0 and station_humidity >= 55.0:
        station_feeling = "muggy"
    if station_temp_f <= 60.0:
        station_feeling = "chilly"
    if station_temp_f <= 45.0:
        station_feeling = "cold"

    data.append({
        'status' : status,
        'station_temp_f' : station_temp_f,
        'station_temp_c' : station_temp_c, 
        'station_humidity' : station_humidity,
        'station_feeling' : station_feeling
    })
    
    data2 = {
        "status": status,
        "station_temp_f":station_temp_f,
        "station_temp_c":station_temp_c,
        "station_humidity":station_humidity,
        "station_feeling":station_feeling
    } 

    with open('data.json', 'w') as outfile:
        json.dump(data2, outfile)

def main():
    # Code to set up MQTT client connection
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    host = "98.121.22.98"
    port = 1883
    client.connect(host, port, 5)
    client.loop_forever()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("")
