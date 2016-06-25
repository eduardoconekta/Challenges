#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#Players generally sit in a circle. 
#The first player says the number “1”, and 
#each player says next number in turn. However,
#any number divisible by X (for example, three)
#is replaced by the word fizz, and any divisible
#by Y (for example, five) by the word buzz.
#Numbers divisible by both become fizz buzz.
#A player who hesitates, or makes a mistake 
#is eliminated from the game.
#
#Write a program that prints out the final series 
#of numbers where those divisible by X, Y and both 
#are replaced by “F” for fizz, “B” for buzz and “FB”
# for fizz buzz.
#
#Input sample:
#Your program should accept a file
# as its first argument. The file
#  contains multiple separated lines; 
#  each line contains 3 numbers that 
#  are space delimited. The first number 
#  is the first divider (X), the second 
#  number is the second divider (Y), and 
#  the third number is how far you should 
#  count (N). You may assume that the input 
#  file is formatted correctly and the numbers
#   are valid positive integers. 
#INPUT
#  3 5 10
#  2 7 15
#
#
#Print out the series 1 through N
#replacing numbers divisible by 
#X with “F”, numbers divisible by
#Y with “B” and numbers divisible 
#by both with “FB”. Since the input 
#file contains multiple sets of values,
#your output should print out one line
#per set. Ensure that there are no 
#trailing empty spaces in each line you print. 
#
#
#OUTPUT
#  1 2 F 4 B F 7 8 F B
#  1 F 3 F 5 F B F 9 F 11 F 13 FB 15
"""
def FizzBuzz(x,y,iteration):
	for i in xrange(1,iteration+1):
		if(i % x == 0 and i % y == 0):
			print " FB ",
		elif(i % x == 0):
			print "F",
		elif(i % y == 0):
			print "B",		
		else:
			print i,

FizzBuzz(3,5,10)
print 
FizzBuzz(2,7,15)