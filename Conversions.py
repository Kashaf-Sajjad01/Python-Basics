#convert str to int
num_str = "100"
num_int = int(num_str) # Convert to integer
print(f"String: {num_str} (type: {type(num_str)})")
print(f"Integer: {num_int} (type: {type(num_int)})")

#int to str
age = 25
age_str = str(age)
print(f"Integer: {age} (type: {type(age)})")
print(f"String after conversion: {age_str} (type: {type(age_str)})")

#float to int
pi = 3.14159
pi_int = int(pi) #decimal part is removed
print(f"Float: {pi} (type: {type(pi)})")
print(f"Integer after conversion: {pi_int} (type: {type(pi_int)})")

#str to float
price_str = "99.99"
price_float = float(price_str)
print(f"String: {price_str} (type: {type(price_str)})")
print(f"Float: {price_float} (type: {type(price_float)})")

#bool to int
is_active = True
is_deleted = False
print(f"True as integer: {int(is_active)}")   # Output: 1
print(f"False as integer: {int(is_deleted)}") # Output: 0

#adding two numbers with type conversion
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum is: {sum}")
