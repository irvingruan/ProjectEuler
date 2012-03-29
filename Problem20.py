#!/usr/bin/env python

# n! means n  (n  1)  ...  3  2  1

# For example, 10! = 10  9  ...  3  2  1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def sum_of_digits(factorial):

    base = factorial
    
    factorial = factorial - 1
    while factorial > 1:
        addendum = base
        for i in range(0, factorial-1):
            base = base + addendum
          
        factorial -= 1
    
    s_of_digits = 0
    for digit in str(base):
        s_of_digits += int(digit)
        
    print "Sum is %s" % str(s_of_digits)

sum_of_digits(100)