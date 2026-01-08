'''
Write a Python program that takes a name as an input from the user and then creates a function that accepts the same name as a parameter and greets the user.
'''



def greet_user(name):
    print("Hello, " + name + "! Welcome!")
input_name = input("Enter your name: ")
greet_user(input_name)