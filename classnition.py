from math import sqrt
import numpy as np


def euklid_distance(point1, point2):
    dx = (point1[0] - point2[0]) ** 2
    dy = (point1[1] - point2[1]) ** 2
    return sqrt(dx + dy)


def get_euklid_distance_map(classes, start_point):
    euklid_distance_map = {
    }
    for points_class in classes:
        for point in points_class:
            euklid_distance_map[euklid_distance(start_point, point)] = point
    return euklid_distance_map


def euklid_closest_point(classes, start_point):
    euklid_distance_map = get_euklid_distance_map(classes, start_point)
    closest_point_distance = min(euklid_distance_map.keys())
    closest_point = euklid_distance_map.get(closest_point_distance)
    return closest_point


def euklid_class_number(classes, start_point):
    class_number = 0
    for points_class in classes:
        class_number += 1
        for point in points_class:
            if np.array_equal(point, euklid_closest_point(classes, start_point)):
                return class_number


def minkovsky_distance(point1, point2, val):
    dx = pow(abs((point1[0] - point2[0])), val)
    dy = pow(abs((point1[1] - point2[1])), val)
    return pow(dx + dy, 1 / val)


def get_minkovsky_distance_map(classes, start_point, val):
    minkovsky_distance_map = {  # distance to start point : points coordinats
    }
    for points_class in classes:
        for point in points_class:
            minkovsky_distance_map[minkovsky_distance(start_point, point, val)] = point
    return minkovsky_distance_map


def minkovsky_closest_point(classes, start_point, val):
    minkovsky_distance_map = get_minkovsky_distance_map(classes, start_point, val)
    closest_point_distance = min(minkovsky_distance_map.keys())
    closest_point = minkovsky_distance_map.get(closest_point_distance)
    return closest_point


def minkovsky_class_number(classes, start_point, val):
    class_number = 0
    for points_class in classes:
        class_number += 1
        for point in points_class:
            if np.array_equal(point, minkovsky_closest_point(classes, start_point, val)):
                return class_number



def _etalon_point(class_array):
    x = sum(class_array[:, 0])
    y = sum(class_array[:, 1])
    return np.array([x/len(class_array), y/len(class_array)])    


def euklid_etalon_distances(classes, start_point):
    etalon_distances = []
    for i in classes:
        etalon_distances.append(euklid_distance(_etalon_point(i), start_point))
    return etalon_distances



def euklid_sum_of_closest_etalons(classes, start_point):
    etalon_distances = euklid_etalon_distances(classes, start_point)
    etalon_distances.sort()
    return etalon_distances[0] + etalon_distances[1] 

def minkovsky_etalon_distances(classes, start_point):
    etalon_distances = []
    for i in classes:
        etalon_distances.append(euklid_distance(_etalon_point(i), start_point))
    return etalon_distances

def minkovsky_sum_of_closest_etalons(classes, start_point):
    etalon_distances = minkovsky_etalon_distances(classes, start_point)
    etalon_distances.sort()
    return etalon_distances[0] + etalon_distances[1]

