## Write a function that takes a string consisting of alphabetic characters
## as input argument and returns True if the string is a palindrome.
## A palindrome is a string which is the same backward or forward.
## Note that capitalization does not matter here i.e. a lower case character
## can be considered the same as an upper case character.

def _palin(instr):
    l = len(instr)
    h = l//2
    for i in range(0,h):
        if instr[i].lower() == instr[l-1-i].lower():
            continue
        else:
            return False
    return True

print (_palin('abcdBA'))
