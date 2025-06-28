import numpy as np

arr = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr)
print(arr.shape)
 
 #2d to 1d
arr1=arr.reshape(-1)
print(arr1)
print(arr1.shape)


arr2=arr.ravel()
print(arr2)
print(arr2.shape)


#reverse
arr3 = np.array([1, 2, 3, 4, 5])
print(arr3)
arr4 = np.flip(arr3)
print(arr4)
