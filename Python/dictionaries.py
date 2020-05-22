# Dictionaries
# Definition and syntax
# a dictionary is a data structure, like a list, but organized with keys and not index.
# They are organized with 'key' : 'value' pairs
# for example 'zebra' : 'an African wild animal that looks like a horse but has black and white or brown and white lines on its body'
# This means you can search data using keys, rather than index.

#syntax
# {}
# my_dictionary={'key':'value'}
# print(type(my_dictionary))
# i.e.: {'zebra': 'A horse with stripes'}

# Defining a dictionary
# allows you to store more data, the value can be anything, it can be another data structure.
# i.e. for stingy landlords list, we need more info regarding the houses they have and contact details.

stingy_landlord1 = {
    'name':'Alfredo',
    'phone_number':'0783271192',
    'property':'Birmingham, near Star City'
}

# printing dictionary
print(stingy_landlord1)
print(type(stingy_landlord1))

# getting one value out
print(stingy_landlord1['name'])
print(stingy_landlord1['phone_number'])


# re-assigning one value
stingy_landlord1['name'] = "Alfredo de Medo"
print(stingy_landlord1)

# new key value pair
stingy_landlord1['address']="house 2, Unit 29 Watson Rd"
print(stingy_landlord1)

stingy_landlord1['number_of_victimes']=0
print(stingy_landlord1)

stingy_landlord1['number_of_victimes']+=1
print(stingy_landlord1)
stingy_landlord1['number_of_victimes']+=1
print(stingy_landlord1)

# get all the values out

# special dictionary methods
# (methods are functions that belong to a specific data type)

# .keys()
print(stingy_landlord1.keys())

# .values()
print(stingy_landlord1.values())

# .items()
print(stingy_landlord1.items())