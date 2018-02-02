'''
Write functions that add, subtract, and multiply
two numbers in their digit-list representation (and return a new digit list). 
If youre ambitious you can implement Karatsuba multiplication. 
Try different bases. What is the best base if you care about speed? 
If you couldnt completely solve the prime number exercise above due
 to the lack of large numbers in your language, you can now use your own library for this task.
'''
def digits(x):
	data = []
	x = str(x)
	size = len(x)
	for i in xrange(0,size):
		data.append(x[i])
	return data

def operations(x):
	old_list = digits(x)
	a = int(old_list[0]+ old_list[1])
	b = int(old_list[1]+ old_list[2])
	new_list = []
	new_list.append(a-b)
	new_list.append(a+b)
	new_list.append(a*b)
	return new_list

print operations(1234)