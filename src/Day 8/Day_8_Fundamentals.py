import numpy as np
a = np.array([[1,2,3],
             [4,5,6]])
b = np.array([10,20,30])
result = a+b
print(result)

#dimensions
print("1-Dimension")
a1 = np.array([1, 2, 3])
print(a1)

print("0-Dimension")
a0 = np.array(5)
print(a0)

print("Two-Dimension")
a2 = np.array([[4, 5, 6],
               [8, 9, 10],
               [1, 2, 3]])
print(a2)

#vectorization
arr = np.random.rand(10)
# Vectorized
squared = arr ** 2
print(arr)
print(squared)

#reshaping
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])
vstacked = np.vstack((a, b))
print(vstacked)
hstacked = np.hstack((a,b))
print(hstacked)

#statistical functions
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
#column wise mean
print(np.mean(data, axis=0))
#row wise mean
print(np.mean(data, axis=1))

#linear algebra
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.dot(A, B))

