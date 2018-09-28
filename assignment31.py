f = open("assignment31text1.txt","r")
f1 = f.read()
f2 = f1.replace('"','\\"')
f.close()
f = open("assignment31text2.txt","w")
f.write(f2)
f.close()
f = open("assignment31text2.txt","r")
print("First File:",f1)
print("Second File:",f.read())

# OUTPUT
# First File: Loki said, "We have a Hulk"
# Thanos says, "Perfectly Balanced, as all things should be"
# Second File: Loki said, \"We have a Hulk\"
# Thanos says, \"Perfectly Balanced, as all things should be\"
