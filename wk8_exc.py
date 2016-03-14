# Write a function that accepts a filename as input argument and reads the file and
# saves each line of the file as an element in a list (without the new line ("\n")character)
# and returns the list. Each line of the file has comma separated values:
# For example if the content of the file looks like this:
# Lucas,Turing,22
# Alan,Williams,27
# Layla,Trinh,21
# Brayden,Huang,22
# Oliver,Greek,20
# then your function should return a list such as
# ['Lucas,Turing,22', 'Alan,Williams,27', 'Layla,Trinh,21', 'Brayden,Huang,22', 'Oliver,Greek,20']
# Please read the "File I/O Exercise Notes" before you attempt to write code.

def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    datastr = "".join(data)
    #print (datastr)
    dlist = datastr.split('\n')
    return (dlist)

# Write a function that accepts a filename(string) of a CSV file which contains the information
# about student's names and their grades for four courses and returns a dictionary of the information.
# The keys of the dictionary should be the name of the students and the values should be a
# list of floating point numbers of their grades. For example, if the content of the file looks like this:

#Mark,90,93,60,90
#Abigail,84,50,72,75
#Frank,46,83,53,79
#Yohaan,47,77,74,96
#then your function should return a dictionary such as:
#out_dict = {'Frank': [46.0, 83.0, 53.0, 79.0],
#            'Mark': [90.0, 93.0, 60.0, 90.0],
#            'Yohaan': [47.0, 77.0, 74.0, 96.0],
#            'Abigail': [84.0, 50.0, 72.0, 75.0]}

def dict_from_file(file_name):
    inlist = list_from_file(file_name)
    #print (inlist)
    inlen = len(inlist)
    keylist = []
    vallist = []

    for item in inlist:
        #print (item)
        ind = item.index(',')
        keylist.append(item[0:ind])
        nlist = item[ind+1:].split(',')
        newlist = []
        #print (nlist)
        for num in nlist:
            newlist.append(float(num))
        vallist.append(newlist)
    #print (keylist)
    #print (vallist)
    outdict = dict(zip(keylist, vallist))
    return (outdict)

# Write a function that takes a file name (string) of a CSV file which contains the information
# about student's names and their grades for four courses and returns a dictionary that contains
# information about the students whose grades in both Math and Chemistry is above 70.
# Note that if the file has any comments (lines starting with #) then you should ignore such a line.
# The file will have the following format:

#first_name,math,physics,chemistry,biology
#For example if the contents of the file are:
#Luke,89,94,81,97
#Eva,40,50,65,90
#Joseph,55,58,54,99
#Oliver,73,74,89,91
#then your function should return a dictionary such as:
#out_dict = {'Luke': [89.0, 94.0, 81.0, 97.0],
#            'Oliver': [73.0, 74.0, 89.0, 91.0]}

def dict_grade(file_name):
    inlist = list_from_file(file_name)
    #print (inlist)
    inlen = len(inlist)
    keylist = []
    vallist = []

    for item in inlist:
        #print (item)
        ind = item.index(',')

        nlist = item[ind+1:].split(',')
        nlen = len(nlist)
        newlist = []
        print (nlist)
        if int(nlist[0]) > 70 and int(nlist[2]) > 70:
            keylist.append(item[0:ind])
            for i in range(nlen):
                newlist.append(float(nlist[i]))
            vallist.append(newlist)
    #print (keylist)
    #print (vallist)
    outdict = dict(zip(keylist, vallist))
    return (outdict)

# Write a function that accepts a filename as input argument, the file contains the information
# about a persons expenses on milk and bread and returns a dictionary that contains exactly the
# strings 'milk' and 'bread' as the keys and their floating point values in a list as values.
# Each line of the file may start with a 'm' or a 'b' denoting milk or bread respectively.
# For example if the contents of the file are:

#m 0 0 0
#b 2 5 1
#b 3 5 4
#m 1 0 0
#b 5 3 1
#m 0 1 0
#b 2 4 5
#then your function should return a dictionary such as:
#out_dict = {'milk': [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
#            'bread': [[2.0, 5.0, 1.0], [3.0, 5.0, 4.0], [5.0, 3.0, 1.0], [2.0, 4.0, 5.0]]}

def dict_milk_bread(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dictionary = {}
    mlist = []
    blist = []

    for line in data:
        name, c1, c2, c3 = line.strip().split(' ')
        if name == 'm':
            mlist.append([float(c1), float(c2), float(c3)])
        elif name == 'b':
            blist.append([float(c1), float(c2), float(c3)])
        #print (mlist, blist)

    my_dictionary['milk'] = mlist
    my_dictionary['bread'] = blist
    return (my_dictionary)

# Write a function that accepts a file name as input argument and constructs and returns a nested dictionary
# from it. The keys of this dictionary should be last names, and the values should be dictionaries that
# contain first names as the keys and integer ages as the values. Note that the data may contain multiple
# people with the same last name, but it will have unique first names. Ignore any lines that start with '#'
# The file will contain comma separated values (CSV) For example if the contents of the file are:

#first_name,last_name,age
#Matthew,Abbey,65
#Chloe,Orion,49
#Yohaan,Adams,54
#Krishna,Adams,35
#Resa,Orion,86
#Lucas,Abbey,60
#Courtney,Abbey,67
#Joseph,Orion,45
#Mark,Abbey,60
#Eva,Orion,76
#then your function should return a dictionary such as:
#{'Abbey': {'Matthew': 65, 'Courtney': 67, 'Lucas': 60, 'Mark': 60},
# 'Orion': {'Chloe': 49, 'Resa': 86, 'Eva': 76, 'Joseph': 45},
# 'Adams': {'Krishna': 35, 'Yohaan': 54}}

def nested(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dictionary = {}
    ndict = {}
    lnlist = list(my_dictionary.keys())

    for line in data:
        if line[0] != '#':
            fname, lname, age = line.strip().split(',')
            if lnlist.count(lname) == 0:
                my_dictionary[lname] = {}
                lnlist.append(lname)
    #print (lnlist)

    for item in lnlist:
        flist = []
        alist = []
        for line in data:
            if line[0] != '#':
                fname, lname, age = line.strip().split(',')
                if lname == item:
                    flist.append(fname)
                    alist.append(int(age))
        print (item, flist, alist)
        my_dictionary[item] = dict(zip(flist, alist))

#    for line in data:
#        ndict = {}
#        if line[0] != '#':
#            fname, lname, age = line.strip().split(',')
#            ndict[fname] = age
            #print (fname, lname, age)
            #print (lname, ndict)
 #           my_dictionary[lname].append(ndict)

    return (my_dictionary)

print (nested('lz4.txt'))
#print (dict_milk_bread('lz3.txt'))
#print (dict_grade('lz2.txt'))
#print (dict_from_file('lz1.txt'))



