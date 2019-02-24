#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
from time import sleep
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

reader = SimpleMFRC522.SimpleMFRC522()
client = mqtt.Client("CLIENT_NAME")
client.username_pw_set('MQTT_USER', 'MQTT_PW')
client.connect('MQTT_IP', 1883)
client.loop_start()

try:
        while True:
            id, text = reader.read()
            print(id)
            print(text)
            client.publish("jukebox/play", text, retain=False)
            print("Published message")
            sleep(5)
finally:
        GPIO.cleanup()