string = input("Enter a string:")
string = string.lower()
r = {}
for i in string:
    if i in r.keys():
        r[i]+=1
    else:
        r[i] = 1
for key, value in r.items():
    print(key,value)

# OUTPUT

# Enter a string:ASaaPoollksklaa
# a 5
# s 2
# p 1
# o 2
# l 3
# k 2