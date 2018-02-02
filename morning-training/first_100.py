'''
Write a function that computes the list
of the first 100 Fibonacci numbers.
'''


def fib():
	i = 1
	first  = 0
	fib = 0
	second = 1
	while i <= 20:
		
		fib = first + second 
		print fib
		first = second 
		second = fib
		i +=1


print fib()