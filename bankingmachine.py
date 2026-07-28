balance = 0
pin = 6769

while True:
    entered_pin = int(input("Enter the pin of ur bank account:"))
    if entered_pin != pin :
        print("Wrong pin")
        continue
    opt = input("Withdraw or deposit or check balance? ")

    if opt == "deposit":
        deposit = int(input("Enter the amount you wanna deposit: "))
        balance += deposit
        print(f"Your current balance is {balance}")

    elif opt == "withdraw":
        withdraw = int(input("Enter the amount you wanna withdraw: "))
        if withdraw > balance:
            print("Withdrawal amount can't be more than your balance!")
            continue
        else:
            balance -= withdraw
            print(f"Your current balance is {balance}")
    elif opt == "check balance" :
        print(balance)

    opt2 = input("Do you want to continue? (yes/no): ")

    if opt2 == "yes":
        continue
    elif opt2 == "no":
        break
print("Tysm for visiting ")