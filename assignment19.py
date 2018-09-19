accepted_string = input("Enter a String:")
resultant_string = ""
accepted_string = accepted_string.replace(" ",'')
for i in range(0,len(accepted_string)):
    if(i%2==0):
        resultant_string = resultant_string + accepted_string[i]
print(resultant_string[::-1])

# OUTPUT
# Enter a String:Hey Brother Do you still believe in one another
# rhoanneelbltuyDetryH 