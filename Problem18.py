#!/usr/bin/env python

# By starting at the top of the triangle below and moving to adjacent numbers on # the row below, the maximum total from top to bottom is 23.

#       3   
#      7 4
#     2 4 6
#    8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

def max_path_sum(f):
    
    fs = open(f, "r")

    triangle = []
    for line in fs:
        triangle.append(line.split())
    
    # Establish base case
    triangle_sum = []
    triangle_sum.append(triangle[0][0])
    
    for i, row in enumerate(triangle):
        # Skip first, base case
        if i == 0:
            pass
        
        row_sum = []
        for i, num in enumerate(row):
            row_sum 
            
            
    
max_path_sum("Problem18Input.txt")