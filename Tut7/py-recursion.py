# encoding:UTF-8
'''
To find the GCD of two numbers is Euclid’s algorithm, which is based on the observation 
that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). 
As a base case, we can use gcd(a, 0) = a.
'''

def gcd(a, b):
    # Finding the remainder
    r = a % b
    if (r == 0):
        return b
    else :
        return gcd(b, r)


print(gcd(3, 8))
print(gcd(1277, 154))
print(gcd(77, 140))