from classification import divide_on_k_matrixes
import numpy as np

matrix_to_devide = np.array([
    np.array([-7, 5]),
    np.array([-5, 3]),
    np.array([-6, 1]),
    np.array([-5, -3]),
    np.array([2, 2]),
    np.array([3, 2]),
    np.array([8, 5]),
    np.array([10, -4])
])

result = divide_on_k_matrixes(matrix_to_devide, 3)
print(result)