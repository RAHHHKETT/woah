print("Calculator (Addition Only)")

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 + num2
    print("Sum:", result)

    choice = input("Do you want to add again? (y/n): ")
    if choice.lower() != 'y':
        print("Calculator stopped.")
        break
