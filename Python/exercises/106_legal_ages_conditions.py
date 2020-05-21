# age = 19
# driver_lisence = True

# - You can vote and drive
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!
age = int(input("How old are you?"))
if age==21:
    print('You can vote and drive')
elif age==18:
    print('You can vote')
elif age==16:
    print('You can drive')
elif age>16:
    print("You can't legally dring but your mates might have your back")
else:
    print("You're are too young, go back to school!")


