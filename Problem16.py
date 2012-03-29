#!/usr/bin/env python

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def sum_of_digits(nth_power):
    
    curr_sum = 32768
    for i in range(15, nth_power):
        curr_sum = curr_sum + curr_sum
            
    indiv_sum = 0
    for i in str(curr_sum):
        indiv_sum += int(i)
        
    print indiv_sum
    
    
sum_of_digits(1000)