# Sequence Data Types
# Sequence data types:
# Lists, Tuples, Strings, Range object

# name = "Adwoa Brocke"

# for i in name:
#     print("******** " + i + " ********" )

# Mutable and Immutable data types
# email = ['k','y','c']
# password = "banku"

# print(email)
# print(password)

# email[1] = 'z'
# print(email)

# #NB: The only way to mutate a string is to slicing and concatenation
# password = password[:2] + 'i' + password[3:]
# print(password)

# The Tuple Data Type
# eggs = ("hello", 42, 25.9)
# print(eggs[0])
# print(eggs[1:3]);
# print(len(eggs))

# # Converting Types with list() and tuple()
# print(tuple(['dog', 'cat', 5]))  

# #Try: convert a tuple to a list

# Reference
# spam = 25
# cheese = spam

# print("Before .....")
# print("Spam: " + str(spam))
# print("Cheese: " + str(cheese))

# spam = 100
# print("After .....")
# print("Spam: " + str(spam))
# print("Cheese: " + str(cheese))
# print("==========================================\n")

# list1 = [0, 1, 2, 3, 4, 5]
# list2 = list1
# print("Before...")
# print(list1)
# print(list2)
# list2[0] = 'Hello'
# print("After...")
# print(f"List1: {list1}")
# print(f"List2: {list2}")
# print("==========================================\n")

# tuple1 = (0, 1, 2, 3, 4, 5)
# tuple2 = tuple1
# print("Before...")
# print(tuple1)
# print(tuple2)
# tuple2 = ('Hello', 1, 2, 3, 4, 5)
# print("After...")
# print(f"List1: {tuple1}")
# print(f"List2: {tuple2}")

# Identity and the id() function
# bacon = "Hello"
# bacon += " World"
# print(id(bacon))
# Automatic Garbage Collector - Deletes any value in memory that is not referenced

# pets = ['cats', 'dogs']
# print(f"Pets: {id(pets)}")
# pets.append('parrot')
# print(f"Pets: {id(pets)}")

# Passing Refereces
# def someFunction (first, second): # Parameters
#     print(first + second)

# numb1 = "King "
# numb2 = "Kong"

# someFunction(numb1, numb2) # Arguments

def anotherFunction (someParameter):
    someParameter.append('Hello')

someVar = [1, 2, 3]
anotherFunction(someVar)
print(someVar)