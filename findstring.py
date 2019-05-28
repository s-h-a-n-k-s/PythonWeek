message = input("Enter a message: ")
searchTerm = input("Enter the search term: ")
count = 0
appearances = 0

while count < len(message):
	if searchTerm[0] == message[count]:
		if message[count : (len(searchTerm) + count)] == searchTerm:
			appearances += 1
			count = count + len(searchTerm) - 1
	
	count += 1

print(searchTerm, "appears in the string", appearances, "times")