#greeting program
name = input("What is your name? ")
print(f"Salam, {name}! Welcome to Python.")

#area of rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area of the rectangle is: {area}")

#age in future
age = int(input("Enter your current age: "))
future_age = age + 10
print(f"In 10 years, you will be {future_age} years old.")

#temperature converter (celsius - farenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
