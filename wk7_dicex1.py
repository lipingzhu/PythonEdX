# Write a function that accepts a dictionary as input and returns a sorted list of all the keys
# in the dictionary.

def sorted(dict):
    slist = list(dict.keys())
    slist.sort()
    return (slist)

# Write a function that accepts a dictionary as input and returns a sorted list of all the
# values in the dictionary. Assume that the values of this dictionary are just integers.

def sortvalue(dict):
    vlist = list(dict.values())
    vlist.sort()
    return (vlist)

# Write a function that accepts a dictionary as input which contains the names and grades of students
# (The keys are student names and the values are lists of grades for 3 exams (1 Dimensional list))
# and returns the list of names for those students whose grade on all three exams is greater than
# or equal to 78.

def namelist(dict):
    nlist = list(dict.keys())
    glist = list(dict.values())
    nlen = len(nlist)
    outlist = []

    for i in range(nlen):
        good = True
        grade = glist[i]
        # print (grade)
        glen = len(grade)
        for j in range(glen):
            if grade[j] < 78:
                good = False
                break
        if good == True:
            outlist.append(nlist[i])

    return (outlist)

# Write a function which accepts a dictionary and an integer as input and returns an ascending
# sorted list of all the keys whose values contain the input value. Note that the keys of this
# dictionary are strings while the values of this dictionary are 1 Dimensional lists of integers.

def sortlist(dict,val):
    nlist = list(dict.keys())
    nlen = len(nlist)
    outlist = []

    for i in range(nlen):
        x = dict.get(nlist[i])
        #print (x)
        if x.count(val) != 0:
            outlist.append(nlist[i])

    outlist.sort()
    return outlist

# Write a function that takes a string as input argument and returns a dictionary of letter counts
# i.e. the keys of this dictionary should be individual letters and the values should be the total
# count of those letters. You should ignore white spaces and they should not be counted as a character.
# Also note that a small letter character is equal to a capital letter character.

def retdict(ins):
    instr = ins.lower()
    inlen = len(instr)
    outkey = []
    outval = []

    for i in range (inlen):
        if outkey.count(instr[i]) == 0 and instr[i]!= " ":
            outkey.append(instr[i])
    #print (outkey)

    for j in outkey:
        outval.append(instr.count(j))
    #print (outval)

    outdict = {}
    #outdict.fromkeys(outkey,"0")
    outdict = dict(zip(outkey, outval))
    #print (outdict)
    return (outdict)

# Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e.
# the keys of this dictionary should be individual vowels and the values should be the total count of those vowels.
# You should ignore white spaces and they should not be counted as a character.
# Also note that a small letter vowel is equal to a capital letter vowel.

def vowdict(ins):
    instr = ins.lower()
    inlen = len(instr)
    vowlist = ['a','e','i','o','u']
    outkey = []
    outval = []

    for j in vowlist:
        x = instr.count(j)
        print (j, x)
        if x != 0:
            outval.append(x)
            outkey.append(j)
    print (outval)
    print (outkey)

    outdict = {}
    outdict = dict(zip(outkey, outval))
    return (outdict)

# Write a function that takes a string of words as input argument and returns a dictionary of word counts.
# The keys of this dictionary should be the unique words and the values should be the total count of those words.
# Assume that characters are not case sensitive.

def cntdict(ins):
    instr = ins.lower()
    inlist = instr.split()
    outkey = []
    outval = []

    for item in inlist:
        if outkey.count(item) == 0:
            outkey.append(item)

    for item in outkey:
        outval.append(inlist.count(item))

    print (outval)
    print (outkey)

    outdict = {}
    outdict = dict(zip(outkey, outval))
    return (outdict)

# Write a function that takes an integer as input argument and returns the integer using words.
# For example if the input is 4721 then the function should return the string "four seven two one".
# Note that there should be only one space between the words and they should be all lowercased
# in the string that you return.

