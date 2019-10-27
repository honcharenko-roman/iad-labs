import classnition
import numpy as np
import matplotlib.pyplot as plt
import filemanager

def center_points(classes):
    center_points_array = []
    for class_point in classes:
        if class_point.size != 0:
            center_points_array.append(classnition._center_point(class_point))
    filemanager.write_down_center_points(center_points_array)


def line_between_center_points(center_points):
    dx = center_points[1][0] - center_points[0][0]
    dy = center_points[1][1] - center_points[0][1]
    k = dy/dx

    b = (center_points[0][1] * dx - center_points[0][0] * dy) / dx
    return k, b


def straight_line_equation(k, x, b):
    return k * x + b 


def get_mid_section(center_point1, center_point2):
    x = center_point1[0] + center_point2[0]
    y = center_point1[1] + center_point2[1]
    return np.array([x/2, y/2]) 
    