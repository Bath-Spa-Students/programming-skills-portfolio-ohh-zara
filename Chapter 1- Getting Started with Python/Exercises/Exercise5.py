#Exercise 5: Compute area of Circle :ballot_box_with_check:
#Write a Python program which accepts the radius of a circle from the user and compute the area.

#We will import "pi" from math module 
from math import pi

#Taking r as a variab 
r = float(input ("Input the radius of the circle : "))

#now printing the whole thing with the formula of radius of the circle
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))