find = input("What are you looking for: ")
replace = input("Replace with what: ")

file_read = open("data.txt", "r")
file_write = open("data2.txt", "w")

for data in file_read:
	count = 0
	while count < len(data):
		if data[count] == find[0]:
			if data[count: len(find) + count] == find:
				print(replace, end = "", file = file_write)
				count += len(find) - 1
			else:
				print(data[count], end = "", file = file_write)

		else:
			print(data[count], end = "", file = file_write)

		count += 1