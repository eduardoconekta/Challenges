#Write a program which determines the sum of the first 1000 prime numbers. 
def PrimesSum(top_number):
	tmp  = 0
	i    = 0
	sumPrimes = 0
	while tmp < top_number:
		i += 1
		j = 0
		cont = 0 
		while j <= i:
			j += 1
			if(i % j == 0):
				cont += 1
		if(cont == 2):
			sumPrimes += i
			tmp += 1
	print sumPrimes
PrimesSum(1000)
			