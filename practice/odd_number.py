n = 8807639300
check = 0
odd_count = 0
even_count = 0
zero_count = 0
prime_count = 0

while (n>0):
    check = n%10

    if check%2 != 0:
        odd_count+=1
    elif check==0:
        zero_count+=1
    else:
        even_count+=1

    n=n//10

print("Odd digits:", odd_count)
print("Even digits:", even_count)
print("Zero digits:", zero_count)
