#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

def isPrime(num):
	if num == 1:
		return False
	elif num < 4:
		return True
	elif num % 2 == 0:
		return False
	elif num < 9:
		return True
	elif num % 3 == 0:
		return False
	else:		
		sqrRoot = int(math.floor(math.sqrt(num)))	
		for i in range(5, sqrRoot+1):
			if num % i == 0:
				return False
			elif num % (i + 2) == 0:
				return False
			i += 6
	return True
	
def primeSumUnder(limit):
	

	sum = 0
	for i in range(1, limit):
		if isPrime(i):
			sum += i
	
	print sum

primeSumUnder(2000000)