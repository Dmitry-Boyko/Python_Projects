# I found this example very usable
print('"discard" methon for remove particular string value from list\n')

words = ['test', 'many', 'makeword', 'jazz', 'tube'] # list

words = set(words)
for  word in {"MAKEWORD", "Makeword", "makeword"}:
    words.discard(word)
    print words

print('\nAnd now we\'re going to "discard" from set number of \
words("MAKEWORD", "Makeword", "makeword", plus using "replace" some string values from tuple\n')

words = ('test', 'many[br]', 'makeword', 'jazz[br]', 'doc', 'word', 'words') # tuple

words = [w.replace('[br]', '<br />') for w in words]
words = set(words) - {"MAKEWORD", "Makeword", "makeword"}
print words

'''
Also, it possible remove elements with set.remove(), but this method will call KeyError exception 
if deleted element not included in set(list or tuple) 
'''
