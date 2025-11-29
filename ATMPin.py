balance = 100000
pin = 567

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    amount = int(input("Enter amount: "))
    
    if amount <= balance:
        balance =balance - amount
        print("Withdrawal successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")