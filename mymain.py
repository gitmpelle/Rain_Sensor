

import esp32
#####################################################################################
from pichromecast import play_url, create_url
import time
import sys
import ubinascii
from umqtt.simple import MQTTClient
import machine
import random
import ntptime
rtc = machine.RTC()
import gc
gc.collect()
from machine import I2C , Pin, deepsleep
from time import sleep
from ADS1115 import *
import esp
esp.osdebug(None)
import json
wake1 = Pin(4, mode = Pin.IN,  pull=Pin.PULL_HOLD|Pin.PULL_UP)

# Publish MQTT messages after every set timeout
last_publish = time.time()
publish_interval = 60

# Default  MQTT_BROKER to connect to
CONFIG = {
     # Configuration details of the MQTT broker
     #https://www.srccodes.com/mqtt-cloudmqtt-mqtt-dashboard-android-esp8266-mycropython-home-automation-blub-internet-of-things-iot-m2m/
     "MQTT_BROKER": "m15.cloudmqtt.com",
     "USER": "quoaqddx",
     "PASSWORD": "zaXkKvgMe7Hx",
     "PORT": 12638,
     "PUBLISH_TOPIC": b"Rain_SensorMsg",
     "SUBSCRIBE_TOPIC": b"Rain_Sensor",
     
     # unique identifier of the chip
     "CLIENT_ID": b"esp32_" + ubinascii.hexlify(machine.unique_id())
      }

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    global last_publish
    print(f"{getTime()} {topic.decode()} {msg.decode()}")

def getTime():
        timestamp=rtc.datetime()
        timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] +  timestamp[4:7])
        return f'{timestring[0:20]}'
########################################################################################################
print(f"Begin connection with MQTT Broker :: {CONFIG['MQTT_BROKER']}")
mqttClient = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'], keepalive=0)
mqttClient.set_callback(sub_cb)
mqttClient.connect()
mqttClient.subscribe(CONFIG['SUBSCRIBE_TOPIC'])
print(f"Connected to MQTT  Broker :: {CONFIG['MQTT_BROKER']}, and waiting for callback function to be called!")
mqttClient.publish(CONFIG['PUBLISH_TOPIC'], str('1').encode())
gc.collect()




#########################################################################################################
#level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
#esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)
#your main code goes here to perform a task

print('Im awake. Going to sleep in 10 seconds')
sleep(10)

print('Going to sleep now')
deepsleep()

