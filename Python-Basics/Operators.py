# Arithmetic operations
a = 10
b = 3
print("a =", a)
print("b =", b)
print("Addition       (a + b) =", a + b)
print("Subtraction    (a - b) =", a - b)
print("Multiplication (a * b) =", a * b)
print("Division       (a / b) =", a / b)
print("Modulus        (a % b) =", a % b)

# Comparison operations
x = 5
y = 8
print("x =", x)
print("y =", y)
print("x == y :", x == y)   # Equal to
print("x != y :", x != y)   # Not equal to
print("x > y  :", x > y)    # Greater than
print("x < y  :", x < y)    # Less than
print("x >= y :", x >= y)   # Greater than or equal to
print("x <= y :", x <= y)   # Less than or equal to

# Assignment operators
num = 10
print("Initial value:", num)
num += 5   # same as num = num + 5
print("After += 5 :", num)
num -= 2   # same as num = num - 2
print("After -= 2 :", num)
num *= 3   # same as num = num * 3
print("After *= 3 :", num)
num /= 2   # same as num = num / 2
print("After /= 2 :", num)
num %= 4   # same as num = num % 4
print("After %= 4 :", num)
num **= 2  # same as num = num ** 2
print("After **= 2:", num)
num //= 3  # same as num = num // 3
print("After //= 3:", num)

#CALCULTOR
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y if y != 0 else "Error: Cannot divide by zero"
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
print("Simple Calculator") #display
print("Operations: +  -  *  /")
op = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = operations.get(op, lambda x, y: "Invalid operator")(num1, num2)
print("Result:", result)

#logical operators
#AND (number between 10 and 50)
num = int(input("Enter a number: "))
if num >= 10 and num <= 50:
    print("The number is between 10 and 50.")
else:
    print("The number is outside the range.")

#check for eligbility
age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ") == "yes"
if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

#OR (number is negative or greater than 100)
num = int(input("Enter a number: "))
if num < 0 or num > 100:
    print("The number is either negative or greater than 100.")
else:
    print("The number is between 0 and 100.")

#NOT (user is admin or not)
user_role = input("Enter your role: ")
if not user_role == "admin":
    print("Access denied. You are not an admin.")
else:
    print("Welcome, admin!")

#AND & NOT (password is valid or not)
password = input("Enter your password: ")
# Check if password is not empty and at least 6 characters long
if password and len(password) >= 6:
    print("Password is valid.")
else:
    print("Invalid password.")
