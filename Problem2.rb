base = 1
nextNum = 2
sum = 0;
while base < 4000000
    if base % 2 == 0
        sum = sum + base
    end 
    temp = nextNum
    nextNum = base + nextNum
    base = temp    
end
print sum
