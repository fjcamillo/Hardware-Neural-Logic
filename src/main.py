import numpy as np
from functools import reduce
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

def perceptron(weight, bias, x):
    model = np.add(np.dot(x, weight), bias)
    print('model: {}'.format(model))
    logit = 1/(1+np.exp(-model))
    print('Type: {}'.format(logit))
    return np.round(logit)

def compute(logictype, weightdict, dataset):
    weights = np.array([ weightdict[logictype][w] for w in weightdict[logictype].keys()[::-1]])
    # output = np.array([ perceptron(weights, weightdict['bias'][logictype], val) for val in dataset])
    output = np.array([perceptron(weights, weightdict['bias'][logictype], dataset)])
    print(logictype)
    print(int(output[0]))
    return logictype, int(output[0])

def main():
    logic = {
        'logic_and' : {
            'w0': -0.1,
            'w1': 0.2,
            'w2': 0.2
        },
        'logic_or': {
            'w0': -0.1,
            'w1': 0.7,
            'w2': 0.7
        },
        'logic_not': {
            'w0': 0.5,
            'w1': -0.7
        },
        'logic_nand': {
            'w0': 0.6,
            'w1': -0.8,
            'w2': -0.8
        },
        'logic_nor': {
            'w0': 0.5,
            'w1': -0.7,
            'w2': -0.7
        },
        'logic_xor': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        },
        'logic_xnor': {
            'w0': -5,
            'w1': 20,
            'w2': 10
        },
        'bias': {
            'logic_and': -0.2,
            'logic_or': -0.1,
            'logic_not': 0.1,
            'logic_xor': 1,
            'logic_xnor': 1,
            'logic_nand': 0.3,
            'logic_nor': 0.1
        }
    }
    dataset = np.array([
        [1,0,0],
        [1,0,1],
        [1,1,0],
        [1,1,1]
    ])

    logic_type = input("""
    Logic Type:
    1. AND
    2. OR
    3. NOT
    """)

    data = input("""
    Data:
    1. [0, 0]
    2. [0, 1]
    3. [1, 0]
    4. [1, 1]
    """)


    compute_type = ['logic_and', 'logic_or', 'logic_not']

    chosen_type, output = compute(compute_type[int(logic_type)-1], logic, dataset[int(data)-1])
    arduino.write(output)


if __name__ == '__main__':
    while True:
        main()
