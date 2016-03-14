## Write a function that accepts a string of words separated by spaces
## consisting of alphabetic characters and returns a string such that
## each word in the input string is reversed while the order of the words
## in the input string is preserved. Capitalization does matter here.
## The length of the input string must be equal to the length of the
## output string i.e. there should be no trailing or leading spaces
## in your output string.

def _rev(instr):
    inlist = instr.split()
    newlist = []
    outstr = ""
    s = " "
    for item in inlist:
        l = len(item)
        newitem = ""
        for i in range (0, l):
            newitem = item[i]+newitem
        newlist.append(newitem)

    outstr=s.join(newlist)
    return (outstr)

print (_rev("this is a sample test"))
