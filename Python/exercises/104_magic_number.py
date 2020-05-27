# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# We should define/assign number to a variable called magic_number
import random
hidden = random.randrange(1,201)
guess= int(input("Please enter your guess: "))

if guess == hidden:
    print("Hit!")
    print(hidden)
elif guess < hidden:
    print("Your guess is too low")
    print(hidden)
else:
    print("Your guess is too high")
    print(hidden)
# magic_number =

# I need to ask user for input


# I need to check if this input matches a magic_number


# I need to let the user know if the response was right or not
#self five

magic_number = int(input("Enter your magic number guess:"))

if magic_number == 17:
    print('Congratulations, you entered the correct number and won!')
else:
    print('Oh no! You did not win this time')

