# raspberry-pi-scripts
Some scripts to control various things using the Flick raspberry pi HAT (Gesture sensing).

# flick-airwheel-mqtt
Takes airwheel values from the Flick library and sends them to an MQTT topic. Values range from 0-100, ideal to control things like light brightness or volume of another device.

# flick-move-mqtt
Reads the position and sends them to MQTT. Values from 0-100.

# flick-swipe-rest
All-in-one script implementing different gestures (flick and double tap). Triggers REST API calls for gestures, in my example I used them to call the Home Assistant API, turn a light on/off and turn the volume of a media player up and down. Double tap will shut down the raspberry pi.

# flick-airwheel-rest
Trigger REST Api calls to set brightness of a light based on airwheel values.

# flick-move-volume
Set the volume of a media player via REST api calls.

# jukebox
Jukebox script, read values on RFID cards and send them to an MQTT topic. From there, trigger playlists based on that (I used Node-red).