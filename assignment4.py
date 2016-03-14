# Part 1: Read file and create dictionary
# Write a function named create_grades_dict that accepts a string as the name of a file. Assuming that the file is a text file
# which includes name and grades of students, your function should read the file and return a dictionary with the exact format
# as shown below: The format of the input file is:

# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# ....
# An example of the input file is shown below. Sample Input Output Assuming that the input file "student_grades.txt"
# contains the following text:
# 1000123456, Rubble, Test_3,  80, Test_4 , 80
# 1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88
# Notes:
# Items are seperated by comma and one or more spaces may exist between the items.
# The "ID" of each student is unique. Two students may have the same Name (but IDs will be different)
# The "Name" of each student will only include a last name with no punctuation. Maximum of 15 characters.
# There will be an integer grade for each test (0-100)
# There are only four valid tests, i.e. Test_1, Test_2, Test_3, Test_4. There may be other grades in the file and
# you should ignore those grades.
# Each student may have missing grade(s) for the tests. A missing grades should be considered as 0.
# Grades may not be in order i.e. Test_3 may appear before Test_1.
# Your function should read the input file, calculate the average test grade for each student and
# return a dictionary with the following format:
# {'Student_ID':[Last_name,Test_1_grade,Test_2_grade,Test_3_grade,Test_4_grade,average], ...}
# For example in the case of sample input file shown above, your function should return the following dictionary:
# {'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}

def create_grades_dict(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    my_dictionary = {}
    test_list = ['Test_1','Test_2','Test_3','Test_4']

    for item in data:
        outlist = []
        itemlist = item.split(',')
        sum = 0
        newlist = []

        for j in itemlist:
            newlist.append(j.strip())
        outlist.append(newlist[1])
        #print (newlist)

        for i in test_list:
            score = 0
            #print (newlist.count(i))
            if newlist.count(i) != 0:
                ind = newlist.index(i)
                score = int(newlist[ind+1])
            outlist.append(score)
            sum = sum + score
        avg = sum/4
        outlist.append(avg)
        #print (outlist)

        my_dictionary[newlist[0]] = outlist
        #print (itemlist)

    return (my_dictionary)

# Part 2: Print grades
# Write a function called print_grades that accepts the name of a file (string) as input argument.
# Assuming the format of the file is the same as the file in part 1, your function should call the function
# that you developed in part 1 to read the file and create the grades dictionary. Using the grades dictionary,
# your function should print the names, grades, and averages of students with the exact format shown below.
# Notice that you are asked to write a function (NOT a program) and that function prints the grades.
# Your function should return None after printing the grades.

# Sample Input file:

# 1000123456, Rubble, Test_3,  80, Test_4 , 80, quiz , 90
# 1000123210, Bunny, Test_2, 100, Test_1, 100,Test_3   , 100 ,Test_4 , 100
# 1000123458, Duck, Test_1, 86, Test_5   , 100 , Test_2 ,93 ,Test_4, 94
# Your program's output should be:

#    ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |
#1000123210 | Bunny            |    100 |    100 |    100 |    100 | 100.00 |
#1000123456 | Rubble           |      0 |      0 |     80 |     80 |  40.00 |
#1000123458 | Duck             |     86 |     93 |      0 |     94 |  68.25 |
# Notes:
# Column titles are all centered
# The printed output is sorted in ascending order based on the student IDs
# Each column is seperated from a neighboring column(s) by three characters ' | ' (space vertical_bar space).
# IDs are always 10 characters and they are left justified (not counting the boundary characters)
# Names are left justified (maximum of 16 characters, not counting the boundary characters).
# Grades and averages are right justified. The width of the columns for the grades and averages is 6 characters
# (not counting the boundary characters).
# Averages are right justified with two digits of accuracy after the decimal point.
# Hint: Use the function which you developed in part 1 to read the input file and create a dictionary.
# Use .format() to format the output.

def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict=create_grades_dict(file_name)
    head_str = "{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} |".format('ID','Name','Test_1','Test_2','Test_3','Test_4','Avg.')
    print (head_str)
    idkeys = list(grades_dict.keys())
    idkeys.sort()
    print (idkeys)

    for id in idkeys:
        vlist = grades_dict.get(id)
        grade_str = "{0:10s} | {1:16s}| {2:6d} | {3:6d} | {4:6d} | {5:6d} | {6:6.2f} |".format(id,vlist[0],vlist[1],vlist[2],vlist[3],vlist[4],vlist[5])
        print (grade_str)

    return None

print (print_grades('student_grades1.txt'))
# print (create_grades_dict('student_grades.txt'))