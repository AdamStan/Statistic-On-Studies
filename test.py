import numpy as np
import math
from classification import calculate_f
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

    def test_calculating_f_vector_one_dimension(self):
        print("TEST - calculating f in one dimension")
        f_results = calculate_f(self.matrixes[0], self.matrixes[1], 1)
        results = list(f_results.values())
        print(self.f_in_one_dimension)
        print(results)
        for i in range(len(self.f_in_one_dimension)):
            self.assertEqual(self.f_in_one_dimension[i], results[i], msg=str(i))

    # def test_calculating_f_vector_two_dimension(self):
    #     print("TEST - calculating f in one dimension")
    #     f_results = calculate_f(self.matrixes[0], self.matrixes[1], 1)
    #     results = list(f_results.values())
    #     print(self.f_in_one_dimension)
    #     print(results)
    #     for i in range(len(self.f_in_one_dimension)):
    #         self.assertEqual(self.f_in_one_dimension[i], results[i], msg=str(i))


if __name__ == "__main__":
    unittest.main()