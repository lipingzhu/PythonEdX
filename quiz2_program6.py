# Write a program that asks the user to enter a positive integer n.
# Assuming that this integer is in seconds, your program should convert
# the number of seconds into days, hours, minutes, and seconds and prints
# them exactly in the format specified below. 
pos = input ("Enter positive integer: ")
seconds = int(pos)
days = 0
hours = 0
mins = 0
secs = 0
sec_in_day = 60*60*24
sec_in_hour = 3600
sec_in_min = 60
if seconds >= sec_in_day:
    days = seconds // sec_in_day
    hours = seconds % sec_in_day // sec_in_hour
    mins = (seconds % sec_in_day) % sec_in_hour // sec_in_min
    secs = (seconds % sec_in_day) % sec_in_hour % sec_in_min
elif seconds >= sec_in_hour:
    hours = seconds // sec_in_hour
    mins = seconds % sec_in_hour // sec_in_min
    secs = seconds % sec_in_hour % sec_in_min
elif seconds >= sec_in_min:
    mins = seconds // sec_in_min
    secs = seconds % sec_in_min
else:
    secs = seconds
print(days,"days",hours,"hours",mins,"minutes",secs,"seconds")

 
