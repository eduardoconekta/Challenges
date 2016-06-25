# have the function SimpleAdding(num) add up
# all the numbers from 1 to num. For the test 
#cases, the parameter num will be any number 
#from 1 to 1000. 
#Input = 12Output = 78
#Input = 140Output = 9870 

def SimpleAdding(num):
	for i in xrange(1,num):
		num+=i
	return num

print SimpleAdding(140)