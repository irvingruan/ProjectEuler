#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def checkPrime(number):
	sqrt = math.sqrt(number)
	for i in range(2, int(math.floor(sqrt))):
		if number % i == 0:
			return False
	
	return True

def findLargestPrimeFactor(number):
	
	biggestPrime = 2
	sqrt = math.sqrt(number)
	for i in range(2, int(math.floor(sqrt))):
		if number % i == 0:
			if checkPrime(i):
				biggestPrime = max(biggestPrime, i)
				
	print biggestPrime
	

findLargestPrimeFactor(600851475143)

	


