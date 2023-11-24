# Function
def add(num1,num2):
    """
    This function adds one number to another number and returns the result!
    :param num1: This is any number
    :param num2: This is any number 
    """
    return num1 + num2

def subtract(num1, num2):
    """
    This function substract one number to another number and returns the result!
    :param num1: This is any number
    :param num2: This is any number 
    """
    return num1 - num2

def multiply(num1, num2):
    """
    This function multiply one number to another number and returns the result!
    :param num1: This is any number
    :param num2: This is any number 
    """
    return num1 * num2

def divide(num1, num2):
    """
    This function divide one number to another number and returns the result!
    :param num1: This is any number
    :param num2: This is any number accept 0,else it will return "Cannot divide by zero"
    """
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

def expo(num1, num2):
    """
    This function takes one number to the power of another number and returns the result!
    :param num1: This is the Base
    :param num2: This is the exponent 
    """
    return num1 ** num2 
