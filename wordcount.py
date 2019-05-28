message = input("Enter a message: ")
words = 0
count = 0

while count < len(message):
	if message[count] == " ":
		words += 1
	
	count += 1

print("There are", (words + 1), "words")