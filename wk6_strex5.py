## Write a function that accepts a string and a character as input and
## returns the count of all the words in the string which start with the
## given character. Assume that capitalization does not matter here.
## You can assume that the input string is a sentence i.e.
## words are separated by spaces and consists of alphabetic characters.

def _cnt(instr, inchr):
    cnt = 0
    newlist = instr.split(' ')
    newchr = inchr.upper()
    
    for item in newlist:
        newitem = item.upper()
        if newitem[0] == newchr:
            cnt = cnt + 1

    return (cnt)

    
