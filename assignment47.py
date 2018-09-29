def count_words(s):
    s = s.split()
    end_with = 0
    in_word = 0
    for i in s:
        if(i[-1:] == '.' or i[-1:] == ','):
            i = i[:-1]
        if(i[-2:] == 'on'):
            end_with+=1
        i = i[1:-1]
        if 'on' in i:
            in_word+=1
    return([end_with,in_word])
my_string = "Strings are amongst the most popular data types in Python. We can create the strings by enclosing characters in quotes. Python treats single quotes the same as double quotes."
cnt = my_string.lower().count('string')
print("Number of Occurences of 'string':",cnt)
x = count_words(my_string)
print("Words ending with 'on':",x[0])
print("Words with 'on' in between first and last letters:",x[1])

# OUTPUT 
# Number of Occurences of 'string': 2
# Words ending with 'on': 2
# Words with 'on' in between first and last letters: 1