def wordnum(inint):
    instr = str(inint)
    dictnum = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
    leni = len(instr)
    outlist = []
    space = " "
    for i in range(leni):
        x = instr[i]
        y = dictnum.get(int(x))
        print (x, y)
        outlist.append(y)

    outstr = ' '.join(outlist)
    return(outstr)

# Write a function that accepts a string which contains a particular date from the Gregorian calendar.
# Your function should return what day of the week it was. Here are a few examples of what the input string
# (Month Day Year) will look like. However, you should not 'hardcode' your program to work only for these input!
# Note that each item (Month Day Year) is separated by one space. For example if the input string is:
# "May 5 1992"
# Then your function should return the day of the week (string) such as:
# "Tuesday"

# Algorithm with sample example:
# Assume that input was "May 5 1992"
# day (d) = 5        # It is the 5th day
# month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... January = 11, February = 12)
# century (c) = 19   # the first two characters of the century
# year (y) = 92      # Year is 1992 (*** if month is January or february decrease one year)
# Formula and calculation
# day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
# after calculation we get, (w) = 2
# Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, Tuesday = 2, ... Saturday = 6

def dayofweek(gcal):
    import math
    slist = gcal.split()
    dictmon = {'March':1, 'April':2, 'May':3, 'June':4, 'July':5, 'August':6, 'September':7, 'October':8, 'November':9,
               'December':10, 'January':11, 'Feburary':12}
    dow = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    m = int(dictmon.get(slist[0]))
    d = int(slist[1])
    fy = slist[2]
    c = int(fy[0:2])
    y = int(fy[2:])

    if m == 11 or m == 12:
        y = y - 1

    print (m, d, c, y)

    w = (d + math.floor(2.6*m - 0.2) - 2*c + y + y//4 + c//4) % 7
    print (w)
    return (dow.get(w))

# Write a function that takes a 4 digit integer (from 1000 to 9999 both inclusive) as input argument and
# returns the integer using words as shown below:
# Sample Examples:
# if the input integer is 7000 then the function should return the string "seven thousand"
# if the input integer is 1008 then the function should return the string "one thousand eight"
# if the input integer is 4010 then the function should return the string "four thousand ten"
# if the input integer is 1012 then the function should return the string "one thousand twelve"
# if the input integer is 4506 then the function should return the string "four thousand five hundred six"
# if the input integer is 9900 then the function should return the string "nine thousand nine hundred"
# if the input integer is 8880 then the function should return the string "eight thousand eight hundred eighty"
# if the input integer is 5432 then the function should return the string "five thousand four hundred thirty two"
# Notice that the words in the output strings should all be lower cased and separated by only one space and make
# sure your words match the following spellings:
# one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
# sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
# ninety, hundred, thousand

def retwords(instr):
    dicnum = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero',
               10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
               11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    intinp = int(instr)
    outlst = []

    x = intinp // 1000
    outlst.append(dicnum.get(x))
    outlst.append('thousand')
    intinp = intinp - x*1000

    if intinp >= 100:
        x = intinp // 100
        outlst.append(dicnum.get(x))
        outlst.append('hundred')
        intinp = intinp - x*100

    if intinp >= 20:
        x = intinp // 10
        y = x*10
        outlst.append(dicnum.get(y))
        intinp = intinp - y

    if intinp > 0:
        outlst.append(dicnum.get(intinp))

    return (' '.join(outlst))


inp = input ('Please enter an integer between 1 and 9999:')
print (retwords(inp))

#print (dayofweek('January 1 1678'))
#print (wordnum(4721))
#print(cntdict('who let the dogs out?'))
#print(vowdict('who let the dogs out?'))
#print(retdict('aabbccdd'))

#print (sorted({"one":1,"two":2,"three":3}))
#print (sortvalue({"one":1,"two":2,"three":3}))
#print (namelist({"Ashley":[99,80,100],"Jennifer":[100,90,77]}))

sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
#print (sortlist(sample, 2))
