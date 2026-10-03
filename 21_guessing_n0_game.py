number = 50

while True:
    guess = int(input("Guess the number: "))

    if guess > number:
        print("Too High")

    elif guess < number:
        print("Too Low")

    else:
        print("Correct!")
        break