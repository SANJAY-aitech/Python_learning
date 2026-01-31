# def Start_and_Last_Digit(n):
#     l = n % 10
#     last = l
#     while n >= 10:
#         n = n//10
#         first = n
#     print("First: ",first,"Last: ",last)
# Start_and_Last_Digit(1)#Enter digit greater than 10

n = 2345
arr = []

while n > 0:
    n2 = n%10
    arr.append(n2) #arr = arr+n
    n = n//10
print(arr)
print("First_digit:",arr[len(arr)-1],"Last_digit: ",arr[0])