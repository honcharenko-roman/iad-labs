import binascii
import random

import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork():

    def __init__(self, LETTERS):
        self.LETTERS = LETTERS
        self.ASCII_LENGTH = 8
        self.NUMBER_OF_ROWS = np.size(list(LETTERS.values())[0], 0)
        self.NUMBER_OF_COLUMNS = np.size(list(LETTERS.values())[0], 1)
        self.MATRIX_SIZE = self.NUMBER_OF_COLUMNS * self.NUMBER_OF_ROWS
        self.auto_associative_matrix = np.array([])
        self.getero_associative_matrix = np.array([])
        self.MAX_ITERATIONS = 250

    def unravel_matrix(self, letter):
        ravel = letter.ravel(order='F')
        wide = np.reshape(ravel, (1, ravel.size))
        long = np.reshape(wide, (wide.size, 1))
        return long, wide

    def teach(self):
        long_H, wide_H = self.unravel_matrix(self.LETTERS['H'])
        long_R, wide_R = self.unravel_matrix(self.LETTERS['R'])
        long_I, wide_I = self.unravel_matrix(self.LETTERS['I'])
        long_Y, wide_Y = self.unravel_matrix(self.LETTERS['Y'])

        self.auto_associative_matrix = np.dot(long_H, wide_H) + np.dot(long_R,
                                                                       wide_R) + np.dot(long_I, wide_I) + np.dot(long_Y, wide_Y)

        np.fill_diagonal(self.auto_associative_matrix, 0)

        ascii_H = np.reshape(self.text_to_bits('H'), (1, self.ASCII_LENGTH))
        ascii_R = np.reshape(self.text_to_bits('R'), (1, self.ASCII_LENGTH))
        ascii_Y = np.reshape(self.text_to_bits('Y'), (1, self.ASCII_LENGTH))
        ascii_I = np.reshape(self.text_to_bits('I'), (1, self.ASCII_LENGTH))

        self.getero_associative_matrix = ascii_H * long_H + ascii_R * long_R + \
            ascii_Y * long_Y  + ascii_I * long_I

    def letter_to_ascii(self, letter):
        self.getero_associative_matrix = np.reshape(
            self.getero_associative_matrix, (self.MATRIX_SIZE, self.ASCII_LENGTH))
        _, wide_letter = self.unravel_matrix(letter)
        result = np.dot(wide_letter, self.getero_associative_matrix)
        return np.reshape(np.sign(result), (self.ASCII_LENGTH, 1))

    def noised_letter_to_ascii(self, letter):
        corrected_letter = self.correct(letter)
        return self.letter_to_ascii(corrected_letter)

    def ascii_to_letter(self, string_letter):
        self.getero_associative_matrix = np.reshape(
            self.getero_associative_matrix, (self.MATRIX_SIZE, self.ASCII_LENGTH))
        string_letter = self.text_to_bits(string_letter)
        ascii_letter = np.reshape(string_letter, (1, self.ASCII_LENGTH))
        result = np.dot(
            ascii_letter, self.getero_associative_matrix.transpose())
        return np.reshape(np.sign(result), (self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS), order='F')

    def noised_ascii_to_letter(self, noised_ascii):
        self.getero_associative_matrix = np.reshape(
            self.getero_associative_matrix, (self.MATRIX_SIZE, self.ASCII_LENGTH))
        noised_ascii = np.reshape(noised_ascii, (1, 8))
        result = np.dot(
            noised_ascii, self.getero_associative_matrix.transpose())
        result = np.where(result == 0, 1, result)
        return np.reshape(np.sign(result), (self.NUMBER_OF_COLUMNS, self.NUMBER_OF_ROWS), order='F')

    def correct(self, noised_letter):
        index = 0
        flag = 0
        while True:
            output_values = []
            _, wide_noised = self.unravel_matrix(noised_letter)
            for i in range(0, np.size(self.auto_associative_matrix, 1)):
                output_values.append(
                    np.sign(sum(wide_noised[0] * self.auto_associative_matrix[:, i])))
            output_values = np.asarray(output_values)
            output_values = np.reshape(
                output_values, (self.NUMBER_OF_ROWS, self.NUMBER_OF_COLUMNS), order='F')
            noised_letter = output_values
            index += 1
            for value in self.LETTERS:
                if np.all(np.equal(noised_letter, self.LETTERS[value])):
                    print('LETTER RECOGNIZED')
                    flag = 1
                    break
            if flag:
                break
            if index > self.MAX_ITERATIONS:
                print('LETTER CANNOT BE RECOGNIZED')
                break
        return noised_letter

    def make_noise(self, letter, noise_percent):
        number_of_noised = int(
            (np.size(letter, 0) * np.size(letter, 1)) * (noise_percent * 0.01))
        noised_positions = random.sample(
            range(0, np.size(letter, 0) * np.size(letter, 1)), number_of_noised)

        noised_letter = np.copy(letter)

        index = 0
        for i in range(0, np.size(letter, 0)):
            for j in range(0, np.size(letter, 1)):
                if index in noised_positions:
                    noised_letter[i][j] = -noised_letter[i][j]
                index += 1

        return noised_letter

    def correct_ascii(self, noised_ascii):
        # print(np.array_str(noised_ascii[0]))
        # print (str(noised_ascii[0]))
        return self.correct(self.noised_ascii_to_letter(noised_ascii))

    def text_to_bits(self, text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int(binascii.hexlify(
            text.encode(encoding, errors)), 16))[2:]
        string = bits.zfill(8 * ((len(bits) + 7) // 8))
        string = string.replace('0', '-1 ')
        string = string.replace('1', '1 ')
        array = np.fromstring(string, sep=' ')
        array = array.astype(int)
        return array
