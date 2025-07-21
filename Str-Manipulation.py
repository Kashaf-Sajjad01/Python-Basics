#string manipulation
message = "  Kashaf is learning Python!  "
#clean
cleaned = message.strip()
print("Cleaned:", cleaned)
#convert to uppercase and lowercase
print("Uppercase:", cleaned.upper())
print("Lowercase:", cleaned.lower())
#find the length of the string
print("Length:", len(cleaned))
#replace a word
new_message = cleaned.replace("Python", "programming")
print("Replaced:", new_message)
#slice the string
print("First 5 characters:", cleaned[:5])
print("Last 7 characters:", cleaned[-7:])
#split the string into a list
words = cleaned.split()
print("Words list:", words)
#join words back into a sentence
joined = " | ".join(words)
print("Joined with | :", joined)
#check if word exists
print("Contains 'Python'? :", "Python" in cleaned)
print("Contains 'Java'?    :", "Java" in cleaned)
