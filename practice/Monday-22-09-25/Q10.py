n = 1490
arr = []
while (n>0):
    check = n%10
    arr.append(check)
    n=n//10
unique_arr = list(set(arr))
unique_arr.sort()
print(unique_arr[-2])  
