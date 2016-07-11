# Demonstrating Lists in Python 
# Lists are dynamically sized arrays. They are fairly general and can contain any linear sequence of Python objects: functions, strings, integers, floats, objects and also, other lists. It is not necessary that all objects in the list need to be of the same type. You can have a list with strings, numbers , objects; all mixed up. 

# Constructing a basic list
# This list purely has integers
test_list = [1,2,3,4,5,6,7,8,9]
print test_list

# Constructing a mixed list
# This list has integers as well as strings
test_mixed_list = [1,2,3,"test list"]
print "Displaying test_list"
print test_list    
print "Displaying test_mixed_list"
print test_mixed_list


# Appending to a list
test_list.append(10)
# Now the test_list = [1,2,3,4,5,6,7,8,9,10]
print "After appending 10 to the test_list"
print test_list
test_list = test_list + [13,12,11]
# Now the test_list = [1,2,3,4,5,6,7,8,9,10,13,12,11]
print "After adding [13,12,11] to the test list"
print test_list


# Delete from the test_list
del test_list[2]
print "Deleted element at index 2 in the test_list"
# new test list is [1,2,4,5,6,7,8,9,10,13,12,11]
print test_list

# Sorting a list
print "Sorting the test list"
test_list.sort()
print test_list
# This will display [1,2,4,5,6,7,8,9,10,11,12,13]

# Reverse a list
print "Reversting the test_list"
test_list.reverse()
print test_list
# This will display [13,12,11,10,9,8,7,6,5,4,2,1]

# Now we will demonstrate "Multiplying" a list with a constant. I.e, the 
# list will be repeatedly concatenated to itself
list_to_multiply = ['a','b','c']
print "list to multiply"
print list_to_multiply
print "After multiplying this list by 3, i.e. repeating it 3 times:"
product_list = 3 * list_to_multiply
print product_list
# This will display ['a','b','c','a','b','c','a','b','c']