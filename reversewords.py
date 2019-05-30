def reverse(word):
	newWord = ""
	count = len(word) - 1
	
	while count >= 0:
		newWord += word[count]
		count -= 1

	return newWord

message = input("Enter a message: ") + " "
newMessage = ""
word = ""

for character in message:
	if character == " ":
		newMessage += reverse(word) + " "
		word = ""
	else:
		word += character

print(newMessage)