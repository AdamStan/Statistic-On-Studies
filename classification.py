import numpy as np
import math

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
            if name in matrixes:
                matrixes[name] = np.append(matrixes.get(name), [numbers], axis = 0)
            else:
                matrixes[name] = np.array([numbers])
            line = file.readline()
        file.close()

    return matrixes

def calculate_mean_vectors(matrixes):
    means = []
    for matrix in matrixes:
        means.append(matrix.mean(1))
    return means

def calculate_standard_deviation_vetors(matrixes):
    standard_deviations = []
    for matrix in matrixes:
        standard_deviations.append(matrix.std(1))
    return standard_deviations

def calculate_f_in_one_dimension(mean_vectors, std_vectors):
    f_results = {}
    for a in range(len(mean_vectors) - 1):
        for i in range(a, len(mean_vectors) - 1):
            for j in range(len(mean_vectors[0])):
                numerator = math.fabs(mean_vectors[i].item(j) - mean_vectors[i+1].item(j))
                denominator = std_vectors[i].item(j) + std_vectors[i+1].item(j)
                f_results[str(a+1) + "|" + str(i+1) + "_" + str(j+1)] = (numerator / denominator)
    
    return f_results

def main():
    matrixes = load_matrixes()
    mean_vecotors = calculate_mean_vectors(matrixes.values())
    std_vectors = calculate_standard_deviation_vetors(matrixes.values())
    f_in_one_dimension = calculate_f_in_one_dimension(mean_vecotors, std_vectors)
    print(mean_vecotors)
    print(std_vectors)
    print(f_in_one_dimension)

if __name__ == "__main__":
    main()