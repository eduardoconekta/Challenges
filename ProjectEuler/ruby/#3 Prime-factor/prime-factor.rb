#Largest prime factor
#Problem 3
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
save  = 1
point = 600851475143
for x in (1 .. 600851475143)
	if point % x == 0  
		puts x
		save *=x
	elsif save == point
		break
	end
end