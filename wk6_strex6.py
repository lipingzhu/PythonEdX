## Write a function which returns the number of words in the input string
## which have more than 4 characters. Assume that the input string consists
## of alphabetic characters separated by spaces and capitalization
## does not matter i.e. an upper case character should be treated
## the same as a lower case character.

def _cnt(instr):
    cnt = 0
    newlist = instr.split(' ')
    
    for item in newlist:
        if len(item) > 4:
            cnt = cnt + 1

    return (cnt)

    
