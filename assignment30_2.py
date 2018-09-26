def revstr(i):
    print(str[i],end='')
    if(i > 0):
        revstr(i-1)
str = input("enter a string:")
print("Original:",str)
print("Reverse:",end=" ")
revstr(len(str)-1)
print("")

# OUTPUT
# enter a string:harshal
# Original: harshal
# Reverse: lahsrah