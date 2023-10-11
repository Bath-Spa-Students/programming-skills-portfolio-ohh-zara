# Exercise 3: Print date and Time 
# Write a Python program to display the current date and time.

#First, we import the dtetime.
import datetime
now = datetime.datetime.now()

#Then, we print the date and time
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
