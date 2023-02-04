# The Collatz Sequence

# (Amazingly enough, this sequence actually works for any integer—sooner or
# later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure
# why. Your program is exploring what’s called the Collatz sequence, sometimes
# called “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with
#the int() function; otherwise, it will be a string value.
# Hint: An integer number is even if number % 2 == 0, and it’s odd if
# number % 2 == 1.
# 
# The output should look like this:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# Second part:
# Input Validation
# Add try and except statements to the previous project to detect whether the
# user types in a noninteger string. Normally, the int() function will raise a
# ValueError error if it is passed a noninteger string, as in int('puppy'). In the
# except clause, print a message to the user saying they must enter an integer.


# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
def collatz (number):
    if (number%2 == 0):
        output_rusults = number//2
        print (output_rusults)
        return output_rusults

    elif (number%2 == 1):
        output_rusults = 3 * number + 1
        print (output_rusults)
        return output_rusults

# Then write a program that lets the user type in an integer and that
# keeps calling collatz() on that number until the function returns the value 1.

# print('please enter a number')
# number =int(input())
# Second part:
# Input Validation
# Add try and except statements to the previous project to detect whether the
# user types in a noninteger string. Normally, the int() function will raise a
# ValueError error if it is passed a noninteger string, as in int('puppy'). In the
# except clause, print a message to the user saying they must enter an integer.


# Write a function named collatz() that has one parameter named number. If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# def collatz (number):
#     if (number % 2 == 0):
#         output_results = number//2
#     else:
#         output_results = 3 * number + 1

#     return output_results

# Then write a program that lets the user type in an integer and that
# keeps calling collatz() on that number until the function returns the value 1.

print('please enter a number')
r_number =int(input())

# Collatz with recursion
# def collatz(number):
#     if number % 2 == 0:
#         results = number // 2
#     else:
#         results = 3 * number + 1
    
#     print(results)

#     if results > 1:
#         results = collatz(results)

#     return results

# collatz(r_number)