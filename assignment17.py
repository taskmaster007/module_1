string1 = input("Enter String 1:")
string2 = input("Enter String 2:")
result = ""
for i in string1:
    if i.isupper():
        result = result + i
for i in string2:
    if i.isupper():
        result = result + i
print("String 1:",string1)
print("String 2:",string2)
print("Result:",result)

# OUTPUT
# Enter String 1:He Is My Good Friend
# Enter String 2:Popeye The Sailor Man
# String 1: He Is My Good Friend
# String 2: Popeye The Sailor Man
# Result: HIMGFPTSM