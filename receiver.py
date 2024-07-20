import paho.mqtt.client as mqtt

broker_address = "127.0.0.1" #localhost
broker_port = 1883
topic = "scada" #topic to subscribe too

client = mqtt.Client()
client.connect(broker_address, broker_port)
client.subscribe(topic)

client.loop_forever()
