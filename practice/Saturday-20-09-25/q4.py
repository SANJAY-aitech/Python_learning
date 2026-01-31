n = 20092025
arr = []

while n > 0:
    n2 = n%10
    arr.append(n2) #arr = arr+n
    n = n//10
# print(arr)
print("3rd:",arr[-3],"4th:",arr[-4])