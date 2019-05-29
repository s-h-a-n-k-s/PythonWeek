def convert(character):
	if ord(character) >= 65 and ord(character) <= 90:
		print(chr(ord(character) + 32))
	elif ord(character) >= 97 and ord(character) <= 122:
		print(chr(ord(character) - 32))
	else:
		print("***Please enter a non-special character***")
		convert(input("Enter a character: "))

convert(input("Enter a character: "))