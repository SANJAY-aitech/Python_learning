def count_zeros(n):
    s_n = str(n)     
    zero = 0

    for ch in s_n:
        if ch == '0':
            zero += 1

    if zero == 0:
        return -1     
    else:
        return zero   



n = int(input("Enter the number: "))
result = count_zeros(n)
print(result)
