# Local and Global Scope

# Local Scopes Cannot Use Variables in Other Local Scopes
# def spam():
#     eggs = 99
#     bacon()
#     print("Eggs in spam is: ", eggs)

# def bacon():
#     ham = 101
#     eggs = 0
#     print("Ham in bacon is: ", ham)
#     print("Eggs in bacon is: ", eggs)

# spam()

# Global Variables Can Be Read from a Local Scope
# def spam():
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)

# Local and Global Variables with the Same Name
# def spam():
#     eggs = 'spam local'
#     print(eggs)

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)

# eggs = 'global'
# bacon()
# print(eggs)

# The Global Statement
# The global statement is used to modify a global variable in a function
# Example 1:
# def spam():
#     global eggs
#     eggs = 'spam'
#     print(eggs)

# eggs = 'global'
# spam()
# print(eggs)

# Example 2:
# def spam():
#     global eggs
#     eggs = 'spam' # this is the global

# def bacon():
#     eggs = 'bacon' # this is a local
#     print(eggs)

# def ham():
#     print(eggs) # this is the global

# eggs = 42 # this is the global
# ham()
# spam()
# print(eggs)
# ham()
# bacon()

# Solve this!!!!!
# def spam():
#     print(eggs)
#     eggs = 'spam local'
    
# eggs = 'global'
# spam()


