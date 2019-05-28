number = int(input("Enter a number "))

if number > 1000:
	print("B")

	if number > 2000:
		print("C")
	else:
		print("F")

	print("2")
else:
	print("A")

	if number > 500:
		print("D")
	else:
		print("E")

	print("1")

print("3")