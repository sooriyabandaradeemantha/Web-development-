"""
Write a Python program that will take a number as an input from the user and then creates a function that accepts the same number as a parameter and returns its absolute value. (Example - a negative number is converted to a positive number, the positive number remains the same).
"""



def num(number):
    return abs(number)

input_num = int(input("Enter a number: "))
num(input_num)
print("the absolute value is:", num(input_num))



