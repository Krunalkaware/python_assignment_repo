num = int(input("Enter an integer: "))

if num == 0:
    print("Zero")

elif num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

else:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")