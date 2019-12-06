from scipy.fftpack import fft, ifft
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math


class ClassificationNetwork:

    def transform_data(self, data):
        return self.__signs_space__(
            self.__fourier_transform__(
                self.__transform_raw_data__(data)))

    def __fourier_transform__(self, data):
        return np.abs(fft(data))

    def __transform_raw_data__(self, raw_data):
        data = raw_data[1000:]
        max_elem = max(abs(data))
        # normalization
        data = [i / max_elem for i in data]
        return data

    def __signs_space__(self, fft_out):
        result = [
        ]
        for i in range(100, 2000, 100):
            result.append(mean(fft_out[i:i+100]))

        result = np.asarray(result)
        max_value = max(abs(result))
        result = [i / max_value for i in result]
        return result

    def __find_average_sound__(self, sound_letter, sounds_map):
        sums = []
        for name, approved_sound in self.sounds_map.items():
            if sound_letter in name:
                sums.append(approved_sound)
        return self.__sum_data__(sums)

    def __sum_data__(self, *args):
        res_list = [0 for x in range(len(args[0][0]))]
        for data_list in args:
            for i in data_list:
                for index, element in enumerate(i):
                    res_list[index] += element
        res_list = [element/len(args[0]) for element in res_list]
        return res_list

    def teach(self, training_inputs):
        self.sounds_map = training_inputs
        self.avg_a = self.__find_average_sound__('a', self.sounds_map)
        self.avg_e = self.__find_average_sound__('e', self.sounds_map)
        self.avg_i = self.__find_average_sound__('i', self.sounds_map)

    def determine(self, name, data):
        result_map = {
            '- Вероятнее всего, это буква A.': self.__compare_data__(data, self.avg_a),
            '- Вероятнее всего, это буква E.': self.__compare_data__(data, self.avg_e),
            '- Вероятнее всего, это буква I.': self.__compare_data__(data, self.avg_i)
        }
        if min(result_map.values()) < 100:
            print(name, self.__get_key__(min(result_map.values()), result_map))
        else:
            print(name, '- Простите, распознать эту букву не могу :(')

    def __get_key__(self, val, dictionary):
        for key, value in dictionary.items():
            if val == value:
                return key

    def __compare_data__(self, data_1, data_2):
        res_list = []
        for a, b in zip(data_1, data_2):
            if a < b:
                res_list.append(abs(((b - a) / a) * 100))
            elif a == b:
                res_list.append(0)
            else:
                res_list.append(abs(((b - a) / a) * 100))

        return mean(res_list)
