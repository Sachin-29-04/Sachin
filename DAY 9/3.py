import numpy as np


arr= np.array([[45, 76, 36], [27, 59, 69]])

# min value
max_value = np.max(arr)
print( max_value)

# max value
min_value = np.min(arr)
print(min_value)

#rows and column
print(arr.shape)

#selecting elements
for x in np.nditer(arr) :
    print(x)

print(" ")
print(arr[0,1])
print(arr[-1,-2])

print(" ")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

#sum of elements using for loop
sum = 0
for row in arr1:
    for x in row:
        sum += x

print(sum)

#arthmetic operations
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[10, 20, 30], [40, 50, 60]])


result= arr2 + arr3
print(result)

print("  ")
result= arr3 - arr2
print(result)

print(" ")

result = arr2 * arr3
print(result)

print(" ")

result = arr3 / arr2
print(result)