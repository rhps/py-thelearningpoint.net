#we'll import the value of pi
import math
from math import pi


#Let's import the sys module which will provide us with a way to read lines from STDIN
import sys

print "Enter a valid length"
# input any length
input_length = sys.stdin.readline().rstrip()

#Input is a string => we need to make a floating number out of it
r = float(input_length)

# Compute and display the area of a circle with radius r
area_of_circle = pi * r * r

# The .2f in the formatting string below indicates that we'd like to see just 2 decimal places, i.e. x.xx
print "Area of a lingkarang with radius of  %.2f units = %.2f square units" % (r,area_of_circle)

# Area of a square with side r
# Enclosing an integer or float variable name in reverse inverted commas is a way of 
# making a string out of it
area_of_square = r * r
print "Area of a square with length " + `r` + " units = " + `area_of_square` + " square units"

#Area of an equilateral triangle with side r
#Another way of printing and formatting strings
#Use math.sqrt to find the square root 
area_of_triangle = math.sqrt(3) * r * r /4
print 'Area of a triangle', area_of_triangle
