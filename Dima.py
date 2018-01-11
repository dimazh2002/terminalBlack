#!/usr/bin/python
from faces import face
from faces import four
from faces import menu

face("happy")

print("What is your name? ")
name = input()
item = "menu"

if name == "dima" or name == "sergei" or name == "luda":
	print ("Hi,", name, "My name is Terminal Niasha!")
	
	while item != "end":
		item = input("I'm waiting for your comand:")	
			
		if item == "menu":
			menu()
		elif item == "end":
			pass
			print ("You push 1. Don't watch YouTube for 24 hours!")
		elif item == "2":
			print ("You push 2. Hi, it's a terminal Black")
		elif item == "3":
			print("You push 3. Yes?")		
		elif item == "4":
			four()
		elif item == "5":
			print ("Sorry do you need help?")
		else:
			print ("Do you need help?")
			print ("Please type 'menu' or press digit key")

else: 
	print("Wrong name!")

