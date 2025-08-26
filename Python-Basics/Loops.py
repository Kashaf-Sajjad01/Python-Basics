#FOR LOOP
#print numbers
for i in range(1, 6):
    print(i)

#print each char
text = "Python"
for char in text:
    print(char)

#print all items in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#print even numbers (1-10)
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#print sum of number (1-100)
total = 0
for i in range(1, 101):
    total += i
print("Sum is:", total)

#for loop through a dict
student = {"name": "Kashaf", "age": 20, "grade": "A"}
for key in student:
    print(key, ":", student[key])

#count vowels in str
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

#print all odd numbers (1-50)
for i in range(1, 51, 2):
    print(i)

#largest number in a list
numbers = [3, 12, 45, 2, 18]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number is:", largest)
