# #Square
for i in range(0,4):
    for j in range(0,4):
        print("*",end=" ")
    print()

# #UPPER RIGHT ANGLED Triangle
for i in range(0,6):
    for j in range(i):
        print("*",end=" ")
    print()
print("====================================")
#LOWER RIGHT ANGLED TRIANGLE
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()