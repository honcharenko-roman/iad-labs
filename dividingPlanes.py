import classnition
import numpy as np
import matplotlib.pyplot as plt

array_center_point = []

legend_map = {
    1: 'r',
    2: 'b',
    3: 'g',
    4: 'm',
}

values = []

def get_center_classes(classes):
    for class_point in classes:
        array_center_point.append(classnition._etalon_point(class_point))
    return array_center_point


def get_mid_section_classes():
    array = [[

    ]]
    array.clear()

    for i in range(0, len(array_center_point)):
        iter_array_center_point = iter(array_center_point)
        for k in range(0, i + 1):
            next(iter_array_center_point)

        for center_point in iter_array_center_point:
            array.append([(array_center_point[:][i][0] + center_point[0]) / 2,
                          (array_center_point[:][i][1] + center_point[1]) / 2])

    return array


def draw_points_and_lines():
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onclick)
    draw_center_lines()
    draw_lines()
    draw_etalon_points()
    draw_center_points()
    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([-0.2, 1])
    axes.set_ylim([-0.5, 1.5])
    plt.show()
    # print(coord_x_array)


def draw_etalon_points():
    legend_map = {
        1: 'r',
        2: 'b',
        3: 'g',
        4: 'm',
    }
    count = 1
    for point in array_center_point:
        plt.plot(point[0], point[1], legend_map[count])
        count += 1


def draw_center_points():
    for point in get_mid_section_classes():
        plt.plot(point[0], point[1], 'or')


def draw_lines():
    count = 1
    legend_map = {
        1: 'r',
        2: 'darkorange',
        3: 'k',
    }
    for i in range(0, len(array_center_point)):
        iter_array_center_point = iter(array_center_point)
        for k in range(0, i + 1):
            next(iter_array_center_point)

        for center_point in iter_array_center_point:
            x1, y1 = [array_center_point[:][i][0], center_point[0]], [array_center_point[:][i][1], center_point[1]]
            plt.plot(x1, y1, legend_map[count])
        count += 1


def get_coefficient_k():
    array_k = []
    for i in range(0, len(array_center_point)):
        iter_array_center_point = iter(array_center_point)
        for k in range(0, i + 1):
            next(iter_array_center_point)

        for center_point in iter_array_center_point:
            k = (center_point[1] - array_center_point[:][i][1]) / (center_point[0] - array_center_point[:][i][0])
            array_k.append((-1) / k)
    return array_k


coord_x_array = np.arange(-0.3, 0.8, 0.01)


def draw_center_lines():
    i = 0
    for line_center_point in get_mid_section_classes():
        iter_mid = iter(get_coefficient_k())

        for _ in range(0, i):
            next(iter_mid)

        for k in iter_mid:
            coord_y_array = (k * (coord_x_array - line_center_point[0]) + line_center_point[1])

            #print('{} * (x - {}) + {}'.format(k, line_center_point[0], line_center_point[1]))
            plt.plot(coord_x_array, coord_y_array, 'b')
            break
        i += 1


def get_final_equation(k, line_center_point, start_point):
    d = (k * (start_point[0] - line_center_point[0]) + line_center_point[1]) - start_point[1]
    return d


def classify_class(d):
    if d[0] < 0 and d[1] > 0 and d[2] < 0 :
        return 1
    elif d[0] > 0 and d[3] > 0 and d[4] < 0 :
        return 2
    elif d[1] < 0 and d[3] < 0 and d[5] < 0 :
        return 3
    elif d[2] > 0 and d[4] > 0 and d[5] > 0:
        return 4
    else: 
        return 0


def onclick(event):
    i = 0
    values = []
    test_array = np.array( [event.xdata, event.ydata] )
    for line_center_point in get_mid_section_classes():
        iter_mid = iter(get_coefficient_k())

        for _ in range(0, i):
            next(iter_mid)

        for k in iter_mid:
            values.append(get_final_equation(k, line_center_point, test_array))
            break
        i += 1

    print (values)
    plt.scatter(event.xdata, event.ydata,
            c = legend_map[classify_class(values)])
    plt.show()
