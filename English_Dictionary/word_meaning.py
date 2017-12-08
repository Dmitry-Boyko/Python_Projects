import json
from difflib import get_close_matches()

data = json.load(open('EnglishWordDictionary.json'))

def translate(w):
    w = w.upper()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no.") % get_close_matches(w, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist. Plesae double check it."
        else:
            return "We didn't understand your query"
    else:
        return 'The word doesn\'t exist. Please double check it.'

word = input('Enter word: ')

# next print will show a list
print(translate(word))
print '\n'
# next print line will show a string
output = translate(word)

for item in output:
    print(item)