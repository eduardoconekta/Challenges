'''
Write a function that rotates a list by k elements. 
For example [1,2,3,4,5,6] rotated by two becomes 
[3,4,5,6,1,2]. Try solving this without creating 
a copy of the list. How many swap or move operations
do you need?
'''

def swap(a,times):
	if(times == 0):
		return a
	times -= 1 
	a.insert(0,a.pop(a.index(a[-1])))
	print a
	return swap(a,times)

a = [1,2,3,4,5,6]

print swap(a,2)