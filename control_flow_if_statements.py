import time


# Control Flow

# control flow dictates where the code will run.
# Much like dams in real life.
# In coding we do this with <if> functions and while loops. We're going to look at if functions.


# If functions
# if functions work with booleans (True or False)
# we usually use comparison operators to equate and compare objects, and result in True or False (booleans).

# syntax of if function:
# if <condition>:
#   block of code: is a section of code that runs, it is defined by indentation


# is_rainy = True
#
#
# # if is_rainy:
#     #print('bring umbrella')
#
# if True:
#     time.sleep(2)
#     print('bring umbrella')
# elif <second_condition>:
#   run this block of code
# else:
#   block of code

# weather = 'wind'
#
# if weather == 'rainy':
#     print('bring umbrella')
# elif weather == 'stormy':
#     print('Stay at home!')
# else:
#     print('put on sun lotion')


# logical and
# syntax
# <condition> and <condition>
# both sides need to result in true to be true
# print(True and True)
# print(True and False)



# logical or
# syntax
# <condition> or <condition>
# only one side needs to be true, to result in true
# print(True or False)
# print(False or False)



weather = 'stormy'
safety_alert = 'red'

if weather == 'stormy' and safety_alert == 'red':
    print('duck for cover')
elif weather == 'rainy':
    print('bring umbrella')
elif weather == 'stormy':
    print('Stay at home!')
else:
    print('put on sun lotion')

# if you need to check everything you can write multiple ifs:
# if <condition>
#    print('this was true')
# if <condition>
#   print('this was true')