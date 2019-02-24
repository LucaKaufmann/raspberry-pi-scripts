#!/usr/bin/env python

from time import sleep
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import flicklib
from requests import post
import time

some_value = 500

@flicklib.airwheel()
def spinny(delta):
    global some_value
    global airwheelint
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 1000:
        some_value = 1000
    airwheelint = int(some_value/10)

client = mqtt.Client("hass-client")
client.username_pw_set('MQTT_USER', 'MQTT_PW')
client.connect('MQTT_IP', 1883)
client.loop_start()
#
# Main display using curses
#
global airwheelint

airwheelint = 0
previousValue = 0
while True:

   # print(airwheelint+10 <= previousValue)
   # print(airwheelint-10 >= previousValue)
    if (airwheelint+10 <= previousValue or airwheelint-10 >= previousValue):
        client.publish("flick/brightness", airwheelint, retain=False)
        previousValue = airwheelint
        print(airwheelint)
    if (airwheelint == 0 and previousValue != 0) or (airwheelint == 100 and previousValue != 100):
        client.publish("flick/brightness", airwheelint, retain=False)
        previousValue = airwheelint
        print(airwheelint)

    time.sleep(0.5)