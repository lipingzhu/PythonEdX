## Write a function which accepts an input string and returns a string
## where every individual word in the input string is reversed and
## the case for every single character is reversed.
## The input string for this function would be a sentence
## (words separated by spaces) consisting of alphabetic characters.

def _rev(instr):
    l = len(instr)
    outstr = ""
    for i in range(0,l):
        outstr = instr[i]+outstr
    
    outstr = outstr.swapcase()
    return (outstr)

print (_rev("Hello World"))
