# The Dictionary Data Type

# in place of indexes, dictionaries have keys
# A key with it's associated value is called a key-value pair

# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'Size': 23}

# spam = {'name': 'Zophie', 'species': 'cat', 'age': 8}
# test = ['kill', 'monger']

# The keys(), values(), and items() Methods
# spam = {'color': 'red', 'age': 42}

# for v in spam.items():
#     print(v)

# Checking whether a key or value exists in a dictionary

# Inventory = sword = 1, magic potions = 5, gold coins = 3
# Loot = [sword, 10 gold coins, 1 magic potion]

# Checking whether a key or value exists in a dictionary

# value in dictionary.keys()
# spam = {"name": "Adwoa", "age": 28}

# res = "Adwoa" in spam.values()
# print(res)
# res = "age" in spam.keys()
# print(res)

# print("Not in dictionary")
# res = 34 not in spam.values()
# print(res)
# res = "age" not in spam.keys()
# print(res)
# res = "name" in spam
# print(res)
# res = "name" not in spam
# print(res)

# the get() method

# grocceryList = {"yam": 50, "tooth paste": 30, "cookies": 21}

# item = input('type item to search for\n')

# # if item not in grocceryList.keys():
# #     print("There is no item such as " + item + " on your list")
# # else:
# #     print(grocceryList[item])

# print("You need to buy " + str(grocceryList.get(item, 0)) + " " + item + " in the list")

# the setdefault() method
# items = {"item1": "value One"}

# items["item2"] = "value Two"
# print(items.setdefault('item2', 'value Three'))
# print(items.get('item2', 'Error message'))
# print(items);

# spam = {'name': 'Pokey', 'age': 5}
# print(spam)
# spam.setdefault('color', 'green')
# print(spam)
# spam.setdefault('color', 'white')
# print(spam)

inventory = {"Sword": 1, "Magic Wand": 5}
loot = [
    {"Sword": 1}, 
    {"Health Potion": 1}, 
    {"Health Potion": 1}, 
    {"Magic Feather": 1}, 
    {"Health Potion": 1}
]

print("Initial Inventory: ")
print(inventory)
print('')
print("After Killing First Boss: ")
print("Loot Dropped: ")
print(loot)
print('')

for i in loot: # Iterate through the loot
    for j in i.items():
        print(f"Picked up {j}")

        itemList = list(j) # Convert the tuple of key - value pair to a list of key - value pair

        key = itemList[0]
        itemVal = itemList[1]

        inventory.setdefault(key, 0) # Make sure the key exists in the dictionary
        inventory[key] = inventory[key] + itemVal # Add the value of loot item to the inventory

print(inventory)

# Question:
# Here is a short program that counts the number of occurrences of each letter in a string.

# message: 'It was a bright cold day in April, and the clocks were striking thirteen.'
# output: {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i': 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}