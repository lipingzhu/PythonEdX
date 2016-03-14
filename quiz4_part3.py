## Write a function named find_longest_word that receives a string as
## parameter and returns the longest word in the string.
## Assume that the input to this function is a string of words consisting
## of alphabetic characters that are separated by space(s). In case of a
## tie between some words return the last one that occurs.

def find_longest_word(instr):
    lword = ""
    llen = 0
    ilist = instr.split()
    for item in ilist:
        if len(item) >= llen:
            llen = len(item)
            lword = item
    return (lword)

print(find_longest_word('this is a joke hahaha'))

            
