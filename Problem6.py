#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
# any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 
# to 20?

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
	

