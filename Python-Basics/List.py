#create a list
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

#access list
numbers = [10, 20, 30, 40, 50]
print("First number:", numbers[0])
print("Last number:", numbers[4])

#add in list
colors = ["red", "green"]
colors.append("blue")
print("Updated colors:", colors)

#add at specific position
languages = ["Python", "Java"]
languages.insert(1, "C++")
print("Languages:", languages)

#remove from list
animals = ["cat", "dog", "rabbit"]
animals.remove("dog")
print("Animals after removal:", animals)

#list length
marks = [88, 76, 92, 85]
print("Total subjects:", len(marks))

#sort and reverse list
numbers = [5, 3, 8, 1]
numbers.sort()       # Ascending
print("Sorted list:", numbers)
numbers.reverse()    # Now descending
print("Reversed list:", numbers)

#sum of list numbers
numbers = [5, 10, 15]
total = sum(numbers)
print("Sum of numbers:", total)

#min max in list
scores = [55, 67, 89, 45]
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

#remove negative numbers during iteration
numbers = [10, -5, 3, -1, 7, -6, 2]
for num in numbers[:]:  #using numbers[:] to create a copy
    if num < 0:
        numbers.remove(num)
print("Updated list (no negative numbers):", numbers)
