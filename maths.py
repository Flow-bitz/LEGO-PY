# Python Arithmetic Operators

# Addition = +
# Subtraction = - 
# Multiplication = *
# Division = /
# Floor Division = //
# Remainder/Modulus = %
# Power/Exponent = **



# IMPORTANT MATHS FUNCTIONS

# math.sqrt() =	Square root
# math.pow()	= Power
# math.ceil()	= Round upward
# math.floor()	= Round downward
# math.factorial() =	Factorial

import math

answer = math.pow(2, 3)

print(answer)


# Random Numbers
import random

number = random.randint(1, 10)

print(number)


# Practical Example: Simple Calculator

number1 = 20
number2 = 5

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# INPUT
name = input("Enter your name: ")
country = input("Enter your country: ")
school = input("Enter your school: ")

print("Name:", name)
print("Country:", country)
print("School:", school)

# Even if the user enters a number, input() normally treats it as a string.


# Converting Input to an Integer

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

answer = number1 + number2

print("Answer:", answer)


# Getting Decimal Numbers

price = float(input("Enter the price: "))

print("Price:", price)


# Combining Input With Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("You are", age, "years old.")
print("Next year you will be", age + 1)

# Using Input With f-strings
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")