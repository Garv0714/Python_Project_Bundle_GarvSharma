# 🔐 Exclusive Modular Calculator for CodSoft Internship
# Created by: Garv Sharma | Custom Logic | Not Copied
# Features: Full error handling, modular design, hidden logging, unique UI

import time

def show_menu():
    print("\n🧮 Choose Operation:")
    print(" 1. Add")
    print(" 2. Subtract")
    print(" 3. Multiply")
    print(" 4. Divide")
    print(" 5. Modulus")
    print(" 6. Power")
    print(" 7. Floor Division")
    print(" 8. Exit")

def get_number(label):
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("❌ Invalid number! Please try again.")

def perform_operation(choice, a, b):
    try:
        if choice == 1:
            return a + b
        elif choice == 2:
            return a - b
        elif choice == 3:
            return a * b
        elif choice == 4:
            return "Error: Divide by zero" if b == 0 else a / b
        elif choice == 5:
            return "Error: Mod by zero" if b == 0 else a % b
        elif choice == 6:
            return a ** b
        elif choice == 7:
            return "Error: Floor div by zero" if b == 0 else a // b
    except Exception as e:
        return f"Unexpected Error: {e}"

def log_calculation(expr, result):
    with open("calc_history_log.txt", "a") as f:
        f.write(f"{expr} = {result} at {time.ctime()}\n")

def calculator():
    print("🧠 Welcome to Garv Sharma’s Modular Pro Calculator 🔥")
    while True:
        show_menu()
        try:
            choice = int(input("🔢 Enter choice (1-8): "))
            if choice == 8:
                print("👋 Exiting... Thank you!")
                break
            elif choice in range(1, 8):
                num1 = get_number("first")
                num2 = get_number("second")
                result = perform_operation(choice, num1, num2)

                op_symbols = {1: '+', 2: '-', 3: '*', 4: '/', 5: '%', 6: '**', 7: '//'}
                symbol = op_symbols.get(choice, '?')
                expression = f"{num1} {symbol} {num2}"

                print(f"✅ Result: {expression} = {result}")
                log_calculation(expression, result)
            else:
                print("⚠️ Invalid menu choice. Please select from 1 to 8.")
        except ValueError:
            print("❌ Please enter a valid number for choice.")

if __name__ == "__main__":
    calculator()