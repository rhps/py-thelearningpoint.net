#Let's import the sys module which will provide us with a way to read lines from STDIN
import sys

print "Hi, what's your name?" #Ask the user what's his/her name
#name = sys.stdin.readline()  #Read a line from STDIN
name = raw_input()
print "Hello " + name.rstrip() #Strip the new line off from the end of the string
