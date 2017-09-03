import serial
import json

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1 )

with open('./data.json', 'r') as f:
    data = json.load(f)

while true:
    arduino.write('1')
