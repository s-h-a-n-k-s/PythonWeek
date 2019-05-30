numbers = []

while True:
	num = int(input("Enter a number: "))
	
	if num == 0:
		break
	else:
		numbers.append(num)
	
highest = numbers[0]
count = 1

while count < len(numbers):
	if numbers[count] > highest:
		highest = numbers[count]
	
	count += 1

print("The highest number entered is:", highest)