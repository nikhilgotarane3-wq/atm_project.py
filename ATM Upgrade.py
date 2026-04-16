balance = 10000
pin = 1234
last_transaction = "No transaction yet"

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    
    while True:
        print("\n1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. Mini Statement")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Your balance is:" ,balance)
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount 
            last_transaction = "deposited" + str(amount)
            print("Updated balance:", balance)
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > 5000:
                print("Limit exceeded (Max 5000)")
            if amount <= balance: 
               balance = balance - amount 
               last_transaction = "withdraw " + str(amount)
               print("Updated balance:", balance)
            else:
                print("Insufficient balance")
        elif choice == 5:
            print("Last transaction:",last_transaction)
        elif choice == 4:
            print("THank you!")
            break
        
        else:
            print("Invalid choice")
    else:
        print("Wrong PIN")