# LIST AND TUPLES

# List can hold multiple values of the same data type of different data types
# Values in a list a called items
# The items are separated by comas (coma-delimited)
# Items in a list are ordered

# names_of_gf1 = "Adwoa"
# names_of_gf2 = "Ama"
# names_of_gf3 = "Akos"
# names_of_gf4 = "Yaayaa"
# names_of_gf5 = "Abena"

    # Item       1       2       3        4        5
# names = ["Adwoa", "Ama", "Akos", "Yaayaa", "Abena"]
    # Indexes    0       1       2        3        4
    # Indexes   -5      -4      -3       -2       -1
 
# NEGATIVE
# print(tsatsu_gfs[-4])

# Getting a list from another list with slices

# pets = ["bat", "cat", "elephant", "rat"]
# predetors = ["lion", "tiger", "eagle"]

# new_list = test_list[0:-1]

# Getting the length of a list

# length_of_list = len(test_list)
# print(length_of_list)

# for i in range(2, len(test_list)):
#     print('Hello ' + test_list[i])

# For loop
# for i in range(start, end, increment):
# for i in range(20, 0, -1):
#     print(i)

# Changing the values in a list with indexes
# print(pets)
# pets[1] = "parrot"

# print(pets)

# List concatenation and list replication

# concat = pets + predetors
# print(concat)

# replicate = predetors * 3
# print(replicate)

# Remove value from a list
# del - keyword
# list[index]
# print(pets)

# del pets[2]
# print(pets)

# Working with lists

# pet1 = 'cat'
# pet2 = 'dog'
# pet3 = 'parrot'
# pet4 = 'snake'

# print("Enter pet 1")
# pet1 = input()
# print("Enter pet 2")
# pet2 = input()
# print("Enter pet 3")
# pet3 = input()
# print("Enter pet 4")
# pet4 = input()

# print('My pets are: ')
# print(pet1 + ' ' + pet2 + ' ' + pet3 + ' ' + pet4 + ' ')

# my_pets = []
# while True:
#     print('Enter pet ' + str(len(my_pets) + 1) + " or nothing to stop")
#     pet_type = input()
#     if pet_type == '':
#         break
#     my_pets = my_pets + [pet_type]

# print('My pets are: ')
# for i in range(len(my_pets)):
#     print(my_pets[i], end= ' ')

# AUGMENTED ASSIGNMENT OPERATORS

# var += 1 ( + = )
# var -= 1 ( - = )
# var *= 2 ( * = )
# var /= 2 ( / = )
# var %= 3 ( % = )

# Methods 
# A method is the same as a function, except it is "called on" an object or value.

# def testFunc (name):
#     print("Hello, " + name);

# defaultStr = "the bomb";
# capStr = "the bomb".title();

# print(defaultStr)
# print(capStr)
# testFunc('Brocke')

# Finding the index of an item in a list with the index() method
# names = ["Adwoa", "Ama", "Akos", "Yaayaa", "Abena"]
# print(names)

# for i in range(len(names)):
#     if (names[i] == "Yaayaa"):
#         print("Index of " + str(names[i] + " is " + str(i)))

# indexYaaya = names.index("Yaayaa");
# print("Index of Yaaya is " + str(indexYaaya));

# names = names + ["Kojo"]
# print(names)

# Adding items to a list with append() and insert() methods
# animals = ['Cat', 'Dog', 'Bat']
# print(animals)
# # append() adds the item to the end of the list, while insert() adds the item in what ever location/index you specify (But it has to be a valid index/location)
# animals.append('Goat')
# print(animals)

# animals.insert(2, "Camel")
# print(animals)

# Sorting values in a list with the sort method
# spam = [2, 3, 5, 3.14, 1, -7]
# print(f"Before sorting: {spam}")

# spam.sort()
# print(f"After sorting in increasing order: {spam}")

# spam.sort(reverse=True)
# print(f"After sorting in decreasing order: {spam}")

# NOTE: you can't sort mixed data
# ASCIIbetical order - for sorting string

# spam = ['a', 'Z', 'A', 'z']
# x = spam
# spam.sort()
# print(f"Sorted: {spam}")
# lists, sequence, dictionaries are reference values

# def testFunction (l):
#     total = 0
#     for i in range(len(l)):
#         total += l[i]

#     return total

# expectedTotal = testFunction([1, 2, 3, 4, 5])
# print(expectedTotal)

# def testFunction2 (l):
#     for i in range(len(l)):
#         l[i] = l[i] * 2
#     print(l)

# testFunction2([1, 2, 3, 4, 5])
# print(testFunction2([1, 2, 3, 4, 5]))
# x = testFunction2([1, 2, 3, 4, 5])
# print("x is: " + str(x))

# y = print("Kofi")
# print("y is : " + str(y))

## reverse() method to reverse items in a list
# spam = ['cat', 'dog', 'mouse']
# spam2 = [1, 3, 4, 8, 10, 2]
# spam2.reverse()
# spam.reverse()
# print(spam2)
# print(spam)

## Exception to indentation rules in python
# spam = [
#     'cat','dog','mouse',
# ]

# print(spam)

## \ is the continuation character in a string 
print("Brocked left Doris" + \
"because she ate all da pizza" + \
"because he is a foodie!");
     #    0               1                   2
test= [[2, 3, 5], ['a', 'b', 'c'], ['cow', 'hen', 'cat']]

print(test[2][0])






