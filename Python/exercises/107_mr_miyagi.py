# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate responses as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'

question = input("Ask a question")
print("questions are wise, but for now. Wax on, and Wax off!")

# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
if not question.startswith("Sensei"):
    print("You are smart, but not wise - address me as Sensei please")
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remember, best block, not to be there..'
elif x=="block":
    print("Remember, best block, not to be there..")
# anything else you say:
# --> 'do not lose focus. Wax on. Wax off.'
else:
    # question==
    print("do not lose focus. Wax on. Wax off.")

# for x in question:
#     x=="Sensei, I am at peace"

# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'
# while question != "Sensei, I am at peace":
#     print("Sometimes, what heart know, head forget")
# your_response = input('(MR.Miyagi)... -.-')

#  EXTRA:
#  make it run continuously
#  consider best practices of functions - make this functional