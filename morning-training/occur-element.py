
def detect_element(x,element):
	if(element in x): 
		return True
	return False
a = [1,2,3,4,3,566,3]
print detect_element(a,0)
print detect_element(a,1)