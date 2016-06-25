# Write a program which reverses the words in an input sentence.
#Input sample:
#
#The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.
#
#For example:
#Hello World
#Hello CodeEval

def reverseSentences(phrase):
	arr_phrase = phrase.split(' ')
	arr_phrase = [i for i in reversed(arr_phrase)]
	phrase 	   =' '.join(map(str,arr_phrase))
	print phrase
	
reverseSentences("Hello World")
reverseSentences("Hello CodeEval")