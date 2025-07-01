#(5),(6),(7)
import numpy as np

arr1=np.array([3,4])
arr2=np.array([1,0])

avg=(arr1+arr2)/2

print("avg : ",avg)

mean1 = np.mean(arr1, axis=0)
print("Mean 1 :", mean1)

median1 = np.median(arr1, axis=0)
print("Median 1 :", median1)

mean2 = np.mean(arr2, axis=0)
print("Mean 2 :", mean2)

median2 = np.median(arr2, axis=0)
print("Median 2: ", median2)

