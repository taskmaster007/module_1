n = int(input("Enter a number:"))
a = 0
b = 1
print(a,b,end=" ")
for i in range(0,n):
    print(a+b,end=" ")
    c = b
    b = a + b
    a = c
print("")

# OUTPUT
# Enter a number:8
# 0 1 1 2 3 5 8 13 21 34