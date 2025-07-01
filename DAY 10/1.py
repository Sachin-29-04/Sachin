#(1)
import numpy as np


arr11= np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])

print(arr11)

arr12=np.nan_to_num(arr11,copy=True,nan=0.0)
print(arr12)


arr13=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr13)
arr14=arr13.T
print(arr14)

#(2)


arr= np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr)
print(" ")
arr[:,:,[0,1]]=arr[:,:,[1,0]]
print(arr)

#(3)

arr1= np.array([[1, np.nan, 3, -4], [np.nan, -8, 0, 2],[7,8,9,5]])

mean=np.nanmean(arr1,axis=0)

ind=np.where(np.isnan(arr1))

arr1[ind]=np.take(mean,ind[1])

print(arr1)