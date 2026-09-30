# # CONDITIONAL STATEMENTS
# A conditional statement allows Python to check a condition and perform an action based on the result.

# IF STATEMENT

age = 20

if age >= 18:
    print("You are an adult.")

# Using if with user input
age1 = int(input("Enter your age: "))

if age1 >= 18:
    print("You are an adult.")

# ELSE STATEMENT
# else allows us to specify what should happen when the if condition is false.
age2 = int(input("Enter your age: "))

if age2 >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Using NotEqual
password = "python123"

if password != "admin123":
    print("Wrong Password")
else:
    print("Correct Password")


# ELIF STATEMENT
# This is used for more than two possible outcomes
score = int(input("Enter your score:"))

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Grade F")


# # CHECKING EVEN AND ODD NUMBERS
number01 = int(input("Enter a number: "))

if number01 % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Combining Conditions
# Using AND
age = 25

if age >= 13 and age <= 17:
    print("You are a teenager.")
else:
    print("Non-teenager")

# Using OR
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")

# Using NOT
# NOT operator Reverses a condition.
logged_in = False

if not logged_in:
    print("Please log in.")



# # PRACTICAL EXAMPLES

# Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid username or password.")


# ATM Withdrawal
balance = 50000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful.")
    print("Remaining balance:", balance - amount)
else:
    print("Insufficient funds.")


# Simple calculator with conditions
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Answer:", number1 + number2)

elif operator == "-":
    print("Answer:", number1 - number2)

elif operator == "*":
    print("Answer:", number1 * number2)

elif operator == "/":
    print("Answer:", number1 / number2)

else:
    print("Invalid operator.")


