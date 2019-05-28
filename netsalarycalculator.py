name = input("Enter your name ")

if name.lower() != "shafeeq":
	salary = int(input("Enter your salary "))
else:
	salary = 95000
	print("Your salary is 95000")

if salary > 2000:
	tax = salary * 25 / 100
else:
	tax = salary * 15 / 100

netSalary = salary - tax

print("--------------------")
print(name)
print("Salary:", salary)
print("Tax:", tax)
print("Net Salary", netSalary)
print("--------------------")

if name.lower() == "shafeeq":
	print("I hate you.")