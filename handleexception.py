def divide():
	try:
		firstNumber = int(input("Enter the first number: "))
		secondNumber = int(input("Enter the second number: "))

		result = firstNumber / secondNumber

		print("Result", result)

	except ZeroDivisionError:
		print("Can't divide by zero")
	except ValueError:
		print("Only enter digits")
	finally:
		print("Finished")