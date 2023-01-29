# Exception Handling - Python
# Error Handling in other languages - Most other languages

# def spam(divideBy):
#     return 42/divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# Using exception handling
# syntax: try - keyword, :, code to run, except - keyword, error name - expected, :, follow with code to execute when the error actually happens

# Example 1:
# def spam(divisor):
#     try:
#         return 42/divisor
#     except ZeroDivisionError:
#         print('Error: Invalid divisor')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# Example 2:
def spam(divisor):
    return 42/divisor

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1)) 
except ZeroDivisionError:
    print('Error: Invalid divisor')