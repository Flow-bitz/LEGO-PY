# # A function is a reusable block of code that performs a specific task.
# def welcome():
#     print("Welcome to the student management system")

# welcome()   

# # Functions and Parameters
# def greet(name):
#     print("Hello", name)

# greet("Paul")    # Passing an argument to the parameter/function
# greet('Silas')
# greet('John')

# # Functions with Multiple Parameters
# def sum(num1, num2):
#     print(num1 + num2)

# sum(10, 15)

# # Multiple Parameters with Different Data Types
# def student_info(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)

# student_info("David", 22, "Computer Science")

# # Function with a calculation
# def calculate_area(length, width):
#     area = length * width
#     print("Area:", area)

# calculate_area(10, 5)

# # Returning values from a function
# def add(a, b):
#     return a + b

# result = add(7, 8)
# print(result)

# # Using a function result in another function
# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# result = add(10, 20)

# answer = multiply(result, 2)

# print(answer)

# # Function with User Input
# def greet(name):
#     print("My name is", name)

# name = input("Enter your name: ")

# greet(name)

# # PRACTICAL EXAMPLE: STUDENT GRADE
# def get_grade(score):
#     if score >= 70:
#         return "A"
#     elif score >= 60:
#         return "B"
#     elif score >= 50:
#         return "C"
#     elif score >= 45:
#         return "D"
#     else:
#         return "F"

# score = int(input("Enter your score: "))

# grade = get_grade(score)

# print("Grade:", grade)

# # Default/Optional Arguement
# def greet(name="Student"):
#     print("Hello", name)

# greet()
# greet('David')

# # Arbitrary Arguments (*args)
# def add_numbers(*numbers):
#     total = sum(numbers)
#     return total

# print(add_numbers(10, 20))
# print(add_numbers(10, 20, 30))
# print(add_numbers(5, 10, 15, 20))
# # *args allows the function to receive multiple positional arguments.

# # Keyward Arbitrary Argument (**kwargs)
# # **kwargs allows a function to receive an unknown number of keyword arguments.
# def student_info(**details):
#     print(details)

# student_info(name="David", age=22, course="Computer Science")



# PRACTICAL EXAMPLE: Student Management

def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

scores = [
    int(input("Enter score 1: ")),
    int(input("Enter score 2: ")),
    int(input("Enter score 3: "))
]

average = calculate_average(scores)
grade = get_grade(average)

print("\nStudent:", name)
print("Scores:", scores)
print("Average:", round(average, 2))
print("Grade:", grade)