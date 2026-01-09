# Advanced Calculator: Add, Subtract, Multiply (with multiple numbers)

def calculator():
    print("Welcome to the advanced calculator!")
    print("You can choose: add, subtract, multiply")
    print("Example: add 5 10 15 OR subtract 100 25 OR multiply 2 3 4")

    # Take full input from user
    user_input = input("Enter your operation and numbers: ").strip().split()

    if len(user_input) < 2:
        print("❌ Please enter an operation followed by numbers.")
        return

    operation = user_input[0].lower()
    try:
        numbers = [float(num) for num in user_input[1:]]
    except ValueError:
        print("❌ Invalid number detected. Please enter only numeric values.")
        return

    # Perform calculation
    if operation == "add":
        result = sum(numbers)
    elif operation == "subtract":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
    else:
        print("❌ Unsupported operation. Use add, subtract, or multiply.")
        return

    print(f"✅ Result: {result}")

# Run the calculator
calculator()
