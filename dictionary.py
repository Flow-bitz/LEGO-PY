student = {
    "name": ["John", "Mary", "David"],
    "age": 20,
    "course": "Computer Science"
}

#print(student["name"][1])

print(student.get("location", "Abuja"))     
# It provides a default value if the key is not found in the dictionary.

# Adding items to a dictionary
student["Country"] = "Nigeria"
print(student)

# Changing items in a dictionary
student["age"] = 21
print(student)

# Removing items from a dictionary using pop()
student.pop("course")

# Removing items from a dictionary using del
del student["Country"]

# Removing items from a dictionary using clear()
student.clear()

# Checking if a key exists in a dictionary
if "name" in student:
    print("Key exists.")

# using not in to check if a key does not exist in a dictionary
if "location" not in student:
    print("Key does not exist.")