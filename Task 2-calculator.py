import math

def show_menu():
    print("\n====== SMART CALCULATOR ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Percentage (%)")
    print("8. View History")
    print("9. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")


def calculator():
    history = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice in ['1', '2', '3', '4', '5', '7']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

        if choice == '1':
            result = num1 + num2
            operation = f"{num1} + {num2}"

        elif choice == '2':
            result = num1 - num2
            operation = f"{num1} - {num2}"

        elif choice == '3':
            result = num1 * num2
            operation = f"{num1} * {num2}"

        elif choice == '4':
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                continue
            result = num1 / num2
            operation = f"{num1} / {num2}"

        elif choice == '5':
            result = num1 ** num2
            operation = f"{num1} ^ {num2}"

        elif choice == '6':
            num = get_number("Enter number: ")
            if num < 0:
                print("❌ Cannot find square root of negative number!")
                continue
            result = math.sqrt(num)
            operation = f"√{num}"

        elif choice == '7':
            result = (num1 / 100) * num2
            operation = f"{num1}% of {num2}"

        elif choice == '8':
            print("\n📜 Calculation History:")
            if not history:
                print("No history yet.")
            else:
                for item in history:
                    print(item)
            continue

        elif choice == '9':
            print("👋 Thank you for using calculator!")
            break

        else:
            print("❌ Invalid choice!")
            continue

        print(f"✅ Result: {operation} = {result}")
        history.append(f"{operation} = {result}")


# Run the program
calculator()
