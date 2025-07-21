#integer (whole number)
age = 18
print("Age:", age)

#float (decimal number)
temperature = 36.6
print("Temperature:", temperature)

#string (text)
name = "Kashaf"
print("Name:", name)

#boolean (True or False)
is_logged_in = True
print("User logged in:", is_logged_in)

#List (ordered collection which can change)
fruits = ["apple", "mango", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])

#tuple (ordered collection which cannot change)
coordinates = (10.5, 20.3)
print("Coordinates:", coordinates)
print("X:", coordinates[0], "Y:", coordinates[1])

#dictionary
student = {
    "name": "Kahaf",
    "age": 19,
    "grade": "A"
}
print("Student Info:", student)
print("Student Name:", student["name"])

#set (unordered, unique items)
colors = {"red", "blue", "green", "red"}  # 'red' is repeated
print("Colors:", colors)  #duplicates removed automatically

# NoneType: represents no value
result = None
print("Result:", result)
print("Type:", type(result))

#multiple variables
name = "Kashaf"                # string
age = 20                      # int
height = 5.4                  # float
is_student = True             # boolean
subjects = ["Python", "English"]  # list
grades = ("A", "B")           # tuple
profile = {"id": 49, "name": "Kashaf"}  # dictionary
skills = {"Python", "HTML", "CSS"}   # set
print(f"{name} is {age} years old and {height} feet tall.")
print("Subjects:", subjects)
print("Grades:", grades)
print("Profile info:", profile)
print("Skills (no duplicates):", skills)
