def N_odd_number(n):
    sum = 0
    for i in range(1,n+1,2):
        sum =sum+i
    print("Sum of odd numbers b/w 1 to N : ",sum)

Number = int(input("Enter the Number: "))
N_odd_number(Number)