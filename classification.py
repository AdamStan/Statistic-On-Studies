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

def classification_using_NN(matrix_to_match, matrix_to_disturb, test, best_coordinates, dimension, k):
    amount_of_test = len(test[0])
    # creating test points
    test_list = []
    match_list = []
    disturb_list = []
    # print(dimension)
    # creating test list, match list, disturb list
    # print(test)
    for i in range(0, dimension):
        # print(best_coordinates[i])
        test_list.append(test[best_coordinates[i]])
        match_list.append(matrix_to_match[best_coordinates[i]])
        disturb_list.append(matrix_to_disturb[best_coordinates[i]])
    # print(test_list)
    # print(disturb_list)
    # print(len(disturb_list))
    more_suitable_match = []
    for match_index in range(0, len(match_list[0])):
        more_suitable_match.append(get_point(match_list, dimension, match_index))
    more_suitable_dist = []
    for dist_index in range(0, len(disturb_list[0])):
        more_suitable_dist.append(get_point(disturb_list, dimension, dist_index))
    # print(len(disturb_list[0]))
    # print(more_suitable_dist)
    recognize_correctly = 0
    # main loop
    for test_index in range(0, len(test_list[0])):
        test_point = get_point(test_list, dimension, test_index)
        # print(test_point)
        distances_from_match = calculate_distances(test_point, more_suitable_match)
        distances_from_dist = calculate_distances(test_point, more_suitable_dist)
        match_index = 0
        dist_index = 0
        # print("match: " + str(distances_from_match))
        # print("Dist: " + str(distances_from_dist))
        for i in range(0, k):
            if(distances_from_match[match_index] <= distances_from_dist[dist_index]):
                match_index += 1
            else:
                dist_index += 1
        # print("match: " + str(match_index) + " Not match: " + str(dist_index))
        if match_index > dist_index:
            recognize_correctly += 1
    # print("Poprawnie rozpoznane: " + str(recognize_correctly))
    # print("Wszystkie testowe: " + str(amount_of_test))
    return recognize_correctly, amount_of_test

def equal_for_divide_on_k_matrixes(group_matrix1, group_matrix2):
    try:
        for i in range(len(group_matrix1)):
            for j in range(len(group_matrix1[i])):
                if group_matrix1[i][j][0] == group_matrix2[i][j][0] \
                        and group_matrix1[i][j][1] == group_matrix2[i][j][1]:
                    continue
                else:
                    return False
        return True
    except Exception:
        return False

def divide_on_k_matrixes(matrix_to_divide, how_many_matrixes):
    matrixes = []
    chosen_indexes = []
    i = 0
    while i < how_many_matrixes:
        random_index = random.randint(0, len(matrix_to_divide) - 1)
        if random_index in chosen_indexes:
            continue
        matrixes.append(np.array([matrix_to_divide[random_index]]))
        chosen_indexes.append(random_index)
        i += 1

    # first calculation
    for i in range(0, len(matrix_to_divide)):
        # print(chosen_indexes)
        if i in chosen_indexes:
            continue
        distnaces = []
        min_value = None
        chosen = 0
        for index_group in range(0, len(matrixes)):
            distnaces.append(np.linalg.norm(matrix_to_divide[i] - matrixes[index_group]))
            if min_value is None or min_value > distnaces[-1]:
                min_value = distnaces[-1]
                chosen = index_group
        matrixes[chosen] = np.append(matrixes[chosen], [matrix_to_divide[i]], axis=0)
    
    while True:
        new_groups = []
        # print(matrixes)
        # print("====================")
        for i in range(how_many_matrixes):
            new_groups.append([])
        for group_to_use in matrixes:
            mean_vector = []
            for group in matrixes:
                mean_vector.append(group.mean(0))
            for point in group_to_use:
                distnaces = []
                min_value = None
                chosen = 0
                for index_group in range(len(mean_vector)):
                    distnaces.append(np.linalg.norm(point - mean_vector[index_group]))
                    if min_value is None or min_value > distnaces[-1]:
                        min_value = distnaces[-1]
                        chosen = index_group
                if len(new_groups[chosen]) == 0:
                    new_groups[chosen] = np.array([point])
                else:
                    new_groups[chosen] = np.append(new_groups[chosen], [point], axis=0)
        if equal_for_divide_on_k_matrixes(new_groups, matrixes):
            break
        else:
            matrixes = new_groups

    return matrixes

def classification_using_nearest_mean(matrix_to_match, matrix_to_disturb, test, best_coordinates, dimension, k = 1):
    correctly_recognized = 0
    amount_of_test = len(test[0])
    
    amount_of_test = len(test[0])
    # creating test points
    test_list = []
    match_list = []
    disturb_list = []
    # print(dimension)
    # creating test list, match list, disturb list
    for i in range(0, dimension):
        # print(best_coordinates[i])
        test_list.append(test[best_coordinates[i]])
        match_list.append(matrix_to_match[best_coordinates[i]])
        disturb_list.append(matrix_to_disturb[best_coordinates[i]])
    # print(test_list)

    more_suitable_match = []
    for match_index in range(0, len(match_list[0])):
        more_suitable_match.append(get_point(match_list, dimension, match_index))
    more_suitable_match = np.array(more_suitable_match)
    # print(more_suitable_match)
    more_suitable_dist = []
    for dist_index in range(0, len(disturb_list[0])):
        more_suitable_dist.append(get_point(disturb_list, dimension, dist_index))
    more_suitable_dist = np.array(more_suitable_dist)
    # print(more_suitable_dist)
    
    # podzial matrix1 i matrix2 na k zbiorow
    k_matrixes_to_match = []
    k_matrixes_to_dist = []
    if k > 1:
        k_matrixes_to_match = divide_on_k_matrixes(more_suitable_match, k)
        k_matrixes_to_dist = divide_on_k_matrixes(more_suitable_match, k)
    else:
        k_matrixes_to_match.append(more_suitable_match)
        k_matrixes_to_dist.append(more_suitable_dist)

    # policzenie odleglosci od srednich

    mean_vector_match = []
    mean_vector_dist = []
    for array_matches in k_matrixes_to_match:
        mean_vector_match.append(array_matches.mean(0))
    for array_dist in k_matrixes_to_dist:
        mean_vector_dist.append(array_dist.mean(0))
    # print(mean_vector_match)

    # main loop
    for test_index in range(0, len(test_list[0])):
        test_point = get_point(test_list, dimension, test_index)
        distances_from_match = calculate_distances(test_point, mean_vector_match)
        distances_from_dist = calculate_distances(test_point, mean_vector_dist)
        match_index = 0
        dist_index = 0
        # print("match: " + str(distances_from_match))
        # print("Dist: " + str(distances_from_dist))
        for i in range(0, k):
            if(distances_from_match[match_index] <= distances_from_dist[dist_index]):
                match_index += 1
            else:
                dist_index += 1
        # print("match: " + str(match_index) + " Not match: " + str(dist_index))
        if match_index > dist_index:
            correctly_recognized += 1

    return correctly_recognized, amount_of_test
