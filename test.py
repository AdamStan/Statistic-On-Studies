import numpy as np
import math
from classification import calculate_mean_vectors, calculate_standard_deviation_vetors, calculate_f_in_one_dimension
import unittest

class TestClassification(unittest.TestCase):
    def setUp(self):
        matrix_A = np.array([[3, 2, 2, 1], [2, 3, 0, 7], [-1, 2, 2, -3]])
        matrix_B = np.array([[3, 1, 5], [6, 4, 5], [-1, 3, -2]])
        
        self.matrixes = [
            matrix_A,
            matrix_B
        ]

        self.means_v = [
            matrix_A.mean(1),
            matrix_B.mean(1)
        ]

        self.std_v = [
            matrix_A.std(1),
            matrix_B.std(1)
        ]

        self.f_in_one_dimension = [
            (math.fabs(self.means_v[0].item(0) - self.means_v[1].item(0))) / (self.std_v [0].item(0) + self.std_v [1].item(0)),
            (math.fabs(self.means_v[0].item(1) - self.means_v[1].item(1))) / (self.std_v [0].item(1) + self.std_v [1].item(1)),
            (math.fabs(self.means_v[0].item(2) - self.means_v[1].item(2))) / (self.std_v [0].item(2) + self.std_v [1].item(2))
        ]

    def test_calculating_mean_vectors(self):
        means = calculate_mean_vectors(self.matrixes)
        for i in range(len(self.means_v)):
            for j in range(len(self.means_v[i])):
                self.assertEqual(self.means_v[i].item(j), means[i].item(j))

    def test_calculating_std_vectors(self):
        stds = calculate_standard_deviation_vetors(self.matrixes)
        for i in range(len(self.std_v)):
            for j in range(len(self.std_v[i])):
                self.assertEqual(self.std_v[i].item(j), stds[i].item(j))

    def test_calculating_f_vector(self):
        f_results = calculate_f_in_one_dimension(self.means_v, self.std_v)
        results = list(f_results.values())
        for i in range(len(self.f_in_one_dimension)):
            self.assertEqual(self.f_in_one_dimension[i], results[i])

if __name__ == "__main__":
    unittest.main()


def test_with_example_of_lab1_in_one_dimension():
    """
    deprecated tests
    """
    matrix_A = np.array([[3, 2, 2, 1], [2, 3, 0, 7], [-1, 2, 2, -3]])
    matrix_B = np.array([[3, 1, 5], [6, 4, 5], [-1, 3, -2]])
    
    matrixes = {
        "Matrix A": matrix_A,
        "Matrix B": matrix_B
    }

    means = calculate_mean_vectors(matrixes.values())

    mean_A = matrix_A.mean(1)
    print(mean_A)
    mean_B = matrix_B.mean(1)
    print(mean_B)
    print(means)

    stds = calculate_standard_deviation_vetors(matrixes.values())

    standard_deviation_A = matrix_A.std(1)
    print(standard_deviation_A)
    standard_deviation_B = matrix_B.std(1)
    print(standard_deviation_B)
    print(stds)
    
    if(len(mean_A) != len(mean_B)):
        raise Exception("Amount of rows in matrixes is not the same!")

    f_results = []
    for i in range(len(mean_A)):
        numerator = math.fabs(mean_A[i] - mean_B[i])
        denominator = standard_deviation_A[i] + standard_deviation_B[i]
        f_results.append(numerator / denominator)
    
    print(f_results)
    print(calculate_f_in_one_dimension(means, stds))
