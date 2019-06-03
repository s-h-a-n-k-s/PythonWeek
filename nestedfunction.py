def operations(day):
	if day == 1:
		def fun(a, b):
			result = a + b
			print("The result is", result)
	if day == 2:
		def fun(a, b):
			result = a - b
			print("The result is", result)

	return fun

operation = operations(1)
operation(1, 9)