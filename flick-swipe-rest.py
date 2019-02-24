#!/usr/bin/env python

from time import sleep
import flicklib
from requests import post
import subprocess
import time


@flicklib.flick()
def flick(start,finish):
    global flicktxt
    flicktxt = start + ' - ' + finish
    print(flicktxt)

@flicklib.double_tap()
def doubletap(position):
    global doubletaptxt
    doubletaptxt = position

#
# Main display using curses
#
global flicktxt
global doubletaptxt

url = 'https://URL:8123/api/services/light/turn_on'
volume_up_url = 'https://URL:8123/api/services/media_player/volume_up'
volume_down_url = 'https://URL:8123/api/services/media_player/volume_down'
headers = {
    'Authorization': 'Bearer TOKEN',
    'content-type': 'application/json',
}

flicktxt = ""
doubletaptxt = ""
while True:

    if (doubletaptxt == "center"):
        print("shutting down")
        subprocess.call("sudo shutdown now", shell=True)

    if (flicktxt == "west - east"):
        print("w-e publish")
        response = post(url, headers=headers, data = '{"entity_id":"light.ENTITY_NAME","brightness_pct":100}')
        flicktxt = ""
	    sleep(0.2)
    if (flicktxt == "east - west"):
	print("e-w publish")
        response = post(url, headers=headers, data = '{"entity_id":"light.ENTITY_NAME","brightness_pct":0}')
        flicktxt = ""
	    sleep(0.2)
    if (flicktxt == "north - south"):
        print("n-s publish")
        response = post(volume_down_url, headers=headers, data = '{"entity_id":"media_player.ENTITY_NAME"}')
        flicktxt = ""
	    sleep(0.2)
    if (flicktxt == "south - north"):
        print("s-n publish")
        response = post(volume_up_url, headers=headers, data = '{"entity_id":"media_player.ENTITY_NAME"}')
        print(response.text)
	    flicktxt = ""
	    sleep(0.2)

    time.sleep(0.1)