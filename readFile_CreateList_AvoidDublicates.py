fh = open('romeo.txt')
lines = fh.readlines()      # reading lines
words = list()              # create list
for line in lines:
    line_words = line.split(" ")  
    for line_word in line_words:
        word = line_word.lstrip().rstrip()
        if word != "" and word not in words:    #add word to list
            words.append(word)
#print words
words.sort()                # sorting
print words
fh.close()
