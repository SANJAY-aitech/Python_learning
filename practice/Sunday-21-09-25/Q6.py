#Square of the each integer 
n = int(input("Enter the number: "))
while (n>0):
    check = n%10
    print(check*check,end=",")
    n=n//10
