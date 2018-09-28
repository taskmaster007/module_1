f = open("student_details.txt","r")
fd = f.read().splitlines()
fa = [i.split() for i in fd]
print("Storing as List of Lists",fa)
fld = []
for i in fd:
    i = i.split()
    fld.append({i[0]: i[1]})
print("Storing as List of Dictionaries:",fld)

# OUTPUT 
# Storing as List of Lists [['101', 'Rahul'], ['102', 'Julie'], ['103', 'Helena'], ['104', 'Kally']]
# Storing as List of Dictionaries: [{'101': 'Rahul'}, {'102': 'Julie'}, {'103': 'Helena'}, {'104': 'Kally'}]