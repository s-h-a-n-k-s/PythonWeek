message = input("Enter a message: ")
word = ""
count = len(message) - 1

while count >= 0:
	if (message[count] == " "):
		print(word)
		word = " "
	else:
		word = message[count] + word

	count -= 1

print(word)
print("")