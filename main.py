import random
import numpy as np
import matplotlib.pyplot as plt

from math import sqrt

import classnition
import ClassificationNetwork


def init_arrays():
    class1 = np.array([[0.05, 0.91],
                       [0.14, 0.96],
                       [0.16, 0.9],
                       [0.07, 0.7],
                       [0.2, 0.63]])

    class2 = np.array([[0.49, 0.89],
                       [0.34, 0.81],
                       [0.36, 0.67],
                       [0.47, 0.49],
                       [0.52, 0.53]])

    class3 = np.array([[0.62, 0.83],
                       [0.79, 0.92],
                       [0.71, 0.92],
                       [0.78, 0.83],
                       [0.87, 0.92]])

    class4 = np.array([[0.55, 0.4],
                       [0.66, 0.32],
                       [0.74, 0.49],
                       [0.89, 0.3],
                       [0.77, 0.2]])


    classes = np.array([class1,
                        class2,
                        class3,
                        class4
                        ])

    return classes


def generate_random_point():
    start_p = np.array([random.uniform(0, 1), random.uniform(0, 1)])
    return start_p


def main():
    classes = init_arrays()
    network = ClassificationNetwork.ClassificationNetwork(classes)
    point = generate_random_point()
    network.classificate(generate_random_point())



if __name__ == "__main__":
    main()