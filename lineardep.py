import random


def least_squares(training_set_inputs, training_set_outputs):
    n = len(training_set_inputs)
    sum_of_inputs_multiple_outputs = sum(
        training_set_inputs * training_set_outputs)
    sum_of_squared_inputs = sum(training_set_inputs ** 2)
    sum_of_inputs_squared = sum(training_set_inputs) ** 2

    m = (n * sum_of_inputs_multiple_outputs - sum(training_set_inputs) *
         sum(training_set_outputs)) / (n * sum_of_squared_inputs - sum_of_inputs_squared)

    c = (sum(training_set_outputs) - (m * sum(training_set_inputs))) / n

    error_array = []
    for x, y in zip(training_set_inputs, training_set_outputs):
        error_array.append((y - (m * x + c)) ** 2)
    return m, c, sum(error_array)


def neural_network(training_set_inputs, training_set_outputs, training_coefficient):
    m = random.random()
    c = random.random()
    error_array = []
    for _ in range(10000):
        error_array.clear()
        for input_value, output_value in zip(training_set_inputs, training_set_outputs):
            error = output_value - (input_value * m + c)
            error_array.append(error)
            m += training_coefficient * error * output_value
            c += training_coefficient * error
        if sum(error_array) < 0.01:
            return m, c, sum(error_array)


def average_approximation_error(training_set_outputs, resulting_set_outputs):
    errors_array = []
    for training_value, resulting_value in zip(training_set_outputs, resulting_set_outputs):
        errors_array.append((abs(training_value - resulting_value)) / training_value)
    return (sum(errors_array) / len(training_set_outputs))
