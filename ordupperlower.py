character = input("Enter a character: ")

if ord(character) >= 65 and ord(character) <= 90:
	print("Uppercase")
else:
	if ord(character) >= 97 and ord(character) <= 122:
		print("Lowercase")
	else:
		if ord(character) >= 48 and ord(character) <= 57:
			print("Digits")
		else:
			print("Special character")