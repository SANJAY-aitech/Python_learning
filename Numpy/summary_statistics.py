import numpy as np

a = np.array([[1,2,3,4],[4,5,6,7]])

print(a.sum())
print(a.mean())
print(a.std())
print(a.var())

print(a.sum(axis=0))
print(a.sum(axis=1))