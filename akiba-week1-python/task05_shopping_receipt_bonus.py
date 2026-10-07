name = input("Enter your name: ")
product1 = input("Enter the product name: ")
product2 = input("Enter the second product name: ")

price1 = float(input("Enter the first product price: "))
price2 = float(input("Enter the second product price: "))
qty1 = int(input("Enter the quantity for the first product: "))
qty2 = int(input("Enter the quantity for the second product: "))

total1 = price1 * qty1
total2 = price2 * qty2
total = total1 + total2

print("========================================")
print("              RECEIPT")
print("========================================")
print(f"Customer: {name} ")
print("\nProduct\t\tPrice\t\tQty")
print("----------------------------------------")
print(f"{product1}\t\t{price1} ETB\t\t{qty1}")
print(f"{product2}\t\t{price2} ETB\t\t{qty2}")
print(f"\nTotal:         {total} ETB")
print("\nThank you for shopping!")
print("========================================")
