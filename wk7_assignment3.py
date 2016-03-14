# Write a function named find_word_horizontal that accepts a 2-dimensional list of characters
# (like a crossword puzzle) and a string (word) as input arguments. This function searches
# the rows of the 2d list to find a match for the word. If a match is found, this functions
# returns a list containing row index and column index of the start of the match,
# otherwise it returns the value None (no quotations).
# For example if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# find_word_horizontal(crosswords,word)
# then your function should return
# [2,1]
# Notice that the 2d input list represents a 2d crossword and the starting index of the horizontal word 'cat' is [2,1]
# Note: In case of multiple matches only return the match with lower row index.
# If you find two matches in the same row then return the match with lower column index.

def find_word_horizontal(list2d, instr):
    outlist = []
    sep = ""
    rownum = len(list2d)

    for i in range(rownum):
        rowlst = list2d[i]
        rowstr = sep.join(rowlst)
        #print (rowstr)
        if rowstr.count(instr) > 0:
            outlist.append(i)
            outlist.append(rowstr.index(instr))
            return (outlist)
    return None

# Write a function named find_word_vertical that accepts a 2-dimensional list of characters
# (like a crossword puzzle) and a string (word) as input arguments. This function searches the
# columns of the 2d list to find a match for the word. If a match is found, this functions
# returns a list containing row index and column index of the start of the match,
# otherwise it returns the value None (no quotations).

def find_word_vertical(list2d, instr):
    col = len(list2d[0])
    row = len(list2d)
    outlist = []
    for i in range(col):
        outstr = ""
        for j in range(row):
            outstr = outstr+list2d[j][i]
        #print (outstr)
        if outstr.count(instr) > 0:
            outlist.append(outstr.index(instr))
            outlist.append(i)
            return (outlist)
    return None

# Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of characters
# (like a crossword puzzle) and a string (word) as input arguments. This function searches the rows and
# columns of the 2d list to find a match for the word. If a match is found, this functions capitalizes
# the matched characters in 2-dimensional list and returns the list. If no match is found, this function
# simply returns the origianl 2-dimensional list with no modification.

def capitalize_word_in_crossword(list2d, instr):
    inlen = len(instr)
    rowlist = []

    rowlist = find_word_horizontal(list2d, instr)
    if rowlist != None:
        x = rowlist[0]
        y = rowlist[1]
        for i in range(inlen):
            list2d[x][y+i] = list2d[x][y+i].upper()
            print (list2d[x][y+i])
        return (list2d)

    collist = find_word_vertical(list2d, instr)
    if collist != None:
        x = collist[0]
        y = collist[1]
        for i in range(inlen):
            list2d[x+i][y] = list2d[x+i][y].upper()
            print (list2d[x+i][y])
        return (list2d)

    return (list2d)

print (capitalize_word_in_crossword([['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']],'cat'))
#print (find_word_vertical([['a', 'b'], ['c', 'd']], 'b'))
#print (find_word_vertical([['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']],'cat'))
#print (find_word_horizontal([['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']],'cat'))



