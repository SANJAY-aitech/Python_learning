#Swapping three  numbers without using temp variable
a = 43
b = 20
c = 1
print("Before Swapping")
print("a =",a,"b = ",b,"c = ",c)

a= a+b
b= a-b
a = a-b

b = b+c
c= b-c
b=b-c
print("After Swapping")
print("a = ",a,"b = ",b,"c = ",c)