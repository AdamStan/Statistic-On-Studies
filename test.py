import numpy as np
import math
from selection import calculate_f, calculate_sfs
from main import divide_set_and_transpose
import unittest

class TestSelection(unittest.TestCase):
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

        self.f_in_two_dimensions = [0.7402156063447579, 0.30000000000000004, 0.15973377703826958]

    def test_calculating_f_vector_one_dimension(self):
        f_result = calculate_f(self.matrixes[0], self.matrixes[1], 1)
        # print(f_result)
        self.assertEqual(f_result, (1,))

    def test_calculating_f_vector_two_dimension(self):
        f_result = calculate_f(self.matrixes[0], self.matrixes[1], 2)
        # print(f_result)
        self.assertEqual(f_result, (0,1))

    def test_calculating_sfs_in_one_dimension(self):
        sfs_resullt = calculate_sfs(self.matrixes[0], self.matrixes[1], 1)
        # print(sfs_resullt)
        self.assertEqual(sfs_resullt, (1,))

    def test_calculating_sfs_in_two_dimension(self):
        sfs_resullt = calculate_sfs(self.matrixes[0], self.matrixes[1], 2)
        # print(sfs_resullt)
        self.assertEqual(sfs_resullt, (0,1))

class TestMainHelpFunctions(unittest.TestCase):

    def setUp(self):
        self.matrix1 = np.array([
            [1, 2, 3, 4,  5], #1
            [6, 7, 8, 9, 10], #2
            [11,12,13,14,15], #3
            [16,17,18,19,20], #4
            [21,22,23,24,25], #5
            [26,27,28,29,30], #6
            [31,32,33,34,35], #7
            [36,37,38,39,40], #8
            [41,42,43,44,45], #9
            [51,52,53,54,55] #10
        ])

    def test_divade_set(self):
        learning_set, training_set = divide_set_and_transpose(self.matrix1, 20)
        self.assertEqual(learning_set.shape, (5,8))
        self.assertEqual(training_set.shape, (5,2))


if __name__ == "__main__":
    unittest.main()