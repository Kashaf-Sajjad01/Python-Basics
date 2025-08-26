#LOCAL VARIABLE
#inside a function
def greet():
    name = "KASHAF"  # local variable
    print("Salam,", name)
greet()

#simple addition
def add_numbers():
    a = 5
    b = 3
    sum = a + b  # local variable
    print("Sum is:", sum)
add_numbers()

#temperature conversion
def convert_to_celsius():
    fahrenheit = 98  # local variable
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)
convert_to_celsius()

#inside a variable
def print_numbers():
    i = 1  # local variable
    while i <= 5:
        print(i)
        i += 1
print_numbers()

#greeting by input
def greet_user():
    username = input("Enter your name: ")  # local variable
    print("Welcome,", username)
greet_user()


#GLOBAL VARIABLE
#inside function
name = "Kashaf"  # global variable
def greet():
    print("Salam,", name)  # using global variable
greet()

#used in multiple functions
message = "Salam"  # global variable
def show_message():
    print("Message:", message)
def change_message():
    global message
    message = "Hi"
show_message()
change_message()
show_message()

#score system
score = 0
def add_points():
    global score
    score += 10
def show_score():
    print("Current Score:", score)
add_points()
add_points()
show_score()

#calculator
result = 0
def add(a, b):
    global result
    result = a + b
add(4, 5)
print("Result:", result)

#boolean global variable
logged_in = False
def login():
    global logged_in
    logged_in = True
def status():
    if logged_in:
        print("User is logged in.")
    else:
        print("User is not logged in.")
status()
login()
status()
