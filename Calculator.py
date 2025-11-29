while True:
    Operation = """Add. Addition
                   Sub. Subtraction
                   Mul. Multiplication
                   Div. Division
                   Ext. Exit"""

    choice = input("Choose an operation: ")

    if choice == "Add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == "Sub":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)

    elif choice == "Mul":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)

    elif choice == "Div":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 / num2)

    else:
        break