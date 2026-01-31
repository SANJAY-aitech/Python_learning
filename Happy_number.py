def happy_number(n):
    sq_sum = 0
    while n>0:
        num1 = n%10
        sq_sum = num1*num1
        num1 = n//10
        n = num1
    return sq_sum