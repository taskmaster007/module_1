try:
    f = open("assaignment31text1.txt","r")
    f1 = f.read()
    f2 = f1.replace('"','\\"')
    f.close()
    print("First File:",f1)
except FileNotFoundError:
    print("The file does not exist, it may have been removed")
    f2 = ''
try:
    f = open("assignment31text2.txt","w")
    f.write(f2)
    f.close()
    f = open("assignment31text2.txt","r")
    print("Second File:",f.read())
except FileNotFoundError:
    print("The file does not exist, it may have been removed")

# OUTPUT
# The file does not exist, it may have been removed
# Second File: