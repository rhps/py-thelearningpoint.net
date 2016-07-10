#Let's import the sys module which will provide us with a way to read lines from STDIN
import sys

print "Hi, what's your first name, second name and age. Separate them by a space?" #Ask the user what's his/her first name, second name and age separated by a space

#[first_name,second_name,age] = sys.stdin.readline().rstrip().split(' ')  #Read a line from STDIN
[first_name,second_name,age] = raw_input().split(' ')
print "First Name: " + first_name.rstrip() #Strip the new line off from the end of the string
print "Second Name" + second_name.rstrip() #Strip the new line off from the end of the string
print "Age:"
print int(age)
print "Next Year, this time your age will be:"
print int(age) + 1