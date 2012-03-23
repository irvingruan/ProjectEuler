sum = 0;
(0...1000).each do |num|
   if num % 5 == 0 || num % 3 == 0
       sum = sum + num 
   end
end
print sum

