from math import sqrt
import collections

import numpy as np
import matplotlib.pyplot as plt

import classnition
import dividingPlanes
import plot 
import filemanager


NUMBER_OF_CLASSES = 3
NUMBER_OF_ITERATIONS = 20
DISTANCE_DIFFERENCE = 0.001
NUMBER_OF_POINTS = 25


def main():
    
    classes = np.array([classnition.get_random_points_array(NUMBER_OF_POINTS), 
                        classnition.get_random_points_array(NUMBER_OF_POINTS),
                        classnition.get_random_points_array(NUMBER_OF_POINTS),
                        classnition.get_random_points_array(NUMBER_OF_POINTS)
    ])


    #TODO: inprogramm calclulations
    # all_points_array = []
    # for points_array in classes:
    #     for point in points_array:
    #         all_points_array.append(point)
    # all_points_array = np.asarray(all_points_array)


    center_points = classnition.get_random_points_array(NUMBER_OF_CLASSES)
    filemanager.save_all_points(classes)
    points_array = filemanager.get_all_points_array()
    classification_map = classnition.classify_points(points_array, center_points)
    filemanager.save_points_by_classes(points_array, classification_map)
    plot.build_plot(classes)
    
    
    for _ in range(NUMBER_OF_ITERATIONS):
        distance_difference_sum = 0
        classes = filemanager.get_classes("new", NUMBER_OF_CLASSES)
        plot.update_plot(classes)
        j = 0

        for points in classes:
            distance_difference_sum += classnition.euklid_distance(center_points[j], classnition._center_point(points))
            center_points[j] = classnition._center_point(points)
            j+=1
        classification_map = classnition.classify_points(points_array, center_points)
        filemanager.save_points_by_classes(points_array, classification_map)

        if distance_difference_sum < DISTANCE_DIFFERENCE * NUMBER_OF_CLASSES:
            plot.job_is_done(5)
            break



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
