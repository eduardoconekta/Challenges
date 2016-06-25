#LetterChanges(str) take the str parameter being
#passed and modify it using the following algorithm. 
#Replace every letter in the string with the letter
#following it in the alphabet
#(ie. c becomes d, z becomes a). 
#Then capitalize every vowel in this new string 
#(a, e, i, o, u) and finally return this modified 
#string.
#Use the Parameter Testing feature in the box below to test your code with different arguments. 
# Input = "hello*3"Output = "Ifmmp*3"
#Input = "fun times!"Output = "gvO Ujnft!" 
import re
def LetterChanges(str):
	vowel =['a','e','i','o','u']
	count = 0
	li = list(str)
	for i in str:
		li[count] = chr(ord(i)+1)
		if not re.findall("[a-zA-Z]",str[count]) :
			li[count] = i
		if str[count] == " " :
			li[count] = ' '
		if str[count] == "z":
			li[count] = 'a'
		if li[count] in vowel:
			li[count] = li[count].upper()
		count +=1
	str = li
	return str

print LetterChanges(raw_input("Letter Changes \n>:"))