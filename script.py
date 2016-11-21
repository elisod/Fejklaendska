fej = "ur"

original = raw_input('Enter a word: ')

word = original.lower()

if len(original) > 0 and original.isalpha() and word:
    print word
else:
    print: 'empty'
        
first = word[0]

new_word = word[1:] + first + fej
    print: new_word
        
