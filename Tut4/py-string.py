import sys
# Demonstrating Strings in Python
# Strings are the simplest and most familiar data structures

# Here is a string constant which we will create 
greeting_statement = "Welcome to Strings in Python"

#Now, let's tell the user to enter his name
print "Can you tell us your name"
# We read the name from STDIN
# rstrip at the end is to eliminate the newline character at the end
input_name = sys.stdin.readline().rstrip()
# Now display the user a customized greeting with his name
# This will show you how strings can be concatenated
print "Demonstrating Concatenation"
print greeting_statement + "," + input_name + "!"

# Now, we will use the multiplication operator to repeat the string five times
print "Demonstrating Replication"
print greeting_statement * 5
# This will display the message Welcome to Strings in Python, five times

#Now we will demonstrate Indexing and Slicing of strings
#x[0] is the first character of the string
#x[1] is the second character of the string
#x[-1] is the last character of the string
#x[-2] is the last-but-one character of the string (or, the second-last character)
#x[1:3] will display the substring of x, from character at index 1 to character at index 3

# Demonstrate Indexes and Slicing of Strings, creating substrings

# Original greeting_statement
print "Original greeting_statement " + greeting_statement

# first character of greeting statement
print "greeting_statement[0]: (first character of greeting statement) "+greeting_statement[0]

# fourth character of greeting statement
print "greeting_statement[3]: (fourth character of greeting statement) "+greeting_statement[3]

# last character
print "greeting_statement[-1]: (last character) " + greeting_statement[-1]

# third-last character
print "greeting_statement[-3]: (third-last character) " + greeting_statement[-3]

# Displays the string from Index 1 to 4
print "greeting_statement[1:4]: (Displays the string from Index 1 to 4) " + greeting_statement[1:4]

# Displays the sub string from first character till index 2 (ie, third character)
print "greeting_statement[:2]: (Displays the string from first character till index 2 (ie, third character)::" + greeting_statement[:2]

# Displays the sub string from index =2  till the end
print "greeting_statement[:2]: (Displays the sub string from index =2  till the end)::" + greeting_statement[2:]

# Displays the length of the string
print "Length of greeting_statement :" + `len(greeting_statement)`

# Splits the string into words, by splitting the string wherever there is a space
print "Splitting the greeting_string into words using split"
print greeting_statement.split(' ')