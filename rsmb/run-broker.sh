BROKER_PATH="${0/run-broker.sh/broker//bin}"
cd "$BROKER_PATH"
./broker

import time, serial

ser = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2)
time.sleep(3)
for i in range(1,10):
    ser.write("ON")
    time.sleep(1)
    ser.write("OFF")
    time.sleep(1)