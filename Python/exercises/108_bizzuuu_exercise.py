# Write a bizz and zzuu game ##project
user_number= (int(input("please enter a number")))
for i in range(1, user_number + 1):
    print(i)

while True:
    user_number

play = input('Do you want to play BIZZZUUUU?\n')
if play == 'yes':
    user_input = int(input('what number would you like to play to?\n'))
    for num in range(1, user_input + 1):
        if num % 15 == 0:
            print('bizzzuu')
        elif num % 3 ==0:
            print('bizzz')
        elif num % 5 ==0:
            print("zzuuu")
        else:
            print(num)
        break

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)
number= int(input("Choose a number:"))
if (number % 5) == 0:
    print("buzz")
elif (number % 3)== 0:
    print("bizz")
else:
    print("You lost")

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu


#  EXTRA:
#  Make it functional
#  make it so I can it so it can work with 4 and 9 insted of 3 and 5.
    #      make it so it can work with any number!

# print ("I'm going to print the numbers!")
# i = int(input("Enter the number: "))
# func(i)