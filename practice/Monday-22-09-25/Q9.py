def Largest_digit(n):
    large = 0
    while n > 0:
        digit = n % 10
        if digit > large:
            large = digit
        n //= 10
    return large


number = int(input("Enter the Number: "))
res = Largest_digit(number)
print("Largest digit in Given Number is:", res)
