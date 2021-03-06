import numpy as np
import sys
from itertools import combinations
import random
# my functions:
from selection import calculate_f, calculate_sfs
from classification import classification_using_nearest_mean, classification_using_NN


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


def divide_set_and_transpose(matrix, procent_to_training_set):
    training_set = None
    learning_set = matrix
    how_many_to_training = ((int) (len(matrix) * procent_to_training_set * 0.01))
    
    for i in range(0, how_many_to_training):
        random_index = random.randint(0, len(learning_set) - 1)
        # print(random_index)
        if training_set is None:
            training_set = np.array([learning_set[random_index]])
        else:
            training_set = np.append(training_set, [learning_set[random_index]], axis = 0)
        # print(training_set.shape)
        learning_set = np.delete(learning_set, random_index, axis = 0)
        # print(learning_set.shape)

    return np.transpose(learning_set), np.transpose(training_set)


# parameters:
# n - procentes for testing
# selection - Fisher or SFS
# c - number of characteristics
# k - for NN and NM
# classification - NN or NM
# 1. divide on two sets, learning and testing
# 2. characteristics selection
# 3. classification
def main():
    traning_set = 20
    selection = "SFS" # SFS / F
    dimension = 3
    which_algo = "NN" # MN / NN
    k = 3
    # load matrixes from file
    matrixes_dict = load_matrixes()
    matrixes_val = list(matrixes_dict.values())
    
    learning_set1, testing_set1 = divide_set_and_transpose(matrixes_val[0], traning_set)
    learning_set2, testing_set2 = divide_set_and_transpose(matrixes_val[1], traning_set)
    print(learning_set1.shape)
    print(testing_set1.shape)
    print(learning_set2.shape)
    print(testing_set2.shape)
    coordinates = None
    if (selection == "SFS"):
        coordinates = calculate_sfs(learning_set1, learning_set2, dimension)
    elif selection == "F":
        coordinates = calculate_f(learning_set1, learning_set2, dimension)

    if which_algo == "NN":
        print("Uzywam NN")
        dobrze1, calkowita1 = classification_using_NN(learning_set1, learning_set2, testing_set1, coordinates, dimension, k)
        dobrze2, calkowita2 = classification_using_NN(learning_set2, learning_set1, testing_set2, coordinates, dimension, k)
        print("Dopasowanie do macierzy pierwszej (Acer)= " + str(dobrze1 / calkowita1))
        print("Dopasowanie do macierzy drugiej (Quercus)= " + str(dobrze2 / calkowita2))
        print("Łączna skuteczność: " + str((dobrze1 + dobrze2)/(calkowita1 + calkowita2)))
    elif which_algo == "MN":
        print("Uzywam Mean Nearest")
        dobrze1, calkowita1 = classification_using_nearest_mean(learning_set1, learning_set2, testing_set1, coordinates, dimension, k)
        dobrze2, calkowita2 = classification_using_nearest_mean(learning_set2, learning_set1, testing_set2, coordinates, dimension, k)
        print("Dopasowanie do macierzy pierwszej (Acer)= " + str(dobrze1 / calkowita1))
        print("Dopasowanie do macierzy drugiej (Quercus)= " + str(dobrze2 / calkowita2))
        print("Łączna skuteczność: " + str((dobrze1 + dobrze2)/(calkowita1 + calkowita2)))

if __name__ == "__main__":
    main()