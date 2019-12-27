import numpy as np
import sys
from itertools import combinations

def wspolczynnik_F_in_one_(matrix1, matrix2):
    """
    returns matrix of F wspolczynnikow
    """
    pass

def load_matrixes(path_to_file = "Maple_Oak.txt"):
    matrixes = {}
    with open(path_to_file) as file:
        # skip first line
        line = file.readline()
        # read correct line
        line = file.readline()
        while line:
            line = line.replace('\n', '').split(',')
            name = line[0]
            numbers = line[1:]
            for i in range(len(numbers)):
                numbers[i] = float(numbers[i])
            name = name.split()[0]
            if name in matrixes:
                matrixes[name] = np.append(matrixes.get(name), [numbers], axis = 0)
            else:
                matrixes[name] = np.array([numbers])
            line = file.readline()
        file.close()

    return matrixes

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

def write_to_file(path_to_file = "results.txt"):
    pass

def calculate_mean_vector(matrix):
    return matrix.mean(1)

def calculate_f(matrix1, matrix2, dimension=1):
    f_results = {}
    # calculate mean vector
    all_combinations = calculate_combinations(len(matrix1),dimension)
    mean_vector1 = calculate_mean_vector(matrix1)
    mean_vector2 = calculate_mean_vector(matrix2)
    
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

    return f_results

def calculate_sfs(matrix1, matrix2, dimension=1):
    f_results = {}
    # calculate mean vector
    mean_vector1 = calculate_mean_vector(matrix1)
    mean_vector2 = calculate_mean_vector(matrix2)
    

def main():
    # load parameters (dimension and SFS or F)
    # 1 = F, 2 = SFS
    dimension = int(sys.argv[1])
    # which_method = sys.argv[2]
    # load matrixes from file
    matrixes_dict = load_matrixes()
    matrixes_val = list(matrixes_dict.values())
    f_in_one_dimension = calculate_f(matrixes_val[0], matrixes_val[1], dimension)
    print(f_in_one_dimension)


if __name__ == "__main__":
    main()