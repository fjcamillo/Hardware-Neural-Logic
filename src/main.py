import serial
import json

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1 )

with open('./data.json', 'r') as f:
    data = json.load(f)

def getweights(data, logic):
    return data[logic]['features'], data[logic]['labels'], data[logic]['weights']


inp = input("""
Logic Type:
1. AND
2. OR
3. NOT
"""
)

print(f"Chosen Logic Type {inp}")

feature = input("""
Input Type:
1. [0, 0]
2. [0, 1]
3. [1, 0]
4. [1, 1]
""")
