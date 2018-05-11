from paho.mqtt.client import Client
import paho

def on_connect(client, userdata, flags, rc):
    client.subscribe('a')

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

client = Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('nuvem.sj.ifsc.edu.br', 1883, 60)
client.loop_forever()
