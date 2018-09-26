def mul3(n):
    if(n > 1):
        mul3(n-1)
    print(n * 3)
x = int(input("Enter n:"))
mul3(x)

# OuTPUT 
# Enter n:6
# 3
# 6
# 9
# 12
# 15
# 18