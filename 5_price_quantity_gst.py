price1 = float(input("Enter price of product 1: "))
quantity1 = int(input("Enter quantity of product 1: "))

price2 = float(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of product 2: "))

price3 = float(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

amount1 = price1 * quantity1
amount2 = price2 * quantity2
amount3 = price3 * quantity3

subtotal = amount1 + amount2 + amount3

discount = subtotal * 10 / 100
after_discount = subtotal - discount

gst = after_discount * 18 / 100

final_amount = after_discount + gst

print("Subtotal =", subtotal)
print("Discount =", discount)
print("GST =", gst)
print("Final Payable Amount =", final_amount)