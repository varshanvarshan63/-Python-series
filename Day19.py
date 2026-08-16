#creating an banking  system simulator using python
balance = 1000

print("===== BANK =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Balance:", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("New Balance:", balance)

elif choice == 3:
    amount = int(input("Enter amount: "))
    if amount <= balance:
        balance = balance - amount
        print("New Balance:", balance)
    else:
        print("Insufficient Balance")

elif choice == 4:
    print("Thank you for using our banking service!")

elif choice == 5:
    print("returning to main menu")

else:
    print("Invalid Choice")     