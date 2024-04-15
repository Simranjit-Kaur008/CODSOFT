def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b==0:
        return "Error!! Cannot divide"
    else:
        return a / b
print("CALCULATOR")
print("Select Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice from 1,2,3,4: ")
number1 = float(input("Enter First Number:"))
number2 = float(input("Enter First Number:"))
if choice == '1':
    print("Solution:", add(number1, number2))
elif choice == '2':
    print("Solution:", subtract(number1, number2))
elif choice == '3':
    print("Solution:", multiply(number1, number2))
elif choice == '4':
    print("Solution:", divide(number1, number2))
else:
    print("Invalid Input")