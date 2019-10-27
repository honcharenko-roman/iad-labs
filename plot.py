from matplotlib import pyplot as plt
import numpy as np

import itertools

import classnition
import dividingPlanes
import filemanager


points = []
fig = plt.figure()
ax = fig.add_subplot(111)


colors_map = {
    1: 'b',
    2: 'g',
    3: 'r',
    4: 'm',
    5: 'c',	
    6: 'y',
    7: 'k',
    8: 'w',	
}


legend_map = {
        -1: '*',
        0: 'x',
        1: 'o'+colors_map[1],
        2: 'o'+colors_map[2],
        3: 'o'+colors_map[3],
        4: 'o'+colors_map[4],
        5: 'o'+colors_map[5],
        6: 'o'+colors_map[6],
        7: 'o'+colors_map[7],
        8: 'o'+colors_map[8]
    }


def build_plot(classes):
    draw_classes(classes)
    fig.subplots_adjust(top=0.85)
    axes = plt.gca()
    axes.set_xlim([-0.1, 1.1])
    axes.set_ylim([-0.1, 1.1])
    plt.grid(True)
    plt.ion()
    plt.show()


def job_is_done(seconds):
    fig.suptitle('Done')
    plt.pause(seconds)
    

def pause_plot(seconds):
    plt.pause(seconds)


def onclick(event):
    start_point = np.array([event.xdata, event.ydata])
    updated_classes = filemanager.read_data_from_file()

    start_point_class_number = classnition.center_method_class_number(updated_classes, start_point)

    filemanager.write_data_to_file(event.xdata, event.ydata, start_point_class_number)
    updated_classes = filemanager.read_data_from_file()

    plt.clf()
    draw_classes(updated_classes)
    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([-0.5, 1.5])
    axes.set_ylim([-0.5, 1.5])
    draw_center_points(updated_classes)
    plt.show()


def update_plot(classes):
    plt.pause(0.001)
    global points 
    for point in points:
        point.remove()
    points = draw_classes(classes)


def draw_center_points(updated_classes):
    k = 1
    dividingPlanes.center_points(updated_classes)
    center_points = filemanager.get_center_points()
    for point in center_points:
        points.extend(
            plt.plot(point[0], point[1], legend_map[0], c = colors_map[k])
        )
        if k <= len(center_points):
            k += 1
    return points


def draw_classes(updated_classes):
    points = []
    k = 1
    for array_point in updated_classes:
        for point in array_point:
            points.extend(
            plt.plot(point[0], point[1], legend_map[k])
            )
        k += 1
    fig.canvas.draw()
    return points
