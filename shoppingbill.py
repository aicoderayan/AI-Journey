customer =input("Enter the customer name: ")

product1 =input("Enter the Product 1: ")
price1 =int(input("Enter Product 1 Price: "))
product2 =(input("Enter the Product 2: "))
price2 =int(input("Enter the Product 2 Price: "))
product3 =input("Enter the Product 3: ")
price3 =int(input("Enter the Product 3 Price: "))

total_price =(price1 + price2 + price3)
discount =(total_price / 100) * 10
final_amount =(total_price - discount)

print("Total price:", total_price)
print("Discount:", discount)
print("Final amount:", final_amount)