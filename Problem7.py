#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th 
# prime is 13.

# What is the 10001st prime number?

import math

def checkPrime(num):
	if num % 2 == 0:
		return False
	for i in range(3, int(math.floor(math.sqrt(num))) + 1):
		# Skip even numbers
		if i % 2 == 0:
			continue
		if num % i == 0:
			return False
			
	return True

def nthPrime(seq):
	nth = 0
	num = 3
	while nth < seq - 1:
		if checkPrime(num):
			nth += 1
		num += 1
	
	print num - 1
	
nthPrime(10001)
	

