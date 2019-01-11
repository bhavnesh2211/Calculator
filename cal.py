from calculator import *
def calculation(num1,num2,oparation):
	while True:
		if oparation == "add" or oparation == "+" or oparation == "Add":
			print add(num1,num2,oparation)
		elif oparation=="sub" or oparation == "-" or oparation == "Sub":
			print sub(num1,num2,oparation)
		elif oparation == "mul" or oparation=="*" or oparation == "Mul":
			print mul(num1,num2,oparation)
		elif oparation == "div" or oparation == "/" or oparation == "Div":
			print div(num1,num2,oparation)
		else:
			print "invial oparation."
		user = raw_input("You want to do calculation again? ""y/n")
		if user == "n" or user == "N":
			break

a = int(raw_input("Enter your first number: "))
b = int(raw_input("Enter your second number: "))
c = raw_input("Enter your oparation what you want to do: ")

calculation(a,b,c)
