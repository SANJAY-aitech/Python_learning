str = input("Enter the String: ")
count = 0
for i in str.strip():
    count+=1
print(count)

for i in range(count-1, -1, -1):
    rev = str[i]
    print(rev,end="")