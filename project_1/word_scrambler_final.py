import random
inputfile = input("Enter Filename:")
with open(inputfile,'r+') as f:
    file_data = f.read()
words = file_data.split()
scrambled_words = []
for word in words:
    if(len(word) > 3):
        p = word[len(word)-1]
        if(p == ',' or p == '.' or p == ';' or p == '!' or p == '?'):
            word = word[:len(word)-1]
        else:
            p = ''
        middle_letters = word[1:len(word)-1]
        middle_letters = list(middle_letters)
        random.shuffle(middle_letters)
        final = word[0] + ''.join(middle_letters) + word[len(word)-1] + p
        scrambled_words.append(final)
    else:
        scrambled_words.append(word)
inputfile = inputfile.split('.')[0] + 'Scrambled.' + inputfile.split('.')[1]
with open(inputfile,'w') as f:
    f.write(' '.join(scrambled_words))
    f.write('\n')
print("Scrambled Words written in",inputfile)
