def ones(digit):
	if digit == 0:
		return ""
	if digit == 1:
		return "one "
	if digit == 2:
		return "two "
	if digit == 3:
		return "three "
	if digit == 4:
		return "four "
	if digit == 5:
		return "five "
	if digit == 6:
		return "six "
	if digit == 7:
		return "seven "
	if digit == 8:
		return "eight "
	if digit == 9:
		return "nine "

def tens(digit):
	if digit == 0:
		return ""
	if digit == 10:
		return "ten "
	if digit == 11:
		return "eleven "
	if digit == 12:
		return "twelve "
	if digit == 13:
		return "thirteen "
	if digit == 14:
		return "fourteen "
	if digit == 15:
		return "fifteen "
	if digit == 16:
		return "sixteen "
	if digit == 17:
		return "seventeen "
	if digit == 18:
		return "eighteen "
	if digit == 19:
		return "nineteen "
	if digit == 2:
		return "twenty "
	if digit == 3:
		return "thirty "
	if digit == 4:
		return "fourty "
	if digit == 5:
		return "fifty "
	if digit == 6:
		return "sixty "
	if digit == 7:
		return "seventy "
	if digit == 8:
		return "eighty "
	if digit == 9:
		return "ninety "

def hundreds(digit):
	return ones(digit) + "hundred "

def thousands(digit):
	return ones(digit) + "thousand "

def splitNumber(number):
	returnString = ""
	
	if(len(number) >= 4):
		returnString = returnString + thousands(int(number[int(len(number)) - 4]))

	if(len(number) >= 3):
		if int(number[int(len(number)) - 3]) == 0:
			returnString = returnString + ""
		else:
			returnString = returnString + hundreds(int(number[int(len(number)) - 3]))

	if(len(number) >= 2):
		if (number[int(len(number)) - 2] == "1"):
			returnString = returnString + tens(int(number[int(len(number)) - 2] + number[int(len(number)) - 1]))
			number = ''
		else:
			if int(number[int(len(number)) - 2]) == 0:
				returnString = returnString + ""
			else:
				returnString = returnString + tens(int(number[int(len(number)) - 2]))

	if(len(number) >= 1):
		if int(number[int(len(number)) - 1]) == 0:
				returnString = returnString + ""
		else:
			returnString = returnString + ones(int(number[int(len(number) - 1)]))

	return returnString



print(splitNumber(input("Enter a number: ")))