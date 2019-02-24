#!/usr/bin/env python

from time import sleep
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import flicklib
import time

some_value = 5000

@flicklib.move()
def move(x, y, z):
    global value
    value = round(x,1)*100

client = mqtt.Client("hass-client")
client.username_pw_set('MQTT_USER', 'MQTT_PW')
client.connect('MQTT_IP', 1883)
client.loop_start()
#
# Main display using curses
#
global value

value = 0
previousValue = 0
while True:
    #print(value)
    #print(previousValue)
    if (value+10 <= previousValue) or (value-10 >= previousValue):
        client.publish("flick/brightness", value, retain=False)
        previousValue = value

    time.sleep(0.2)