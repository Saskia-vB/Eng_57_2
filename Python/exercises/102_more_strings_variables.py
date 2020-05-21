# Practice strings
# Welcome to Sparta - exercise

# Version 1 specs - with concatenation
# define a variable name, and assign a string
name = "Saskia"

# prompt the user for input and ask the user for his/her name
# re assign the original variable this this input
name = str(input("What is your  name?"))
print(name)

# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print("Hello",(name.strip()),"Welcome!")

# Version 2 - with interpolation

# ask the user for a first name, save it in a variable
first_name = str(input("What is your first name?"))
# ask the user for a last name, save it in a variable
last_name = str(input("What is your last name?"))
# use interpolation to print the message

print(f'Hello {first_name} {last_name}, welcome!')


# Calculate year of birth

# gather details on age and name
age = int(input("How old are you?"))
name = str(input("What is your name?"))
from datetime import date
def year_born(age):
        today = date.today()
        return today.year - age
        print(year_born(age))
# print something like
# OMG <person>, you are <age> years old so you were born in <year>