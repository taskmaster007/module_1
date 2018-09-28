f = open("rhyme.txt","r")
fd = f.read()
fd = fd.lower().split()
wd = {}
for i in fd:
    if(i in wd.keys()):
        wd[i] = wd[i] + 1
    else:
        wd[i] = 1
f.close()
f = open("words.txt","w")
f.write("Unique words: "+str(len(wd))+"\nTotal Words: "+str(len(fd))+"\nUnique words with number of occurences: "+str(wd))