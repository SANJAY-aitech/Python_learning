def N_even_number_reverse(n):
    for i in range(n,1,-1):
       if i%2==0:
           print(i,end=" ")

Number = int(input("Enter the Number: "))
N_even_number_reverse(Number)