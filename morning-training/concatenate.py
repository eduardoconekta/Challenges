def concat(a,b):
	new_list = a
	for i in b:
		new_list.append(i)
	return new_list


a = ['a','b','c']
b = [1,2,3]
print concat(a,b)