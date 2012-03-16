#!/usr/bin/env python

import math

def checkIfPalindrome(number):
	digits = str(number)
	secondChunk = digits[3:6]
	if digits[:3] == secondChunk[::-1]:
		return True
	
	return False

def checkIfDivisible(number):
	for i in range(100, 1000):
		if number % i == 0 and len(str(i)) == 3 and len(str(number/i)) == 3:
			print i, number / i
			return True
			
	return False

def findLargestPalindrome():
	
	# Biggest number from xyz * abc
	i = 998001
	while i > 99999:
		if checkIfPalindrome(i):
			if checkIfDivisible(i):
				print i
				break
		
		i -= 1
	

findLargestPalindrome()
