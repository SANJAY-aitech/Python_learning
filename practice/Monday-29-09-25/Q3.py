def N_even_number(n):
    for i in range(2,n+1,2):
        print(i,end=" ")

Number = int(input("Enter the Number: "))
N_even_number(Number)