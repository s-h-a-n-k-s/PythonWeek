def wordCount(message):
	words = 1
	count = 0

	while count < len(message):
		if message[count] == " ":
			words += 1

		count += 1

	return words

print("There are", wordCount(input("Enter a message: ")), "words")