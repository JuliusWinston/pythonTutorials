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

grocceryList = {"yam": 50, "tooth paste": 30, "cookies": 21}

item = input('type item to search for\n')

# if item not in grocceryList.keys():
#     print("There is no item such as " + item + " on your list")
# else:
#     print(grocceryList[item])

print("You need to buy " + str(grocceryList.get(item, 0)) + " " + item + " in the list")
