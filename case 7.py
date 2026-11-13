

balance = 5000
history = []          # list of tuples (type, amount)

while True:
    print("\n1. Deposit  2. Withdraw  3. Balance  4. Summary  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Deposit amount: "))
        if amount <= 0:
            print("Invalid amount!")
        else:
            balance = balance + amount
            history.append(("Deposit", amount))
            print("Deposited. New balance:", balance)

    elif choice == "2":
        amount = int(input("Withdraw amount: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > 10000:
            print("Limit exceeded! Maximum Rs 10000 per transaction.")
        elif balance - amount < 500:
            print("Insufficient balance! Minimum Rs 500 must remain.")
        else:
            balance = balance - amount
            history.append(("Withdraw", amount))
            print("Withdrawn. New balance:", balance)

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        print("--- Transaction Summary ---")
        if len(history) == 0:
            print("No transactions yet.")
        for kind, amt in history:
            print(kind, ":", amt)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
