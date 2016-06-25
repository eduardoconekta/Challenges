#have the function CheckNums(num1,num2) 
#take both parameters being passed and 
#return the string true if num2 is greater than num1, 
#otherwise return the string false. 
#If the parameter values are equal to each other then return the string -1. 
#
#Input = 3 & num2 = 122Output = "true"
#Input = 67 & num2 = 67Output = "-1" 

def CheckNums(num1, num2):
	if num2 > num1:
		str = "true"
	elif num2 < num1:
		str = "false"
	elif num2 == num1:
		str = "-1"
	return str


print CheckNums(3,1220) #true
print CheckNums(67,67)	# -1
