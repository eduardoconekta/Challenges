'''
Write three functions that compute the sum of the 
numbers in a list: using a for-loop, a while-loop 
and recursion. (Subject to availability of these 
constructs in your language of choice.)
'''

def sum_for(x):
	sum = 0
	for i in x:
		sum += i
	return sum
def sum_while(x):
	sum = 0
	position = len(x)
	while position > 0:
		position -= 1
		sum += x[position]
	return sum
def sum_recursion(x,sum):
	if len(x) == 0:
		return sum
	sum +=x[0]
	#print x #debug
	x.pop(0)
	return sum_recursion(x,sum)

a = [1,2,3,4,6,77,7,5,454756,867,67,85,541,2343]

print sum_for(a)
print sum_while(a)
print sum_recursion(a,0)
