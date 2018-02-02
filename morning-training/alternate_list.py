def alternate(a,b, new_list):
	if(len(a) == 0):
		return new_list
	new_list.append(a.pop(0))
	new_list.append(b.pop(0))
	return alternate(a,b,new_list)
	

a=['a','b','c']
b=[1,2,3]
print alternate(a,b,[])