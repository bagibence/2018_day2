from maxima import find_maxima
import numpy as np


def test_find_maxima(input, output):
    'Test the find_maxima function in the maxima module'
    try:
        return find_maxima(input) == output
    except:
        print('Error for', input)


if __name__ == '__main__':
    x1 = [0, 1, 2, 1, 2, 1, 0]
    x2 = [-i**2 for i in range(-3, 4)]
    x3 = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    x4 = [4, 2, 1, 3, 1, 2]
    x5 = [4, 2, 1, 3, 1, 5]
    x6 = [4, 2, 1, 3, 1]

    y1 = [2, 4]
    y2 = [3]
    y3 = [16, 78]
    y4 = [0, 3, 5]
    y5 = [0, 3, 5]
    y6 = [0, 3]

    print(test_find_maxima(x1, y1))
    print(test_find_maxima(x2, y2))
    print(test_find_maxima(x3, y3))
    print(test_find_maxima(x4, y4))
    print(test_find_maxima(x5, y5))
    print(test_find_maxima(x6, y6))
