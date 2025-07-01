#(4)

import numpy as np

arr=np.array([[5,-1,8],[-9,4,-3]])

print(arr)
print(" ")
arr[arr<0]=0
print(arr)
print(" ")



#(8)

a = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])

b = np.array([9, -6, 17])

print(a)
print("")
print(b)

solution = np.linalg.solve(a, b)
print(solution)

print(" ")

inv = np.linalg.inv(a)

print(inv)

