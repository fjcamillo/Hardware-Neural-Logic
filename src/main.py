import serial
import json

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1 )

with open('./data.json', 'r') as f:
    data = json.load(f)
print(data)
def getweights(data, logic):
    return data[logic]['features'], data[logic]['labels'], data[logic]['weights']

def linearmodel(feature, input_data, weights):
    model = weights[0][0] + feature[input_data][0]*weights[1][0] + feature[input_data][1]*weights[2][0]
    return model



while True:
    inp = input("""
    Logic Type:
    1. AND
    2. OR
    3. NOT
    """
    )
    inp_types = ['and', 'or', 'not']
    print(f"Chosen Logic Type {inp}")

    input_data = input("""
    Input Type:
    1. [0, 0]
    2. [0, 1]
    3. [1, 0]
    4. [1, 1]
    """)

    features, labels, weights = getweights(data, inp_types[int(inp)-1])
    output = linearmodel(features, int(input_data)-1, weights)

    arduino.write(output)
