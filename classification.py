import numpy as np
import random

def get_point(dimension_list, dimension, index):
    point = []
    for i in range(0, dimension):
        point.append(dimension_list[i][index])
    return np.array(point)

def calculate_distances(point, matrix):
    distances = []
    for m_point in matrix:
        distances.append(np.linalg.norm(m_point-point))
    distances.sort()
    return distances

def classification_using_NN(matrix_to_pass, matrix_to_disturb, test, best_coordinates, dimension, k):
    amount_of_test = len(test[0])
    # creating test points
    test_list = []
    pass_list = []
    disturb_list = []
    print(dimension)
    # creating test list, pass list, disturb list
    for i in range(0, dimension):
        print(best_coordinates[i])
        test_list.append(test[best_coordinates[i]])
        pass_list.append(matrix_to_pass[best_coordinates[i]])
        disturb_list.append(matrix_to_disturb[best_coordinates[i]])

    # print(test_list)
    # print(len(test_list))
    more_suitable_pass = []
    for pass_index in range(0, len(pass_list[0])):
        more_suitable_pass.append(get_point(pass_list, dimension, pass_index))

    more_suitable_dist = []
    for dist_index in range(0, len(disturb_list[0])):
        more_suitable_dist.append(get_point(disturb_list, dimension, dist_index))
    
    recognize_correctly = 0
    # main loop
    for test_index in range(0, len(test_list[0])):
        test_point = get_point(test_list, dimension, test_index)
        distances_from_pass = calculate_distances(test_point, more_suitable_pass)
        distances_from_dist = calculate_distances(test_point, more_suitable_dist)
        pass_index = 0
        dist_index = 0
        for i in range(0, k):
            if(distances_from_pass[pass_index] < distances_from_dist[dist_index]):
                pass_index += 1
            else:
                dist_index += 1
        # print("Pass: " + str(pass_index) + " Not pass: " + str(dist_index))
        if pass_index > dist_index:
            recognize_correctly += 1
    print("R " + str(recognize_correctly))
    print("To test: " + str(amount_of_test))
    pass_to_first_matrix = recognize_correctly / amount_of_test
    return pass_to_first_matrix


def classification_using_nearest_mean(matrix_1, matrix_2, test, best_coordinates, dimension, k = 1):
    how_many_pass_to_matrix_1 = 0
    how_many_pass_to_matrix_2 = 0
    amount_of_test = len(test[0])
    kx = 0
    for i in matrix_1:
        kx+=1
        print(kx)
        print(i.shape)

    pass_to_first_matrix = how_many_pass_to_matrix_1 / amount_of_test
    pass_to_second_matrix = how_many_pass_to_matrix_2 /amount_of_test
    return pass_to_first_matrix, pass_to_second_matrix
