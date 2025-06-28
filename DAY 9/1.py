import numpy as np

#combining 2d and 1d
arr1= np.array([[1, 2],
               [3, 4],
                [5,6]])
print(arr1)
arr2= np.array([7, 8, 9])
print(arr2)

arr3=arr2.reshape(3,1)
print(arr3)
arr4=np.concatenate((arr1,arr3),axis=1)
print(arr4)


