# Define the following variables
# name, last_name, age, eye_color, hair_color
name = str(input("What is your first name?"))
# print(name)
last_name = str(input("What is your last name?"))
# print(last_name)
eye_color = str(input("What is your eye color?"))
# print(eye_color)
hair_color = str(input("What is your hair color?"))
# print(hair_color)
age = int(input("What is your age?"))
# Prompt user for input and Re-assign these

# Print them back to the user as conversation

print("Hello",name,last_name,"! Welcome, your age is",age,", your eyes are",eye_color,"and your hair color is",hair_color)
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

from datetime import date
def year_born(age):
        today = date.today()
        return today.year - age
        print(year_born(age))
print("You said you were", age, "hence you were born in", year_born(age))

# age=input('How old are you,' + first_name + '?')
# birthday_gone= input('Has your birthday passed this year? Yes/no')
# if birthday_gone== 'Yes':
#         birthday_gone=0
# else:
#         birthday_gone =1
# birth_year = 2020 - int(age) - birthday_gone

#Extra - Cast your input
#