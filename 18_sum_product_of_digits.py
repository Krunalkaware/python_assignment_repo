num = int(input("Enter an integer: "))

sum_digits = 0
product_digits = 1

while num != 0:
    digit = num % 10

    sum_digits = sum_digits + digit
    product_digits = product_digits * digit

    num = num // 10

print("Sum of digits =", sum_digits)
print("Product of digits =", product_digits)