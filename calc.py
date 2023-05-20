# Get the first number from the user
first = float(input("First: "))

# Get the operation from the user
operation = input("Operation (+, -, *, /): ")

# Get the second number from the user
second = float(input("Second: "))


# Perform the operation
if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "/":
    if second != 0:  # Check for division by zero
        result = first / second
    else:
        print("Error: Division by zero is not allowed")
        result = None
else:
    print("Error: Invalid operation")
    result = None

# Print the result
if result is not None:
    print("Result:", result)
