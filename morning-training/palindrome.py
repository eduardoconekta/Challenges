#Write a function that tests whether a string is a palindrome.
# -*- coding: utf-8 -*-

def palindrome(input):
	return input.lower() == input[::-1].lower()
a = ["Ababa", "Abalaba", "aibofobia", "Ana", "ala", "arenera", "arepera", "anilina", "aviva" ,"Malayalam", "Menem",  "oro", "Oruro", "oso", "ojo", "radar", "reconocer", "rotor", "salas", "seres", "somos", "sometemos"]
for i in a:
	print palindrome(i)