# using and managing strings ' ' " "
# single_quotes= 'Look! these are single quotes'
# print(single_quotes)
#
# double_quotes="Martin's double quotes"
# print(double_quotes)
# Double quotes are best practice to avoid confusion, i.e. when using apostrophes
# To use single quotes you need to use /

# string_fixed= ' I said \'Wow!\''
#
# Quote_in_quote = 'I said "Wow!"'
# print(string_fixed)
# print(Quote_in_quote)

# slicing strings: how to take things out of strings

# h e l l o w o r l d !
# 0 1 2 3 4 5 6 7 8 9 10

# Example:
#Hw = "Hello! World"
# print(Hw[7:]) # use slicing to get all the letters after the 7th character
# print(Hw[0:5]) # to get "Hello" or [:6]
# print(len(Hw))  # can only be used for strings

# strip
# white_space = "lot's of space at the end      "
# # to count the spaces:
# print(len(white_space))
# # to not count the spaces at the end (not between the words):
# print(len(white_space.strip()))

# some more methods sub_string
# Example_text = "some text here"
# print(Example_text.count("text"))
# The result is 1, because it is counting text as 1

# Example_text = "some text text text here"
# print(Example_text.count("text"))
# The result is 3, because it is counting 3 times the word text


# Bring everything to lower case:
# Example_text = "Some Text Here"
# print(Example_text.lower())

# Bring everything to upper case:
# Example_text = "some text here"
# print(Example_text.upper())

# To capitalize first letter:
# Example_text = "some text here"
# print(Example_text.capitalize())

# How can we replace text
# Example_text = "some text here"
# print(Example_text.replace("some","plenty"))

# Concatenation & Casting

# x = 2
# y = 5.4
# z = "there's now a number 25.4 unless we put a space in"
# # To print (x+y+z)
# # Concatenation
# print(z+" "+ str(y) +" "+ str(x) +" " + str(x+y))
# print(str(x) + str(y) +z)

# x = "8"
# # find the type of variable
# print(type(x))
# # change it to int
# print(int(x))
# # change it to float
# print(float(x))
# # print all

# Boolean operators
# True and False are the only two types that can be used
# a = True
# b = False
# c = 2
# d = 1
# when you use = your are assigning the value, == you are asking if it is equal
# print(c==d)
# print(c != d)
# print (c <= d)

# Startswith
# greetings = "Hello World!"
# print(greetings.startswith("H"))
# print(greetings.endswith("!"))

# print(bool(None))
# a = True
# b= False
# print((bool(a)))
#
# print(""==None)

# List

# they are organized with index. This means it starts at 0.

# syntax
# []
# print(type([]))
# print(len([]))
# example
# defining a list and assigning it to a variable
my_stingy_landlords = ['Alfredo', 'Betty', 'Joanna', 'Mr. Summersbee', 123, True]
#             index = [   0     ,    1   ,    2     ,      3         ]

# print all of the list
# print(my_cringy_landlords)
# print(type(my_cringy_landlords))

# access on entry of the list
# use the index with the list
# print(my_cringy_landlords[2])
# print(type(my_cringy_landlords[2])) # here the type is a string because the index means the value is Joanna

# special_land_person=my_cringy_landlords[2]
# print(special_land_person)

#accessing the first or last index
# print(my_cringy_landlords[0])
# print(my_cringy_landlords[-1])

# Re-assign an entry
my_stingy_landlords = ['Alfredo', 'Betty', 'Joanna', 'Mr. Summersbee', 123, True]
print(my_stingy_landlords)
my_stingy_landlords[-2] = "Patrick"
print(my_stingy_landlords)
my_stingy_landlords[-1]= "Hotel of Mum and Dad"
print(my_stingy_landlords)

# Remove an entry from a list
# remove "Hotel of Mum and Dad"
my_stingy_landlords.pop()
print(my_stingy_landlords)
# add an entry to the list
my_stingy_landlords.append('Filipe Paiva')
print(my_stingy_landlords)
# Filipe Paiva to the list

# Remove entry and index 3
# what method?
# where in the documentation
## include 2 Joannas
my_stingy_landlords.append('Joanna')
print(my_stingy_landlords)
# delete entry
my_stingy_landlords.remove('Joanna')
# With a pop you can indicate index
my_stingy_landlords.pop(3)
print(my_stingy_landlords)