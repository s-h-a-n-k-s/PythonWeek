upperAlpha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lowerAlpha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
message = input("Enter a message: ")
count = 0
outCount = 0

while count < len(message):
	if message[count] != " ":
		if ord(message[count]) >= 65 and ord(message[count]) <= 90:
			upperAlpha[ord(message[count]) - 65] += 1
		else:
			lowerAlpha[ord(message[count]) - 97] += 1

	count += 1

while outCount <= 25:
	if upperAlpha[outCount] > 0:
		print(chr(outCount + 65), "=", upperAlpha[outCount])

	if lowerAlpha[outCount] > 0:
		print(chr(outCount + 97), "=", lowerAlpha[outCount])

	outCount += 1