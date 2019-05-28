message = input("Enter a message: ") + " "
word = ""
count = 0

while count < len(message):
	if (message[count] == " "):
		print(word)
		word = ""
	else:
		word = word + message[count]

	count += 1