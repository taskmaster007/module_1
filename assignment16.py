str = input("Enter a String:")
str = str.lower()
s = str[::-1]
if(str == s):
    print("It's a Palindrome")
else:
    print("It's not a palindrome")
print("Original String:",str)
print("Reverse String:",s)

# OUTPUT
# Enter a String:BookooB
# It's a Palindrome
# Original String: bookoob
# Reverse String: bookoob