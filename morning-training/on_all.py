'''
Write a function on_all that applies a function to every 
element of a list. Use it to print the first twenty perfect 
squares (a natural number n is a perfect square if it can 
be written as n=m*m for some other natural number m. 1,4,9,16,25 are the first 5).
'''


def on_all():
	i = 1
	j = 1
	l = False
	iterator = 0
	collect = []
	while i <= 20:
		while l != True:
			#print "i{} x l{}".format(j,i) #debugg
			if(j == i):
				collect.append(i * j)
				l = True
				i+=1
			j +=1 
		iterator+= 1
		l = False
	return collect

print on_all()