# Write a program which asks the user to enter an integer 'n'
# which would be the total numbers of hours the user worked in
# a week and calculates and prints the total amount of money the
# user made during that week. If the user enters any number less than
# 0 or greater than 168 (n < 0 or n > 168) then your program should print
# INVALID 

# Assume that hourly rate for the first 40 hours is $8 per hour. 

# Hourly rate for extra hours between 41 and 50 (41 <= n <= 50 ) is $9 per hour. 

# Hourly rate for extra hours greater than 50 is $10 per hour.

pos = input ("Enter positive integer: ")
hour = int(pos)
if hour < 0 or hour > 168:
    print("INVALID")
elif hour <= 40:
    wage = 8*hour
    print("YOU MADE",wage,"DOLLARS THIS WEEK")
elif hour <= 50:
    wage = 320 + 9*(hour - 40)
    print("YOU MADE",wage,"DOLLARS THIS WEEK")
else:
    wage = 320+90+10*(hour - 50)
    print("YOU MADE",wage,"DOLLARS THIS WEEK")
 
