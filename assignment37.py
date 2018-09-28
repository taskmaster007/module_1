def sumofnaturalnumbers(n):
    sum = 0
    for i in range(0,n):
        sum = sum + i
    return sum

try:
    x = int(input("Enter n:"))
    print(sumofnaturalnumbers(x))
except ValueError:
    print("You should enter a Natural Number")

# OUTPUT
# Enter n:asx
# You should enter a Natural Number