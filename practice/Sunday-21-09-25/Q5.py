n = 8807639300
odd_count = 0
even_count = 0
while (n>0):
    check = n%10

    if check%2 != 0:
        odd_count+=1
    else:
        even_count+=1

    n=n//10

print("Odd digits:", odd_count)
print("Even digits:", even_count)
