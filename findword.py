message = input("Enter a message: ") + " "
searchWord = input("Enter the word to find: ")
word = ""
count = 0
wordCount = 0

while count < len(message):
	if (message[count] == " "):
		if word.lower() == searchWord.lower():
			wordCount += 1

		word = ""
	else:
		word = word + message[count]

	count += 1

print(searchWord, "is in the string", wordCount, "times")
print("")