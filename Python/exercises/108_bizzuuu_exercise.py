# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)
number= int(input("Choose a number:"))
print(range(number(int(input()))))
# print(number(range(int(input())),sep='')
for x in number:
    if (number % 5) == "0":
        print("buzz")
    elif (number % 3)== "0":
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

print ("I'm going to print the numbers!")
i = int(input("Enter the number: "))
func(i)