def sumofnaturalnumbers(n):
    sum = 0
    for i in range(0,n):
        sum = sum + i
    return sum

x = int(input("Enter n:"))
print(sumofnaturalnumbers(x))

# OUTPUT
# Enter n:65
# 2080