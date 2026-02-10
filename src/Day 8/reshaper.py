import numpy as np


arr1d = np.arange(24)


arr3d = arr1d.reshape(4, 3, 2)


arr_transposed = arr3d.transpose(0, 2, 1)


print("Final Shape:", arr_transposed.shape)
print("Final Array:")
print(arr_transposed)
