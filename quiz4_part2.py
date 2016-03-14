## Write a function named count_consonants that receives a string as
## parameter and returns the total count of the consonants in the string.
## Consonants are all the characters in the english alphabet
## except for 'a', 'e', 'i', 'o', 'u'. If the same consonant repeats multiple
## times you should count all of them. Note that capitalization and
## punctuation does not matter here i.e. a lower case character should be
## considered the same as an upper case character.

def count_consonants(instr):
    cnt = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(instr)):
        if vowel.count(instr[i].lower()) != 0:
            continue
        if instr[i] == " ":
            continue
        cnt = cnt + 1
    return cnt

print (count_consonants('Hercules was a hero'))
