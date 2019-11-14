import random
import numpy as np
import matplotlib.pyplot as plt

from math import sqrt

import classnition
import ClassificationNetwork


DENSITY = 0.02

fig = plt.figure()
ax = fig.add_subplot(111)
legend_map = {
    1: 'or',
    2: 'ob',
    3: 'og',
    4: 'om',
}


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

network = ClassificationNetwork.ClassificationNetwork(init_arrays())


def generate_random_point():
    start_p = np.array([random.uniform(0, 1), random.uniform(0, 1)])
    return start_p


def main():
    classes = init_arrays()
    fig.canvas.mpl_connect('button_press_event', onclick)
    plot(classes)
    point = generate_random_point()
    affiliation = network.classify(point)
    update_plot(point, affiliation)
    ax.set_title('The point ' + str(point) +
                 ' belongs to ' + str(affiliation) + ' class')
    plt.show()


def color_map(network):
    for x in np.arange(0, 1, DENSITY):
        for y in np.arange(0, 1, DENSITY):
            affiliation = network.classify(np.array([x, y]))
            update_plot(np.array([x, y]), affiliation)
    fig.canvas.draw()
    plt.show()


def update_plot(point, affiliation):
    plt.plot(point[0], point[1], legend_map[affiliation], markersize=12)


def plot(classes):
    fig.canvas.mpl_connect('button_press_event', onclick)
    k = 1
    p = []
    for class_array in classes:
        for j in enumerate(class_array):
            p1, = plt.plot(class_array[:, 0],
                           class_array[:, 1], legend_map[k])
        p.append(p1)
        k += 1
    ax.legend(p, ["class1", "class2", "class3", "class4"])
    ax.grid(True)


def onclick(event):
    affiliation = network.classify(np.array([event.xdata, event.ydata]))
    plt.plot(event.xdata, event.ydata,
            legend_map[affiliation])
    ax.set_title('The point ' + str(np.array([event.xdata, event.ydata])) +
                 ' belongs to ' + str(affiliation) + ' class')
    plt.show()


if __name__ == "__main__":
    main()
