import time, serial
import mosquitto
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")

client.subscribe("LED")

ser = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2)

def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)

    if msg.payload == "ON":

        #on
        ser.write("1")
        #wait for 2 seconds

        
    elif msg.payload == "OFF":
        
        #off
        ser.write("0")


client.on_message = messageReceived
    
while (client != None): client.loop()