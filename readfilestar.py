read = open("data.txt", "r")

for line in read:
	for character in line:
		if character == "o":
			print("*", end = "")
		else:
			print(character, end = "")