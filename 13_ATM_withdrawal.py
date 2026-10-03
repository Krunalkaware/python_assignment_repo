pin = int(input("Enter your PIN: "))
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if pin != 1234:
    print("Invalid PIN")

elif amount <= 0:
    print("Invalid withdrawal amount")

elif amount > balance:
    print("Insufficient Balance")

else:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)