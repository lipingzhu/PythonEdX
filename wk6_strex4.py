## Write a function that accepts a string and a character as input and
## returns the number of times the character is repeated in the string.
## Note that capitalization does not matter here i.e. a lower case character
## should be treated the same as an upper case character.

def _num(instr, inchr):
    newstr = instr.upper()
    newchr = inchr.upper()
    cnt = newstr.count(newchr)
    return (cnt)
