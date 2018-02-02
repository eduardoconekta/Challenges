'''
Write a function that takes a number and returns a list of its digits.
'''
def digits(x):
	data = []
	x = str(x)
	size = len(x)
	for i in xrange(0,size):
		data.append(x[i])
	return data

print digits(100)