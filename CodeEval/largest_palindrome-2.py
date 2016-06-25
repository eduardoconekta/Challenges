#Write a program which determines the largest prime palindrome less than 1000. 

def largest_palindrome(x):
	for i in xrange(1,x):
		cont = 0
		for j in xrange(1,i+1):
			if(i % j == 0):
				cont +=1
		if cont == 2:
			cast_i = str(i)
			if cast_i[:len(cast_i)/2][::-1] == cast_i[-(len(cast_i)/2):]:
					result = i
	return result

print largest_palindrome(1000);