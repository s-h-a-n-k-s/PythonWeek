number = int(input("Enter a number "))
range = int(input("Enter the range "))
count = 1

while count <= range:
	print(count, "x", number, "=", (count * number))
	count += 1