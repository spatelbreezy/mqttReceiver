import paho.mqtt.client as mqtt

broker_address = "127.0.0.1" #localhost
broker_port = 1883
topic = "scada" #topic to subscribe too

def on_message(client, userdata, message):
    print(f"Received a message: {message.payload.decode('utf-8')} on topic {message.topic}")

client = mqtt.Client() #Initialize client

client.on_message = on_message #Define function to be called when receiving message

client.connect(broker_address, broker_port) #Connect to the broker

client.subscribe(topic) #Subscribe to the predefined topic

client.loop_forever() #Receive messages

