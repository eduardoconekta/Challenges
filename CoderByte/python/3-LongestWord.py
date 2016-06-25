#LongestWord(sen) take the sen parameter being passed and return 
#the largest word in the string. If there are two or more words 
#that are the same length, return the first word from the string 
#with that length. Ignore punctuation and assume sen will not be 
# empty.
#Output = "time"
#Output = "love" 
import re
sen = []
sen.append("fun&!! time")
sen.append("")

def LongestWord(sen):
	bigger = ""
	sen = sen.split(" ")
	for i in sen:
		if not re.findall("[\W]",i):
			bigger=(bigger,i)[len(i)>len(bigger)]
	return bigger, len(bigger)

print LongestWord("fun&!! time")

print LongestWord("I love dogs")
