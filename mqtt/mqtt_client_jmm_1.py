# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:57:04 2016

@author: jmmauricio


sudo apt-get install mosquitto
sudo update-rc.d mosquitto defaults
sudo /etc/init.d/mosquitto start

"""

import paho.mqtt.client as mqtt
import time
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/jmm/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.193", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

t_0 = time.time()
while True:
    t = time.time()-t_0
    client.publish("jmm", '{:2.3f}'.format(t))
    time.sleep(0.01)
#