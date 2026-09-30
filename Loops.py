# FOR LOOPS
# A for loop allows you to repeat a block of code for every item in a sequence.

# Example:
names = ["John", "Mary", "David"]

for name in names:
    print(name)

# Python takes each item from the list one at a time and stores it in the variable name.

# for - Tells Python that you want to create a loop.

# name - This is the loop variable.

# It temporarily stores the current item.

# names - This is the sequence Python will go through.

# : - The colon tells Python that the loop's code is beginning.

# Indentation - The code inside the loop must be indented.


## Using For Loops with Strings
name = "Python"

for letter in name:
    print(letter)

# Using range()
for number in range(5):
    print(number)

# Using if Inside a For Loop
scores = [35, 75, 42, 90, 60, 25]

for score in scores:
    if score > 50:
        print(score)

# Student Grade Example
scores = [85, 45, 72, 30, 90]

for score in scores:

    if score >= 50:
        print(score, "Pass")
    else:
        print(score, "Fail")



### WHILE LOOP
# A while loop is used to repeatedly execute a block of code as long as a condition is true.

# Example
number = 1

while number <= 5:
    print("Hello World", number)
    number = number + 1


# Password Verification
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Login successful!")


### SIMPLE ATM MENU
balance = 50000
choice = ""

while choice != "4":

    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM.")

    else:
        print("Invalid option.")