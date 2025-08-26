#basic greeting program
name = input("Enter your name: ")
print("Salam, {}! Welcome to Python.".format(name))

#multiple variables
name = "Kashaf"
age = 20
print("My name is {} and I am {} years old.".format(name, age))

#basic calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
sum = a + b
print("The sum of {} and {} is {}".format(a, b, sum))

#temperature conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("{}°C is equal to {:.1f}°F".format(celsius, fahrenheit))

#using placeholder
print("Hello, {name}. You are a {role}.".format(name="Kashaf", role="developer"))
