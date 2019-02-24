#!/usr/bin/env python
import flicklib
from requests import post
import time

some_value = 5000

@flicklib.airwheel()
def spinny(delta):
    global some_value
    global airwheelint
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 10000:
        some_value = 10000
    airwheelint = float(some_value/10000)


@flicklib.move()
def move(x, y, z):
    global volume
    volume = round(x/2,2)



#
# Main display using curses
#
global volume

volume = 0
url = 'https://HA_URL:8123/api/services/media_player/volume_set'
headers = {
    'Authorization': 'Bearer TOKEN',
    'content-type': 'application/json',
}
previousValue = 0
while True:
    print(volume)
    print(previousValue)
    if (volume+0.1 >= previousValue) or (volume-0.1 <= previousValue):
        response = post(url, headers=headers, data = '{"entity_id":"media_player.ENTITY_ID","volume_level":'+str(volume)+'}')
        print(response.text)
        previousValue = volume

    time.sleep(0.2)