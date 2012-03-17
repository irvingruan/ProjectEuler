#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
# any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 
# to 20?

import math

def checkDivisibility(num):
	for div in range(2, 21):
		if num % div != 0:
			return False
			
	return True

def findSmallestNumber(initial):
	b = initial * 10000000
	while initial < b:
		divisible = checkDivisibility(initial)
		if divisible == True:
			print initial
			break
		initial += 2
	print "Final: " + str(initial)
	

findSmallestNumber(100)
