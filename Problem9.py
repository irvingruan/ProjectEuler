#!/usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isTriplet(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	return False

# Not optimized. Purely brute force.		
def solve(sum):
	for i in range(1, sum - 1):
		for j in range(1, sum - 1):
			for k in range(1, sum - 1):
				if isTriplet(i, j, k) and i+j+k == 1000:
					print i, j, k,
					print i * j * k
					break
	
	
solve(1000)

