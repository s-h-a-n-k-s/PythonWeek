productName = input("Enter product name")
price = float(input("Enter product price"))
quantity = int(input("Enter quantity"))

amount = quantity * price
vat = amount * 15 / 100
bill = amount + vat

print("Your reciept:")
print("-------------------")
print(productName)
print("Amount: ", amount)
print("VAT: ", vat)
print("-------------------")
print("Total bill: ", bill)