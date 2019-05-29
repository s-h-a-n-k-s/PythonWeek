def change(message):
	count = 0
	returnString = ''

	while count < len(message):
		if ord(message[count]) >= 65 and ord(message[count]) <= 90:
			returnString = returnString + chr(ord(message[count]) + 32)
		elif ord(message[count]) >= 97 and ord(message[count]) <= 122:
			returnString = returnString + chr(ord(message[count]) - 32)
		elif ord(message[count]) >= 48 and ord(message[count]) <= 57:
			returnString = returnString + str(int(message[count]) * 2)
		else:
			returnString = returnString + message[count]
		
		count += 1

	return returnString

string = input("Enter text: ")
print("You entered:", string, "- the function has returned", change(string))