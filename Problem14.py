#!/usr/bin/env python

# The following iterative sequence is defined for the set of positive integers:

# n  n/2 (n is even)
# n  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import math

def sequence(n):
    longest_counter = 0   
    num = 3
    save = 0
    
    recurrence_dict = {}
    
    while num < n:
        
        counter = 0
        check = num
        key = num
        
        while check != 1:
            if check % 2 == 0:
                check = check / 2
            else:
                check = (check * 3) + 1
                
            counter += 1        
            recurrence_dict[key] = counter
            
            if check in recurrence_dict:
                recurrence_dict[key] = recurrence_dict[check] + counter
                counter = recurrence_dict[key]
                break
         
            
        if counter >= longest_counter:
            longest_counter = counter
            save = num
        
        num += 1
        
    print save, longest_counter
    
sequence(1000000)

