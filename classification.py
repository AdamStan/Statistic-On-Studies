import numpy as np
import sys

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

def write_to_file(path_to_file = "results.txt"):
    pass

def calculate_mean_vector(matrix):
    return matrix.mean(1)

def calculate_f(matrix1, matrix2, dimension=1):
    f_results = {}
    # calculate mean vector
    mean_vector1 = calculate_mean_vector(matrix1)
    print("Mean vector 1:" + str(mean_vector1))
    mean_vector2 = calculate_mean_vector(matrix2)
    print("Mean vector 2:" + str(mean_vector2))
    # calculate f
    for j in range(dimension):
        for i in range(j, len(mean_vector1)):
            # distance between matrix 
            numerator = np.linalg.norm(mean_vector1[i:i + dimension] - mean_vector2[i:i + dimension])
            # sum of standard deviation
            denominator = np.std(matrix1[i:i + dimension]) + np.std(matrix2[i:i + dimension])
            f_results[str(j + 1) + "_" + str(i+1)] = (numerator / denominator)
    
    return f_results

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