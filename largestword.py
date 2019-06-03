def largestWord(text):
	largestWord = ""
	word = ""
	lw = []
	
	for character in text:
		if character == " ":
			if len(word) > len(largestWord):
				largestWord = word
				lw = [word]
			elif len(word) == len(largestWord):
				lw.append(word)
			word = ""

		else:
			word += character

	print("The largest word in '", text, "' is:")
	print(*lw, sep = ", ")

largestWord(input("Enter a message: ") + " ")