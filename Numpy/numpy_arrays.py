import numpy as np
a = np.array([1,2,3,4])
##indexing
print(a[0])
print(a[2])
##slicing

print(a[1:3])
##multi-idexing
print(a[[1,2,-1]])

##array types
b = np.array([1.0,2.0,3.0,4.0])
print(a.dtype)
print(b.dtype)

#Dimensions and shapes
x = np.array([[5,6,7],[4,5,6]])
print(x)

print(x.shape)
print(x.size)
print(x.ndim)

print(x[:,:2])