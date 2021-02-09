from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("Switch-control")

def on_message(client, userdata, msg):
    i = 0
    while(i<10):
        if(i==9):
            i=0
        if msg.payload.decode() == "0on":
            cp.pixels[i] = (255, 255, 255)
        elif msg.payload.decode() == "0off":
            cp.pixels[i] = (0, 0, 0)
        i+=1
cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt