billAmount = int(input("Enter the total bill "))
paidAmount = int(input("Enter the total amount paid "))
print("")
print("")

totalChange = paidAmount - billAmount
change = paidAmount - billAmount

print("Change =", totalChange)
print("-------------------")
print("")

if int(change / 50) > 0:
	fifties = int(change / 50)
	change = (change - (50 * fifties))#
	print("x 50 =", fifties)

if int(change / 20) > 0:
	twenties = int(change / 20)
	change = (change - (20 * twenties))
	print("x 20 =", twenties)

if int(change / 10) > 0:
	tens = int(change / 10)
	change = (change - (10 * tens))
	print("x 10 =", tens)

if int(change / 5) > 0:
	fives = int(change / 5)
	change = (change - (5 * fives))
	print("x 5 =", fives)

if int(change / 2) > 0:
	twos = int(change / 2)
	change = (change - (2 * twos))
	print("x 2 =", twos)

if int(change / 1) > 0:
	ones = int(change / 1)
	change = (change - (1 * ones))
	print("x 1 =", ones)

print("")