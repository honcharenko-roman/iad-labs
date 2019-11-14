import math
import asyncio

import matplotlib.pyplot as plt
import numpy as np

SIGMA = 0.1


class ClassificationNetwork:

    def __init__(self, training_inputs):
        self.weights = training_inputs

    def __teach__(self, training_inputs):
        for class_ in training_inputs:
            for point in class_:
                self.weights = np.append(self.weights, point)
        self.weights = np.reshape(self.weights, (20, 2))
        return self.weights

    def classify(self, classified_point):
        result = self.__template_layer__(classified_point)
        return self.__output_layer__(result) + 1

    def __template_layer__(self, classified_point):
        distances = []
        result = []
        for class_ in self.weights:
            for point in class_:
                distances.append(self.__activation_function__(
                    point, classified_point))
            result.append(sum(distances))
            distances.clear()
        return result

    def __activation_function__(self, point_1, point_2):
        w_x1 = (point_1[0] - point_2[0])**2
        w_x2 = (point_1[1] - point_2[1])**2
        return math.exp(-((w_x1 + w_x2) / SIGMA**2))

    def __output_layer__(self, result):
        min_elem = max(result)
        return result.index(min_elem)
