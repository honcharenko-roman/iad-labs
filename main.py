import binascii
import time
import random

import matplotlib.pyplot as plt
import numpy as np

import network


# H = [ -1 1 -1 -1 1 -1 -1 -1 ]
# R = [ -1 1 -1 1 -1 -1 1 -1 ]
# I = [ -1 1 -1 -1 1 -1 -1 1 ]
# Y = [ -1 1 -1 1 1 -1 -1 1 ]

LETTERS = {
    'H': np.array([[-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, -1, -1, -1, -1, -1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1]
                   ]),

    'R': np.array([[-1, -1, -1, -1, -1, -1, 1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, -1, -1, -1, -1, -1, 1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1]
                   ]),

    'I': np.array([[1, 1, -1, -1, -1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, -1, -1, -1, 1, 1]
                   ]),

    'Y': np.array([[-1, 1, 1, 1, 1, 1, -1],
                   [-1, 1, 1, 1, 1, 1, -1],
                   [1, -1, 1, 1, 1, -1, 1],
                   [1, 1, -1, 1, -1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1],
                   [1, 1, 1, -1, 1, 1, 1]
                   ])
}

neuro_network = network.NeuralNetwork(LETTERS)
ASCII_LENGHT = 8
NOISE_PERCENT = 15

ASCII = {
    # 'H': np.c_[np.reshape(neuro_network.text_to_bits('H'), (1, ASCII_LENGHT)), z],
    'H': np.reshape(neuro_network.text_to_bits('H'), (1, ASCII_LENGHT)),
    'R': np.reshape(neuro_network.text_to_bits('R'), (1, ASCII_LENGHT)),
    'I': np.reshape(neuro_network.text_to_bits('I'), (1, ASCII_LENGHT)),
    'Y': np.reshape(neuro_network.text_to_bits('Y'), (1, ASCII_LENGHT))
}


def plot_letters(LETTERS):
    _, axarr = plt.subplots(1, len(list(LETTERS.values())))
    for index, value in enumerate(LETTERS):
        axarr[index].imshow(LETTERS[value])
    plt.show()


def noise_letters():
    plot_letters(LETTERS)

    noised_letters = {}
    for value in LETTERS:
        noised_letters[value] = neuro_network.make_noise(
            LETTERS[value], NOISE_PERCENT)
    plot_letters(noised_letters)

    corrected_letters = {}
    for value in LETTERS:
        corrected_letters[value] = neuro_network.correct(noised_letters[value])
    plot_letters(corrected_letters)


def noised_ascii():
    noised_ascii = {}
    for value in ASCII:
        noised_ascii[value] = neuro_network.make_noise(
            ASCII[value], NOISE_PERCENT)

    corrected_ascii = {}
    for value in ASCII:
        corrected_ascii[value] = neuro_network.correct_ascii(
            noised_ascii[value])
    plot_letters(corrected_ascii)


def plot_letter(letter):
    _, axarr = plt.subplots()
    axarr.imshow(neuro_network.ascii_to_letter(letter))
    plt.show()


def plot_matrix(matrix):
    _, axarr = plt.subplots()
    axarr.imshow(matrix)
    plt.show()


def main():
    neuro_network.teach()
    #noise_letters()
    #noised_ascii()

    # print('ideal letter to ascii', neuro_network.letter_to_ascii(
    #     LETTERS['R']).transpose())
    # plot_matrix(neuro_network.ascii_to_letter('H'))

    noised_H = neuro_network.make_noise(LETTERS['H'], NOISE_PERCENT)
    print('noised letter to ascii:',
          neuro_network.noised_letter_to_ascii(noised_H).transpose())


if __name__ == "__main__":
    main()
