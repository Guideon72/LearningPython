#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10/0
# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    x = 10/0
except:
    print("That's not it!")

# TODO: You can also catch specific exceptions

try:
    answer = input("What number should I divide 10 by? ")
    print(10 / int(answer))
except ZeroDivisionError as e:
    print("Cannot divide by zero without ending all of humanity.")
except ValueError as e:
    print("Did not receive a valid number from the user.")
finally:
    print("You can clean up during this Finally block.")
