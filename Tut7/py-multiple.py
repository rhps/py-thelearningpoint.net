'''
Generally whenever we call a function, we specify a few parameters which are passed to the function.
In the function signature, we specify the number of variables which are received from the function call.
But say we don't know how many parameters are sent when the function is called ?
For this we use multiple function arguments which specify some variables and at the end includes a 
list variable which contains the rest of the variables passed to the function.
'''

def f1(a, b, c):
    print(a, b, c)

def f2(a, *b):
	print (a, list(b))
	
f1(5, 6, 7)
f2(5, 6, 7)


# In order to go through each element passed to a function, we traverse the list.
def f3(a, *b):
    print (a)
    for i in b:
        print (i)

f3(5, 6, 7)