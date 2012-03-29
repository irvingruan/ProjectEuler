#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in # words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
# letters. The use of "and" when writing out numbers is in compliance with 
# British usage

def count(num_words):
    
    single_digit = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
    tens_digit = {10:3, 11:6, 12:6, 13:7, 14:8, 15:7, 16:7, 17:8, 18:8, 19:8}
    tweens_digit = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
        
        
        
    hundreds_sum = (100 * 10) + (100 * 10) + (100 * 12) + (100 * 11) + (100 * 11 ) + (100 * 10) + (100 * 12) + (100 * 12) + (100 * 11)
    hundreds_and_sum = 891 * 3
    
    tens_sum = 0
    for i in range(20, 100):
        if i % 10 != 0:
            tens_sum += tweens_digit[int(str(i)[0])] + single_digit[int(str(i)[1])]
        else:
            tens_sum += tweens_digit[int(str(i)[0])]
            
    tens_sum = tens_sum * 10
    
    ones_sum = 0
    for i in range (1, 10):
        ones_sum += single_digit[i]
        
    ones_sum = ones_sum * 10
    
    tweens_sum = 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    tweens_sum = tweens_sum * 10
    
    total_sum = hundreds_sum + hundreds_and_sum + tens_sum + ones_sum + tweens_sum + 11
    
    print total_sum
    
count(1000)