# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????

example_xmas = ['walkie talkies', 'socks', 'lynx']

cookies_recipe = ['flour', 'eggs', 'milk','sugar','chocolate chips']

# Print the lists and check it's type
print(cookies_recipe)
print(type(cookies_recipe))

# Print the list's first object
print(cookies_recipe[0])

# Print the list's second object
print(cookies_recipe[1])

# Print the list's last object
print(cookies_recipe[-1])

# Re-define the first item on the list and
cookies_recipe[0] = "self raising flour"

# Re-define another item on the list and print all the list
cookies_recipe[1] = "Free range eggs"
print(cookies_recipe)
# Add an item to the list and print the list
cookies_recipe.append('peanut butter')
print(cookies_recipe)
# Remove an item from the list and print the list
cookies_recipe.pop()
print(cookies_recipe)

# Add two items to list and print the list
cookies_recipe.append('almonds')
cookies_recipe.append('white chocolate')
print(cookies_recipe)

example_xmas.append('iphone')
example_xmas.append('money for icecream')
print(example_xmas)