#!/usr/bin/env python
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






#
# Main display using curses
#
global airwheelint

airwheelint = 0
url = 'https://HA_URL.org:8123/api/services/light/turn_on'
headers = {
    'Authorization': 'Bearer TOKEN',
    'content-type': 'application/json',
}
previousValue = 0
while True:
    print(airwheelint)
    print(previousValue)
    if (airwheelint+10 >= previousValue) or (airwheelint-10 <= previousValue):
        response = post(url, headers=headers, data = '{"entity_id":"light.ENTITY_NAME","brightness_pct":'+str(airwheelint)+'}')
        print(response.text)
        previousValue = airwheelint

    time.sleep(0.1)