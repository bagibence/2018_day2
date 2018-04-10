from maxima import find_maxima
import numpy as np


def test_find_maxima(input, output):
    'Test the find_maxima function in the maxima module'
    try:
        return find_maxima(input) == output
    except:
        print('Error for', input)


if __name__ == '__main__':
    inputs = list()
    inputs.append([0, 1, 2, 1, 2, 1, 0])
    inputs.append([-i**2 for i in range(-3, 4)])
    inputs.append([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)])
    inputs.append([4, 2, 1, 3, 1, 2])
    inputs.append([4, 2, 1, 3, 1, 5])
    inputs.append([4, 2, 1, 3, 1])

    outputs = list()
    outputs.append([2, 4])
    outputs.append([3])
    outputs.append([16, 78])
    outputs.append([0, 3, 5])
    outputs.append([0, 3, 5])
    outputs.append([0, 3])

    for input, output in zip(inputs, outputs):
        print(test_find_maxima(input, output))
