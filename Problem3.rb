def checkPrime(value,iterator)
   prime = -1
   while value % iterator != 0
       prime = iterator
       iterator += 1
       if iterator == value
           break
       end
   end
   return prime
end

test = 600851475143
squareRoot = Math.sqrt(600851475143)
print 'square root is '
current = 50
index = 1
biggest = 0
while current <= squareRoot
   unless current % 2 == 0 
       val = checkPrime(current,3)
       if val > biggest
           biggest = val
       end
   end
   current += 1

end
print bigest