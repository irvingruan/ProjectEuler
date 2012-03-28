#!/usr/bin/env ruby

# Starting in the top left corner of a 2 x 2 grid, there are 6 routes (without backtracking) to the bottom right corner.You can only move down or right.

# How many routes are there through a 20 x 20 grid?

def paths(length)
    
    first_array = Array.new
    (length * 2 + 1).times do
        first_array.push 0
    end
    
    second_array = Array.new
    (length * 2 + 1).times do
        second_array.push 0
    end
    
    # Add base values
    first_array[0] = 1
    first_array[1] = 2
    first_array[2] = 1
    
    # Use Pascal's Triangle recurrence
    (length * 2 - 2).times do 
       second_array[0] = 1 
       
       for index in 1 ... second_array.size
            second_array[index] = first_array[index-1] + first_array[index]
        
       end
       first_array = second_array.dup
    
    end
    
    print "Paths to the botom corner of #{length} x #{length} square: " + second_array[length].to_s()
    
end


paths(20)

