## Write a function which returns the total number of vowels in an input
## string which consists of alphabetic characters. Note that capitalization
## does not matter here i.e. a lower case character should be considered
## the same as an upper case character. For this problem,
## the vowels are considered to be A, E, I, O, U.

def _vowel(instr):
    cnt = 0
    l = len(instr)
    vstr = 'AEIOU'
    for i in range (0, l):
        c = instr[i].upper()
        if vstr.find(c) >= 0:
            cnt = cnt + 1
    return cnt
