import numpy as np
from numpy import exp, array, dot
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

import lineardep

TRAINING_COEFFICIENT = 0.01


def main():
    training_set_inputs = np.array(
        [[1], [2], [3], [4], [5], [6], [7], [8], [9]])
    training_set_outputs = np.array(
        [[3.6], [4.4], [5.8], [6.2], [7.4], [8], [9.2], [10.4], [11.8]])

    m, c, e = lineardep.least_squares(
        training_set_inputs, training_set_outputs)

    average_approximation_error_least_square = lineardep.average_approximation_error(training_set_outputs, np.array(
        [m * input_value + c for input_value in training_set_inputs]))
    print("Least squares method: \nm - {0}, c - {1}, error - {2}, average approximation error - {3}".format(
        m, c, e, average_approximation_error_least_square))

    m, c, e = lineardep.neural_network(training_set_inputs,
                                       training_set_outputs, TRAINING_COEFFICIENT)

    average_approximation_error_neural_network = lineardep.average_approximation_error(training_set_outputs, np.array(
        [m * input_value + c for input_value in training_set_inputs]))
    print(
        "Neural network method: \nm - {0}, c - {1}, error - {2} average approximation error - {3}".format(
            m, c, e, average_approximation_error_neural_network))

    build_plot(training_set_inputs, training_set_outputs)

    plt.show()


def build_plot(training_set_inputs, training_set_outputs):

    m, c, _ = lineardep.least_squares(
        training_set_inputs, training_set_outputs)
    p1, = plt.plot(training_set_inputs, m * training_set_inputs + c)
    m, c, _ = lineardep.neural_network(training_set_inputs,
                                       training_set_outputs, TRAINING_COEFFICIENT)
    p2, = plt.plot(training_set_inputs, m * training_set_inputs + c)

    plt.plot(training_set_inputs, training_set_outputs, 'og')

    plt.legend([p1, p2], ['Least squares', 'Neural network'])


if __name__ == "__main__":
    main()
