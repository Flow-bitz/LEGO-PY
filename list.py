# # A list is a collection of multiple values stored in a single variable.

# names = ["David", "John", "Mary", "Peter"]

# # Accessing List Items
# fruits = ["Apple", "Orange", "Mango", "Banana"]

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

# # Negative Indexing
# # Python also allows us to access items from the end of a list using negative numbers.
# print(fruits[-1]) # Banana
# print(fruits[-2]) # Mango

# Changing List Items
fruits1 = ["Apple", "Orange", "Mango"]
fruits1[1] = "Banana"
print(fruits1)

# Changing Multiple Items
fruits2 = ["Apple", "Orange", "Mango", "Banana"]
fruits2[1:3] = ["Pineapple", "Watermelon"]
print(fruits2)

# Adding Items With append()
fruits3 = ["Apple", "Orange"]
fruits3.append("Mango")
print(fruits3)

# Adding an Item With insert()
fruits4 = ["Apple", "Mango"]
fruits4.insert(1, "Orange")
print(fruits4)

# Adding Multiple Items With extend()
fruits5 = ["Apple", "Orange"]
fruits5.extend(["Mango", "Banana", "Pineapple"])
print(fruits5)

# Removing an Item With remove()
fruits6 = ["Apple", "Orange", "Mango"]
fruits6.remove("Orange")
print(fruits6)

# Removing an Item With pop()
fruits7 = ["Apple", "Orange", "Mango"]
fruits7.pop(1)
print(fruits7)

# Deleting Items With del
fruits8 = ["Apple", "Orange", "Mango"]
del fruits8[1]
print(fruits8)

# You can also delete multiple items:
fruits9 = ["Apple", "Orange", "Mango", "Banana"]
del fruits9[1:3]
print(fruits9)

# Clearing a List
fruitss = ["Apple", "Orange", "Mango"]
fruitss.clear()
print(fruitss)

# Finding the Length of a List
fruitz = ["Apple", "Orange", "Mango", "Banana"]
print(len(fruitz))

# Checking if an Item Exists
fruitz2 = ["Apple", "Orange", "Mango"]
print("Apple" in fruitz2)