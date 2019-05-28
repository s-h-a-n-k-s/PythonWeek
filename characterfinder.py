message = input("Enter a message: ")
character = input("What character are you looking for: ")

while len(character) > 1:
	character = input("Please enter a single character: ")

count = 0
characterCount = 0

while count < len(message):
	if (message[count].lower() == character.lower()):
		characterCount += 1
	
	count += 1

print("There are", characterCount, character.upper())
print("")