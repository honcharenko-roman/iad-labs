import math

import matplotlib.pyplot as plt
import numpy as np

SIGMA = 0.1

fig = plt.figure()
ax = fig.add_subplot(111)
legend_map = {
    1: 'or',
    2: 'ob',
    3: 'og',
    4: 'om',
}


class ClassificationNetwork:

    def __init__(self, training_inputs):
        self.weights = training_inputs

    def classificate(self, classified_point):
        distances = []
        result = [-math.inf]
        for class_ in self.weights:
            for point in class_:
                w_x1 = (point[0] - classified_point[0])**2
                w_x2 = (point[1] - classified_point[1])**2
                distances.append(math.exp(-((w_x1 + w_x2) / SIGMA**2)))
            result.append(sum(distances))
            distances.clear()
        self.__output_layer__(result, classified_point)

    def __output_layer__(self, result, classified_point):
        min_elem = max(result)
        print(result.index(min_elem))
        self.plot(classified_point)

    def plot(self, point):
        k = 1
        p = []
        for class_array in self.weights:
            for j in enumerate(class_array):
                p1, = plt.plot(class_array[:, 0],
                               class_array[:, 1], legend_map[k])
            p.append(p1)
            k += 1
        p1, = plt.plot(point[0], point[1], '+r')
        ax.legend(p, ["class1", "class2", "class3", "class4"])
        ax.grid(True)
        plt.show()
