num = int(input("Enter an integer: "))

n = abs(num)

count = 0
largest = 0
smallest = 9

while n > 0:
    digit = n % 10

    count = count + 1

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    n = n // 10

print("Number of digits:", count)
print("Largest digit:", largest)
print("Smallest digit:", smallest)
