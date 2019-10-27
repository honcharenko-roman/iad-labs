from math import sqrt
import numpy as np
import filemanager
import plot


def euklid_distance(point1, point2):
    dx = (point1[0] - point2[0]) ** 2
    dy = (point1[1] - point2[1]) ** 2
    return sqrt(dx + dy)


def get_euklid_distance_map(classes, start_point):
    euklid_distance_map = {}
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
    minkovsky_distance_map = {}  # distance to start point : points coordinats
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


def _center_point(class_array):
    if class_array.size != 0:
        x = sum(class_array[:, 0])
        y = sum(class_array[:, 1])
        return np.array([x/len(class_array), y/len(class_array)])    


def euklid_center_distances(classes, start_point):
    center_distances_map = {}   #distance to start_point: class_number
    k = 1
    for i in classes:
        center_distances_map[euklid_distance(_center_point(i), start_point)] = k
        k += 1
    return center_distances_map


def center_method_class_number(classes, start_point):
    center_distances_map = euklid_center_distances(classes, start_point)
    closest_distance = min(center_distances_map.keys())
    return  center_distances_map[closest_distance]


def euklid_sum_of_closest_center(classes, start_point):
    center_distances = euklid_center_distances(classes, start_point).values()
    center_distances.sort()
    return center_distances[0] + center_distances[1] 


def minkovsky_center_distances(classes, start_point):
    center_distances = []
    for i in classes:
        center_distances.append(euklid_distance(_center_point(i), start_point))
    return center_distances


def minkovsky_sum_of_two_closest_center(classes, start_point):
    center_distances = minkovsky_center_distances(classes, start_point)
    center_distances.sort()
    return center_distances[0] + center_distances[1]


def classify_points(points, center_points):
    local_array = []
    classification_map = {} #point : classified_class
    i = 0
    for point in points:
        local_array.clear()
        local_array.append(5)
        for center_point in center_points:
            local_array.append(euklid_distance(point, center_point))
        classification_map[i] = local_array.index(min(local_array))
        i+=1
    return classification_map


def get_random_points_array(number_of_points):
    random_points_array = np.array([])
    for i in range (1, number_of_points + 1):
        random_point = [float ('%.2f' % i) for i in np.random.rand(2)]
        random_points_array = np.append(random_points_array, random_point)
    random_points_array = np.reshape(random_points_array, (number_of_points,2))
    return random_points_array
