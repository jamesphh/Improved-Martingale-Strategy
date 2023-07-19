import random


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def martingale(balance, target, increment):
    bet = increment
    inARow = 0

    while balance < target:
        balance = round(balance, 3)
        if balance < increment:
            print("Balance: £" + str(balance))
            print("Bust")
            return
        print("Balance: £" + str(balance))
        if bet <= balance:
            if random.random() < 18 / 37:
                balance += bet
                bet = increment
                inARow = 0
            else:
                balance -= bet
                bet *= 2
                inARow += 1
        else:
            bet = increment
            print("Starting Over")

    print("Balance: £" + str(balance))
    print("Success")


def main():
    balance = get_positive_float("Starting Amount (£): ")
    target = get_positive_float("Target Amount (£): ")
    increment = get_positive_float("Increment (£): ")

    martingale(balance, target, increment)


if __name__ == "__main__":
    main()
