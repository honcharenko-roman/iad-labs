import random
from math import sqrt

import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox as mb

import classnition
import dividingPlanes
import plot


def generate_random_point():
    start_p = np.array([random.uniform(0, 1), random.uniform(0, 1)])
    return start_p


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


def main():
    classes = init_arrays()

    plot.build_plot(classes)

    print(dividingPlanes.get_center_classes(classes))

    dividingPlanes.get_mid_section_classes()
    dividingPlanes.draw_points_and_lines()
    # GUI
    # root = Tk()
    # root.title("Диалоговое окно")
    # root.geometry("500x350")

    # header = Label(text="Выберите метод", padx=15, pady=10)
    # header.grid(row=0, column=0, sticky=W)

    # lang = IntVar()
    # lang.set(0)

    # Euklid_button = Radiobutton(root, text="Метод Евклида", value=1, variable=lang, height=3)
    # Euklid_button.grid(row=1, column=0, sticky=W)

    # Minkovsky_button = Radiobutton(root, text="Метод Минковского", value=2, variable=lang)
    # Minkovsky_button.grid(row=2, column=0, sticky=W, pady=10)

    # label = Label(root, text="Случайно сгенерированная точка: \n{}".format(start_point), height=8)
    # label.grid(row=0, column=1, sticky=W)

    # label = Label(root, text="Наибольшое значение расстояния \n среди эталонов классов: \n{}".format(
    #     max(classnition.etalon_distances(classes, start_point)), height=8))
    # label.grid(row=1, column=1, sticky=W)

    # label = Label(root, text="Сумма значений расстояния к двум \nближайшим эталонам класса: \n{}".format(
    #     classnition.sum_of_closest_etalons(classes, start_point, 2)), height=8)
    # label.grid(row=2, column=1, sticky=W)

    # button = Button(root, text="Продолжить", command=select_method, justify=CENTER)
    # button.grid(row=6, column=1, sticky=S)

    # button1 = Button(root, text="Закончить", command=finish, justify=CENTER)
    # button1.grid(row=6, column=2, sticky=S, padx=20)

    # root.mainloop()

    # def select_method():
    #     result = lang.get()
    #     if result == 1:
    #         build_plot(classes, classnition.euklid_class_number(classes, start_point))
    #     elif result == 2:
    #         build_plot(classes, classnition.Minkovsky_class_number(classes, start_point, 3))
    #     else:
    #         mb.showerror("Ошибка", "Выберите какой-либо метод")

    # def finish():
    #     answer = mb.askyesno("Выход", "Вы точно хотите выйти?")
    #     if answer:
    #         root.destroy()


if __name__ == "__main__":
    main()
