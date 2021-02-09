from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("Switch-control")

def on_message(client, userdata, msg):
    if msg.payload.decode() == "0on":
        cp.pixels[0] = (255, 255, 255)
    elif msg.payload.decode() == "1on":
        cp.pixels[1] = (255, 255, 255)
    elif msg.payload.decode() == "2on":
        cp.pixels[2] = (255, 255, 255)
    elif msg.payload.decode() == "0off":
        cp.pixels[0] = (0, 0, 0)
    elif msg.payload.decode() == "1off":
        cp.pixels[1] = (0, 0, 0)
    elif msg.payload.decode() == "2off":
        cp.pixels[2] = (0, 0, 0)

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt