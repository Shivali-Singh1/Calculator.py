# Python program for a simple calculator

# Function for addition
def add(x, y):
    return x + y


# Function for subtraction
def subtract(x, y):
    return x - y


# Function for multiplication
def multiply(x, y):
    return x * y


# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Main function to run the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input! Please enter a valid choice.")
        return

    # Get the two numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    # Perform the operation based on the user's choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")


# Run the calculator
if __name__ == "__main__":
    calculator()

