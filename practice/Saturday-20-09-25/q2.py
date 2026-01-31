n = 244532
arr = []

while n > 0:
    n2 = n%10
    arr.append(n2) #arr = arr+n
    n = n//10
# print(arr)
print(arr[-2])