from scipy.fftpack import fft, ifft
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math
from ClassificationNetwork import ClassificationNetwork


def load_data(network):
    _, data_a1 = read('sounds/a/a (1).wav')
    _, data_a2 = read('sounds/a/a (2).wav')
    _, data_a3 = read('sounds/a/a (3).wav')

    _, data_e1 = read('sounds/e/e (1).wav')
    _, data_e2 = read('sounds/e/e (2).wav')
    _, data_e3 = read('sounds/e/e (3).wav')

    _, data_i1 = read('sounds/i/i (1).wav')
    _, data_i2 = read('sounds/i/i (2).wav')
    _, data_i3 = read('sounds/i/i (3).wav')

    sounds_map = {
        'a1': network.transform_data(data_a1),
        'a2': network.transform_data(data_a2),
        'a3': network.transform_data(data_a3),
        'e1': network.transform_data(data_e1),
        'e2': network.transform_data(data_e2),
        'e3': network.transform_data(data_e3),
        'i1': network.transform_data(data_i1),
        'i2': network.transform_data(data_i2),
        'i3': network.transform_data(data_i3)
    }

    _, data_undefined_a = read('sounds/undefined/undefined a.wav')
    _, data_undefined_e1 = read('sounds/undefined/undefined e (1).wav')
    _, data_undefined_e2 = read('sounds/undefined/undefined e (2).wav')
    _, data_undefined_i1 = read('sounds/undefined/undefined i (1).wav')
    _, data_undefined_i2 = read('sounds/undefined/undefined i (2).wav')
    _, data_undefined_i3 = read('sounds/undefined/undefined i (3).wav')
    _, data_undefined_g = read('sounds/undefined/undefined g.wav')

    undefined_sounds_map = {
        'undefined_a': network.transform_data(data_undefined_a),
        'undefined_e1': network.transform_data(data_undefined_e1),
        'undefined_e2': network.transform_data(data_undefined_e2),
        'undefined_i1': network.transform_data(data_undefined_i1),
        'undefined_i2': network.transform_data(data_undefined_i2),
        'undefined_i3': network.transform_data(data_undefined_i3),
        'undefined_g': network.transform_data(data_undefined_g)
    }

    return sounds_map, undefined_sounds_map


def draw_transformed_data(sounds_map, network):
    fig, ax = plt.subplots(3, 3)
    fig.suptitle('Трансформированные данные', fontsize=16)
    k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            ax[i][j].plot(list(sounds_map.values())[k])
            ax[i][j].set_title(list(sounds_map.keys())[k])
            k += 1
    plt.show()


def draw_average_signs(*args):
    fig, ax = plt.subplots()
    fig.suptitle('Паттерны букв', fontsize=16)
    for avg_value in args:
        ax.plot(avg_value)
    ax.legend(("Паттерн A", "Паттерн E", "Паттерн I"))
    plt.show()


def main():
    network = ClassificationNetwork()
    sounds_map, undefined_sounds_map = load_data(network)
    network.teach(sounds_map)

    draw_transformed_data(sounds_map, network)
    draw_average_signs(network.avg_a, network.avg_e, network.avg_i)

    print('Использованные в обучении нейросети буквы:')
    for name, data in sounds_map.items():
        network.determine(name, data)
    print('\nНеиспользованные в обучении нейросети буквы и неподходящая под шаблон буква:')
    for name, data in undefined_sounds_map.items():
        network.determine(name, data)


if __name__ == "__main__":
    main()
