def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
# print (my_fun(y))

# Write a function named n_letter_dictionary that receives a string (words separated by spaces)
# as parameter and returns a dictionary whose keys are numbers and whose values are lists that
# contain unique words that have the number of letters equal to the keys.

# For example, when your function is called as:

# n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become")
# Then, your function should return a dictionary such as
# {2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'],
# 5: ['treat'], 6: ['become', 'people']}
# Notes:
# Each list of words with the same number of letters should be sorted in ascending order
# The words in a list should be unique. For example, even though the word "them" is repeated twice
# in the above sentence, it is only considered once in the list of four letter words.
# Capitalization does not matter, this means that all the words should be converted to lower case.
# For example the words "The" and "the" appear in the sentence but they are both considered as lower case "the".
# Do NOT import any module for solving this problem.

def n_letter_dictionary(my_string):
    my_dict = {}
    my_string = my_string.lower()
    my_list = my_string.split(' ')
    keylist = list(my_dict.keys())

    for item in my_list:
        item_len = len(item)
        if keylist.count(item_len) == 0:
            vallist = []
            keylist.append(item_len)
            vallist.append(item)
        else:
            vallist = list(my_dict[item_len])
            #print (vallist)
            if vallist.count(item) == 0:
                vallist.append(item)
        vallist.sort()
        my_dict[item_len] = vallist
        #print (my_dict)

    return (my_dict)

#n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become")

# Write a function named my_final_grade_calculation that receives a file name and returns a dictionary
# that tells whether a student in this course passed or failed based on the following criteria.

# Each line of the file will have the format:

# name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final
# where
# name is a string
# q1 through q6 are quiz scores (integers)
# a1 through a4 are assignment scores (integers values)
# midterm is midterm score (integer)
# final is final exam score (integer)
# For example, if the content of the file looks like this:
# tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85
# mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
# joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5
# Note that there may be additional spaces between the entries in each line.

# Your function should return a dictionary such as:
# {"tom":"pass", "mary":"pass", "joan":"fail"}
# Notes:
# Two of the lowest quizzes should be dropped and the average of the remaining
# four quizzes is worth 25% of the total grade.
# The lowest assignment score should be dropped and the average of the remaining
# three assignments is worth 25% of the total grade.
# Midterm and final exams are each 25% of the total grade.
# Calculate the total score of the student and if the total score is greater than or equal to 60
# (totalscore >= 60) then the student has passed. Notice that the keys (names) and the values (pass or fail)
# of the dictionary should be all lower cased with no spaces in any of them.
# Do NOT import any module for solving this problem.

def my_final_grade_calculation(filename):
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()

    my_dict = {}
    keylist = []
    for row in data:
        slist = row.split(',')
        totalscore = 0
        key = slist[0].strip()
        firstminval = 101
        score = 0
        for i in range(1,7):
            ints = int(slist[i])
            score = score + ints
            if ints < firstminval:
                firstminval = ints
                minind = i
        score = score - firstminval

        secondminval = 101
        for i in range(1,7):
            ints = int(slist[i])
            if (ints < secondminval) and (i != minind):
                secondminval = ints
        score = score - secondminval

        weightedquizscore = score/4.0*0.25
        #print (score, weightedquizscore)

        assminval = 101
        assscore = 0
        for i in range(7,11):
            ints = int(slist[i])
            assscore = assscore + ints
            if ints < assminval:
                assminval = ints
        aasscore = assscore - assminval

        weightedassscore = assscore/3.0*0.25
        #print (assscore, weightedassscore)

        examscore = (int(slist[11])+int(slist[12]))*0.25
        totalscore = weightedquizscore + weightedassscore + examscore
        #print (totalscore)
        if totalscore > 60.0:
            my_dict[slist[0]] = "pass"
        else:
            my_dict[slist[0]] = "fail"

    #print (my_dict)
    return (my_dict)

#my_final_grade_calculation('lz7.txt')

# Write a function named "MY_2D_LIST" that receives a positive integer n (n >= 1) as parameter and
# returns a 2 dimensional list of numbers as shown below:

# For example, if the function is called as

# MY_2D_LIST(8)
# then your function should return
# [[1],
# [1, 1],
# [1, 2, 1],
# [1, 3, 3, 1],
# [1, 4, 6, 4, 1],
# [1, 5, 10, 10, 5, 1],
# [1, 6, 15, 20, 15, 6, 1],
# [1, 7, 21, 35, 35, 21, 7, 1]]
# Notes:
# The first list has 1 element, the second list has 2 elements, the third list has 3 elements and so on.
# The first and the last element of each list are always 1.
# The value of other elements in each list is the sum of the elements from the previous list with
# the same index and the index before. For example, the value of the element with index 2 in the list
# with index 5 is 10 which is equal to the sum of the values of the elements from previoius list with
# index 2 and index 1.
# This is called Pascal's Triangle
# Do NOT import any module for solving this problem.

def MY_2D_LIST(n):
    my_list = []
    for i in range (1,n+1):
        if i == 1:
            sublist = [1]
            my_list.append (sublist)
        elif i == 2:
            sublist = [1, 1]
            my_list.append (sublist)
        else:
            sublist = [1]
            for j in range(1,i-1):
                tempval = my_list[i-2][j] + my_list[i-2][j-1]
                #print (tempval)
                sublist.append(tempval)
            sublist.append(1)
            my_list.append(sublist)
    #print (my_list)
    return (my_list)

#MY_2D_LIST(8)

# Write a function named "reverse_dictionary" that receives a dictionary as input argument and returns a
# reverse of the input dictionary where the values of the original dictionary are used as keys for the
# returned dictionary and the keys of the original dictionary are used as value for the returned dictionary
# as explained below:

# For example, if the function is called as

# reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'],
# 'smart': ['clever', 'bright', 'talented']})
# then your function should return
# {'precise': ['accurate', 'exact'], 'clever': ['astute', 'smart'], 'talented': ['smart'], 'bright': ['smart'],
# 'exact': ['accurate'], 'smart': ['astute']}
# Notes:
# The list of values in the returned dictionary is sorted in ascending order
# Capitalization does not matter. This means that all the words should be converted to lower case letters.
# For example the word "Accurate" is capitalized in the original dictionary but in the returned dictionary
# it is written with all lower case letters
# Do NOT import any module for solving this problem.

def reverse_dictionary(input_dict):
    new_dict = {}
    new_keylist = list(new_dict.keys())
    inp_keylist = list(input_dict.keys())
    new_vallist = []

    for item in inp_keylist:
        inp_vallist = input_dict[item]
#        print ("input key ", item, inp_vallist)
        for valitem in inp_vallist:
            new_vallist = []
            if new_keylist.count(valitem.lower()) == 0:
                new_keylist.append(valitem.lower())
                new_vallist.append(item.lower())
                new_dict[valitem.lower()] = new_vallist
                #print ("new key ", valitem, new_vallist)
            else:
#                new_dict[valitem].extend(new_vallist)
                new_dict[valitem.lower()].append(item.lower())
                new_dict[valitem.lower()].sort()
                #print ("after", new_dict[valitem])

        #print (new_dict)

    return (new_dict)



#reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever']})
print(reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}))

