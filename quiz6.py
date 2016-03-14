# Write a function named list_to_tuples that receives a two dimensional list of strings as parameter and
# returns a tuple of tuples where the content of each inner list is reversed as shown below:
# For example if the two dimensional list received by the function is

# [['mean', 'really', 'is', 'jean'],
# ['world', 'my', 'rocks', 'python']]
# Then, your function should return a tuple of tuples as shown below:
# (('jean', 'is', 'really', 'mean'), ('python', 'rocks', 'my', 'world'))

def list_to_tuples(instr2d):
    outlist = []
    for rlist in instr2d:
        rlist.reverse()
        outlist.append(tuple(rlist))
    outtup = tuple(outlist)
    return (outtup)

# Write a function named calculate_grades that receives a file name. The file contains names of
# students and their grades for 4 quizzes and returns a tuple as specified below.
# Each line of the file will have the following format:

# name,quiz1_score,quiz2_score,quiz3_score,quiz4_score
# For example if the contents of the file are:
# john,89,94,81,97
# eva,40,45,65,90
# joseph,0,0,54,99
# tim,73,74,89,91
# The name and grades are separated by commas. Your function should return the names of the
# student and their quiz averages as a tuple of tuples as shown below:
# (('eva', 60.0), ('john', 90.25), ('joseph', 38.25), ('tim', 81.75))
# The tuples should be sorted in ascending order by the student's name.

def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dict = {}
    namelist = []
    rowlist = []
    sublist = []
    outlist = []

    for row in data:
        rowlist = row.split(',')
        namelist.append(rowlist[0])
        avg = (int(rowlist[1])+int(rowlist[2])+int(rowlist[3])+int(rowlist[4]))/4
        my_dict[rowlist[0]] = avg
    namelist.sort()
    #print (namelist)

    for name in namelist:
        sublist = []
        sublist.append(name)
        sublist.append(my_dict[name])
        outlist.append(tuple(sublist))
        #print (outlist)

    outtup = tuple(outlist)
    #print (outtup)
    return (outtup)

# Write a function named formatted_print that receives a dictionary as argument.
# The keys of the dictionary will be the names of the students and the values of the
# dictionary will be their average scores. Your function should print this information exactly
# as specified below :

# For example if the dictionary received by the function is

# {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}
# Then your function should print:
# alex       90.55
# eva        88.50
# tim        65.90
# john       34.48
# Note:
# The names have to be accommodated within 10 spaces and they are left justified.
# The scores are floats and they should be right justified in 6 spaces with two digits after the decimal point.
# All this information has to be sorted (descending order) by the scores of the students.
# Notice how alex has the highest score and appears first and john has the lowest score and appears last.

def formatted_print(my_dictionary):
    keylist = my_dictionary.keys()
    vlist = list(my_dictionary.values())
    vlist.sort(reverse=True)
    #print (vlist)
    for item in vlist:
        for key in keylist:
            if my_dictionary[key] == item:
                print ("{0:<10s}{1:>6.2f}".format(key, item))

# Write a function named calculate_expenses that receives a filename as argument.
# The file contains the information about a person's expenses on items. Your function should
# return a list of tuples sorted based on the name of the items. Each tuple consists of the name
# of the item and total expense of that item as shown below:

# milk,2.35
# bread , 1.95
# chips ,    2.54
# milk  ,    2.38
# milk,2.31
# bread,    1.90

# Notice that each line of the file only includes an item and the purchase price of that item
# separated by a comma. There may be spaces before or after the item or the price.
# Then your function should read the file and return a list of tuples such as:
# [('bread', '$3.85'), ('chips', '$2.54'), ('milk', '$7.04')]
# Notes:
# Tuples are sorted based on the item names i.e. bread comes before chips which comes before milk.
# The total expenses are strings which start with a $ and they have two digits of accuracy
# after the decimal point.
# Hint: Use "${:.2f}" to properly create and format strings for the total expenses.

def calculate_expenses(filename):
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()

    outlist = []
    temp_dict = {}
    for row in data:
        keylist = temp_dict.keys()
        sublist = list(keylist)
        #sublist = []
        templist = row.split(',')
        newitem = templist[0].strip()
        #sublist.append(newitem)
        newitem1 = templist[1].strip()
        #sublist.append(newitem1)
        if sublist.count(newitem) != 0:
            temp_dict[newitem] = temp_dict[newitem] + float(newitem1)
        else:
            temp_dict[newitem] = float(newitem1)
        #print (temp_dict)

    outlist = []
    keylist = temp_dict.keys()
    templist = list(keylist)
    templist.sort()
    for key in templist:
        outsublist = []
        outsublist.append(key)
        outsublist.append("${:.2f}".format(temp_dict[key]))
        outlist.append(tuple(outsublist))
    print (outlist)
    return (outlist)

calculate_expenses('lz6.txt')
#formatted_print({'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900})
#calculate_grades('lz5.txt')
#list_to_tuples([['mean', 'really', 'is', 'jean'],['world', 'my', 'rocks', 'python']])