
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
wake1 = Pin(14, mode = Pin.IN)

#level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)

#your main code goes here to perform a task

print('Im awake. Going to sleep in 10 seconds')
sleep(10)
print('Going to sleep now')
deepsleep()
