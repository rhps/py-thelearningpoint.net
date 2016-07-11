def cube(n):
    '''
    a ** b means a^b.
    eg : 2**3 = 2 x 2 x 2 = 8
    '''
    return n ** 3

def string_operation(s):
    '''
    String is an immutable object. So whatever operations we perform on strings
    a new string is generated and the original string stays the same.
    '''
    # Capitalize makes the first letter of the string capital
    print('Capitalized String :', s.capitalize())

    # To find a substring in a given string, python has a function called find(). 
    # If the substring is present in the string, it returns index of its first entry, otherwise -1.     
    print('To find whether the string has the phrase "oper" in it', s.find('oper'))

    # The index function returns the first index location where the substring is contained.
    # It raises a ValueError if the substring is not there. That's why we use find().
    if (s.find('oper') != -1):
        print('Index of "oper"', s.index('oper'))

    print('True if all the characters are alphanumeric and the string is not empty', s.isalpha())

    print('True if all the characters are digits otherwise false', s.isdigit())

    print('Generates a new string with characters capitalized', s.upper())

def volume(length=10, breadth=10, height=10):
    '''
    In the function header we have assigned default values of length, breadth and height
    that is to say if the function is called with only 2 parameters given, then the 
    value of height will be taken as 10.
    '''
    return(length * breadth * height)

def main():
    # Print the cube of a number
    num = int(input("Enter a number : "))
    print("The cube of the number is :", cube(num))
    
    # String Operations
    n = input("Enter a string : ")
    string_operation(n)

    # Volume of a cuboid
    l = int(input("Enter length : "))
    b = int(input("Enter Breadth : "))
    h = int(input("Enter Height : "))
    print("Volume of cuboid :", volume(l, b, h))

if (__name__ == '__main__'): main()