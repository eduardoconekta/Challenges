#[5, 4, 0, 3, 4, 1]
import sys

def graph(arr):
	max_value  = max(arr) 
	lenght_arr = len(arr)
	matrix = []
	for index,i in enumerate(range(lenght_arr,0,-1)):
		for j in xrange(0,lenght_arr):
			if arr[j] >= i-1:
				sys.stdout.write("*")
			else:
				sys.stdout.write(" ")
		print
	
arr = [5, 4, 0, 3, 4, 1]
graph(arr)