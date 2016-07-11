# Python Dictionaries are Hash Tables
# Here, let us create a small telephone number directory where the Keys are the names of people
# and the values are their phone numbers

# General syntax for initializing a dictionary

phone_directory = {"Ankit":"123-56789","Alex":"567-89010","Nina":"345-678910"}

# Accessing Values in the Dictionary
print "***\nDisplaying the values in the phone directory"
print "Ankit's telephone number", phone_directory["Ankit"]
print "Alex's telephone number", phone_directory["Alex"]
print "Nina's telephone number", phone_directory["Nina"]


# Changing and Updating Values in the Dictionary
#As an example, let us change Ankit's Phone Number.
print "***\nNow, updating Ankits phone number to 321 12345"
phone_directory["Ankit"]="321-12345"
# Now let us print it
# You will notice that the phone number stored in the dictionary has changed
# And the new phone number is displayed
print phone_directory

# Removing/deleting dictionary elements
# Let's say, we'd like to remove Alex's phone number
del phone_directory["Alex"]
# Now when we print this dictionary, there will not be any record for Alex
print phone_directory

# Clearing the dictionary
phone_directory.clear()
# All recors will be wiped out from it
print phone_directory
# no key-value pairs left to display

#Deleting the dictionary
del phone_directory

#Once deleted, you can't update, access or display it