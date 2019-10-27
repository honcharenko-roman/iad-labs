import numpy as np
import dividingPlanes
import os


NUMBER_OF_CLASSES = 4


def get_classes(new_or_old, number_of_classes):
    if new_or_old == "old":
        classes = []
        for i in range(1, NUMBER_OF_CLASSES + 1):
            classes.append(np.loadtxt('class{}.txt'.format(i)))
        classes = np.asarray(classes)
    else :
        classes = []
        for i in range(1, number_of_classes + 1):
            classes.append(np.loadtxt('newclass{}.txt'.format(i)))
        classes = np.asarray(classes)
    return classes


def save_all_points(classes):
    f=open("class0.txt", "w+")
    for points_array in classes:
        for point in points_array:
            f.write("{:.2f} {:.2f}\n".format(point[0], point[1]))
    f.close()


def get_all_points_array():
    class0 = np.loadtxt("class0.txt")
    return class0


def clear_files():
    for i in range (1, 9):
        file_name = "newclass{}.txt".format(i)
        f = open(file_name, "w+")
        f.close()


def save_points_by_classes(points, classification_map):
    clear_files()
    for i in classification_map:
        write_data_to_file_by_point(points[i][0], points[i][1], classification_map[i])


def write_data_to_file_by_point(x, y, class_number):
    file_name = "newclass{}.txt".format(class_number)
    f = open(file_name, "a+")
    f.write("{:.2f} {:.2f}\n".format(x, y))
    f.close()


def write_data_to_file_by_array(array, class_number):
    f=open("class{}.txt".format(class_number), "w+")
    for point in array:
        f.write("{:.2f} {:.2f}\n".format(point[0], point[1]))
    f.close()


def get_center_points():
    return np.loadtxt("center_points.txt")
    
    
def write_down_center_points(center_points):
    f=open("center_points.txt", "w+")

    for center_point in center_points:
        if center_point is not None:
            f.write("{:.4f} {:.4f}\n".format(center_point[0], center_point[1]))
    f.close()
