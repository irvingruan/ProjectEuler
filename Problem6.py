#!/usr/bin/env python

# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and 
# the square of the sum is 3025  385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

import math

def difference():
	
	# Sum of first 100 natural numbers is ...
	# 1 + 2 + 3 .... + 97 + 98 + 99 + 100 = X
	# (1+100) + (2+99) + (3+98) + ... + (50,51) = 101 * 50
	# so.... sum of squares is
	# (1^2 + 100^2) + (2^2 + 99^2) + (3^2 + 98^2) ...
	
	baseDiff = 196
	sum = 0
	initialSum = 10001
	for i in range(1, 51):
		sum = sum + initialSum
		initialSum = initialSum - baseDiff
		baseDiff -= 4
		
	s = 5050
	print int(math.fabs(sum - 5050**2))
	
difference()
	

