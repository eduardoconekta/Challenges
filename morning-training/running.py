#Write a function that computes the running total of a list.

def running(a):
	for index,position in enumerate(a):
		print "{} - {}".format(index,position)

a = [1,2,3,4,4,4,6567,67878,7,564,5,4,2,346,5,76,1,1,3,2,3,4,4,4,6567,67878,7,564,5,4,2,346,5,76,1,1,3,34]
print running(a)