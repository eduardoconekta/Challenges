#Write a function that returns the largest element in a list.

def largest_element(x):
	if len(x) == 1:
		return x[0]
	if x[0] > x[1]:
		x.pop(1)
	else:
		x.pop(0)
	return largest_element(x)

arr = [2,3,4,5,63,5,5]

print largest_element(arr)
