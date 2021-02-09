from microbit import *
import paho.mqtt.client as mqtt

DIRECTIONS = {
    "N":Image.ARROW_N,
    "NE":Image.ARROW_NE,
    "E":Image.ARROW_E,
    "SE":Image.ARROW_SE,
    "S":Image.ARROW_S, 
    "SW":Image.ARROW_SW,
    "W":Image.ARROW_W,
    "NW":Image.ARROW_NW
    }
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        display.show(Image.YES)
        client.subscribe("my topic")


def on_message(client, userdata, msg):
    direction = msg.payload.decode()
    print("Direction from html:",direction)
    if(direction in list(DIRECTIONS.keys())):
        display.show(DIRECTIONS[direction])
    else:
        display.show(Image("00000:00000:00000:00000:00000"))

    
  

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()