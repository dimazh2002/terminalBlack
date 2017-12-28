from war import war
from war import chose



def face(mood):

	print ("\n")
	if mood == "happy":
		print ("(^ _ ^)")
		
	elif mood == "warning":
		print ("(! _ !)")
		
	elif mood == "ignor":
		print ("(* * ()")
		
	print ("\n")
	return

def four():
	count = 0
	print ("Please enter password!")
	password = input()
	
	while password != "12qw":
		if count == 1:
			face("happy")
			print("please repeat again")
		elif count == 2:
			face("ignor")
			print("repeat again")
		elif count == 3:
			print("Don't try do it again!")
			face("warning")
		elif count == 4:
			war()
		count = count + 1
		print ("Please enter password!")
		password = input()

	print("I hava a cat, his name is Cat!")	

	return

def fourfoour():
	count = 0

	print ("Please enter password!")
	password = input()
	if password == "12qw":
		print("I hava a cat, his name is Cat!")	
	if count == 1:
		face("happy")
		print("please repeat again")
	elif count == 2:
		face("ignor")
		print("repeat again")
	elif count == 3:
		face("warning")
		print("Don't try do it again!")
		war()
		
	return

def menu():

	face("warning")
	print ("Press 1 or 2 or 3 or 4 or 5 and press 'Enter'")
	print ("Or do something useful")
	print ("Be careful with 6")
	print ("Make your choise!")
	
	return