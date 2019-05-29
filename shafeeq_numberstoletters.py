def ones(num):
	if num == 1:
		return "one"
	if num == 2:
		return "two"
	if num == 3:
		return "three"
	if num == 4:
		return "four"
	if num == 5:
		return "five"
	if num == 6:
		return "six"
	if num == 7:
		return "seven"
	if num == 8:
		return "eight"
	if num == 9:
		return "nine"
	if num == 10:
		return "ten "
	if num == 11:
		return "eleven "
	if num == 12:
		return "twelve "
	if num == 13:
		return "thirteen "
	if num == 14:
		return "fourteen "
	if num == 15:
		return "fifteen "
	if num == 16:
		return "sixteen "
	if num == 17:
		return "seventeen "
	if num == 18:
		return "eighteen "
	if num == 19:
		return "nineteen "

def tens(num):
	if num == 20:
		return "twenty "
	if num == 30:
		return "thirty "
	if num == 40:
		return "fourty "
	if num == 50:
		return "fifty "
	if num == 60:
		return "sixty "
	if num == 70:
		return "seventy "
	if num == 80:
		return "eighty "
	if num == 90:
		return "ninety "

num = int(input("Enter a number: "))
response = ""

if num >= 1000 and num <= 9999:
	response += ones(int(num / 1000)) + " thousand "
	num %= 1000
if num >= 100:
	response += ones(int(num / 100)) + " hundred "
	num %= 100
if num >= 20:
	response += tens(int(num / 10) * 10)
	num %= 10
if num > 0 and num <= 19:
	response += ones(num)

print(response)