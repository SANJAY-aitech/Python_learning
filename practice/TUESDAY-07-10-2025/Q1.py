n = 8807639300
three = []
four = []
while n>0:
    num = n%10

    if (num%3==0) and (num!=0):
        three.append(num)
    elif (num%4==0) and (num!=0):
        four.append(num)
    else:
        pass
    n=n//10
print("Divisble by 3 : ",three)
print("Divisble by 4 : ",four)
