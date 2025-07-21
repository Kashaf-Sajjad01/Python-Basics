#number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#grade checker
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

#age group
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#simple login
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "Kashaf" and password == "12345":
    print("Login successful!")
else:
    print("Invalid credentials.")

#number comparison
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print("Both numbers are equal.")

#DECISION MAKING PROGRAM
print("Welcome to the Decision Maker!")
print("Let's help you decide if you should go out today.\n")
weather = input("Is it raining? (yes/no): ").lower()
have_umbrella = input("Do you have an umbrella? (yes/no): ").lower()
busy = input("Are you busy with work or study? (yes/no): ").lower()
if weather == "no" and busy == "no":
    print("\n✅ Go out and enjoy your day!")
elif weather == "yes" and have_umbrella == "yes" and busy == "no":
    print("\n☔ Take your umbrella and go out.")
elif busy == "yes":
    print("\n📚 You should probably stay in and finish your work.")
else:
    print("\n❌ Better to stay home for now.")
print("\nThanks for using the Decision Maker App!")
