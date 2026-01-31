n = int(input("Enter a number: ")) #Constraints  15>N>0
even_num = []
odd_num = []
if n<=15:
    for i in range (1,n+1):
        if i%2==0:
            even_num.append(i)
        else:
            odd_num.append(i)

    print("even_numbers: ",even_num)
    print("odd_number: ",odd_num)
else:
    print("n shoulb be less than or equal to 15")
