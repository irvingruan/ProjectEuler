#!/usr/bin/env python

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# See Problem13Input.txt for the number

def firstTen(fh):
	
	nList = []
	for line in open(fh, 'r'):
		strNum = line.rstrip('\n')
		nList.append(int(strNum))
		
	s = 0
	for num in nList:
		s += num
		
	print str(s)[0:10]
	

firstTen("Problem13Input.txt")

