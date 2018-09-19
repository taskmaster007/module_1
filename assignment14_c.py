n = int(input("Enter a number:"))
flag = 0
for i in range(2,n):
    if(n%i == 0):
        flag = 1
        break

if(flag == 0):
    print(n,"is Prime")
else:
    print(n,"is not Prime")


# OUTPUT
# Enter a number:65
# 65 is not Prime
# Enter a number:17
# 17 is Prime