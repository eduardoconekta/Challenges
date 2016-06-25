#have the function LetterCapitalize(str) 
#take the str parameter being passed and 
#capitalize the first letter of each word.
#Words will be separated by only one space.
def LetterCapitalize(str):
	word = ""
	for i in xrange(0,len(str)):
		if str[i-1] == " " and str[i-2] != " " or i == 0:
			word +=str[i].upper()
		else:
			word +=str[i]
	str = word
	return str

print LetterCapitalize("this  is the phrase")



