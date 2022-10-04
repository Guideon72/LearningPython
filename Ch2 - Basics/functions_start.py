#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def bFunct():
    print("A basic function")

# TODO: function that takes arguments


def dFunct(a, b):
    print(a * b)

# TODO: function that returns a value


def rFunct(a, b):
    return a+b

# TODO: function with default value for an argument


def defFunct(a=2, b=5):
    return a-b

# TODO: function with variable number of arguments


def varFunct(*args):
    result = 0
    for x in args:
        result = result + x
    return result


bFunct()
dFunct(3, 7)
print(rFunct(8, 9))
print(defFunct())
print(varFunct(42, 8))
