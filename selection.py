import numpy as np
import sys
from itertools import combinations
import random


def calculate_combinations(matrix_length, dimension):
    rows = []
    for i in range(matrix_length):
        rows.append(i)
    return list(combinations(rows, dimension))


def calculate_det_like_in_lesson(matrix):
    mean_vector = matrix.mean(1)
    for row in range(np.size(matrix, 0)):
        for column in range(np.size(matrix, 1)):
            matrix[row][column] = matrix[row][column] - mean_vector[row]
    matrix_std = 1 / np.size(matrix, 1) * np.matmul(matrix, matrix.transpose())
    return np.linalg.det(matrix_std)


def calculate_mean_vector(matrix):
    return matrix.mean(1)


def calculate_f(matrix1, matrix2, dimension=1):
    f_results = {}
    # calculate mean vector
    all_combinations = calculate_combinations(len(matrix1),dimension)
    mean_vector1 = calculate_mean_vector(matrix1)
    mean_vector2 = calculate_mean_vector(matrix2)
    
    the_best_result = 0
    the_best_coordinates = None
    for coordinates in all_combinations:
        temp_mean_vector1 = []
        temp_mean_vector2 = []
        temp_matrix1 = []
        temp_matrix2 = []
        for i in coordinates:
            temp_mean_vector1.append(mean_vector1[i])
            temp_mean_vector2.append(mean_vector2[i])
            temp_matrix1.append(matrix1[i])
            temp_matrix2.append(matrix2[i])
        # distance between matrix
        numerator = np.linalg.norm(np.array(temp_mean_vector1) - (np.array(temp_mean_vector2)))
        # sum of standard deviation
        denominator = 0
        if len(coordinates) > 1:
            denominator = calculate_det_like_in_lesson(np.array(temp_matrix1)) + calculate_det_like_in_lesson(np.array(temp_matrix2))
        else:
            denominator = np.array(temp_matrix1).std() + np.array(temp_matrix2).std()
        f_results[coordinates] = (numerator / denominator)

        if the_best_result < f_results[coordinates]:
            the_best_result = f_results[coordinates]
            the_best_coordinates = coordinates

    # print("The best coordinates (f): " + str(the_best_coordinates))
    return the_best_coordinates


def calculate_sfs(matrix1, matrix2, dimension=1):
    f_results = {}
    # calculate mean vector
    mean_vector1 = calculate_mean_vector(matrix1)
    mean_vector2 = calculate_mean_vector(matrix2)
    
    the_best_diff = 0
    the_best_coordinates = ()
    for d in range(1, dimension + 1):
        # refresh value
        the_best_diff = 0
        # print(d)
        # get all possible combinations
        all_combinations = calculate_combinations(len(matrix1), d)
        chosen_combinations = []
        # print(all_combinations)
        if the_best_coordinates:
            for coordinates_candidate in all_combinations:
                flag = True
                for i in the_best_coordinates:
                    flag = i in coordinates_candidate
                    if not flag:
                        break
                if flag:
                    chosen_combinations.append(coordinates_candidate)
        # print("Chosen comb:" + str(chosen_combinations))
        if not chosen_combinations:
            chosen_combinations = all_combinations

        for coordinates in chosen_combinations:
            temp_mean_vector1 = []
            temp_mean_vector2 = []
            temp_matrix1 = []
            temp_matrix2 = []
            for i in coordinates:
                temp_mean_vector1.append(mean_vector1[i])
                temp_mean_vector2.append(mean_vector2[i])
                temp_matrix1.append(matrix1[i])
                temp_matrix2.append(matrix2[i])
            # distance between matrix
            numerator = np.linalg.norm(np.array(temp_mean_vector1) - (np.array(temp_mean_vector2)))
            
            # sum of standard deviation
            denominator = 0
            if len(coordinates) > 1:
                # print("Macierz: " + str(temp_matrix1))
                # print("Wyznacznik macierzy: " + str(calculate_det_like_in_lesson(np.array(temp_matrix1))))
                denominator = calculate_det_like_in_lesson(np.array(temp_matrix1)) + calculate_det_like_in_lesson(np.array(temp_matrix2))
            else:
                denominator = np.array(temp_matrix1).std() + np.array(temp_matrix2).std()
            
            # print(f_results)
            f_results[coordinates] = (numerator / denominator)
            # print(f_results)
            if the_best_diff < f_results[coordinates]:
                the_best_diff = f_results[coordinates]
                # print("Change: " + str(the_best_coordinates))
                # print("On: " + str(coordinates))
                the_best_coordinates = coordinates

    # print("The best coordinates (sfs): " + str(the_best_coordinates))
    return the_best_coordinates
