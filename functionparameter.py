def operation(f, a, b):
	f(a, b)

def addition(a, b):
	result = a + b
	print("Result:", result)

def subtraction(a, b):
	result = a - b
	print("Result:", result)

def chooseOperation(a):
	if a == 1:
		return addition
	if a == 2:
		return subtraction

operation(chooseOperation(2), 10, 10)
