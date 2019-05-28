number = int(input("Enter any number "))

if number > 1000:
	print("B")
	if number > 2000:
		print("C")
else:
	print("A")
	if number > 500:
		print("D")