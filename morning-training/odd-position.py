

def odd_position(x):
	odd = []
	for index,position in enumerate(x):
		if(index % 2 == 1):
			odd.append(position)
	return odd

a = [1,2,3,4,4,4,6567,67878,7,564,5,4,2,346,5,76,1,1,3,2,3,4,4,4,6567,67878,7,564,5,4,2,346,5,76,1,1,3,34]

print odd_position(a)