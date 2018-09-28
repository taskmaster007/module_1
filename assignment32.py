f = open("courses.txt","r")
fd = f.read()
fa = fd.splitlines()
print("Storing as a List:",fa)
fdictionary = {}
for i,d in enumerate(fa):
    fdictionary[i] = d
print("Storing as a dictionary:",fdictionary)

# OUTPUT
# Storing as a List: ['Java', 'Python', 'Javascript', 'PHP']
# Storing as a dictionary: {0: 'Java', 1: 'Python', 2: 'Javascript', 3: 'PHP'}