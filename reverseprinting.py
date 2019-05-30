message = input("Enter a message ") + " "
count = 0
word = ""
reversedMessage = ""

while count < len(message):
	if message[count] != " ":
		word += message[count]
	else:
		wordCount = len(word) - 1
		while wordCount >= 0:
			reversedMessage += word[wordCount]
			wordCount -= 1

		reversedMessage += " "
		word = ""

	count += 1

print(reversedMessage)