# the function SimpleSymbols(str) take the str parameter
#being passed and determine if it is an acceptable sequence
#by either returning the string true or false. The str 
# parameter will be composed of + and = symbols with several
# letters between them (ie. ++d+===+c++==a) and for the string to 
# be true each letter must be surrounded by a + symbol. So the 
#string to the left would be false. The string will not be empty and will have at least one letter. 

# Input = "+d+=3=+s+"Output = "true"
# Input = "f++d+"Output = "false"

from time import sleep 
simbols = ['+','=']
def SimpleSymbols(str):
	validation = False
	for i in xrange(0,len(str)):
		if str[0] not in simbols:
			validation = False
		elif str[i] not in simbols:
			if i == len(str)-1 and str[i] not in simbols:
				validation = False
				break
			elif str[i+1] in simbols and str[i-1] in simbols :
				validation = True;
				
	str = validation
	return str;

print SimpleSymbols("++d+===+c++==a") #False
print SimpleSymbols("+d+=3=+s+")	  #True
print SimpleSymbols("f++d+")		  #False
