# Demonstrating Tuples
# Tuples are sequences of immutable Python objects. They are quite similar to lists.
# The difference is, that tuples can't be changed, once creaed. i.e. they are immutable
# Also, tuples use parentheses while Lists use Square Brackers

# Let us declare some tuples to look at the general syntax.

tuple1 = ('history','geography',1,2,3)
tuple2 = (1,10,20,30)
tuple3 = "name","age","qualification"

#Empty tuple
tuple4 = ()

# Tuple with just one element: make sure to use the comma
tuple5 = (10,)

# Accessing values in tuples. Indexing and Slicing.
# Quite similar to Lists.
print "Displaying tuple1"
print tuple1
print "Displaying tuple1[0] ..i.e, the first element of tuple1"
print tuple1[0]
# This will display: history
print "Displaying tuple1[1:3] .. i.e display a subsequence of elements of tuple1"
print tuple1[1:3]
# This will display 10, 20, 30

# Updating Tuples
# We can't update or change existing tuples since they are immutable. 
# However, we can make new tuples out of them
print "Making a new tuple from tuple2 and tuple3"
print "tuple2:"
print tuple2
print "tuple3:"
print tuple3
print "Creating a new tuple4 = tuple2 + tuple3"
tuple4 = tuple2 + tuple3
print "Tuple4:"
print tuple4
# This will print (1,10,20,30,name,age,qualification)