#--File for reading our first json file and printing some of its information.

import json
import termcolor

# -- Open the json file
f = open("person.json", 'r')

# Read the da
# ta from the file
# Now person is a dictionary with all the information
person = json.load(f)

# Print the information in the object
print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")
print(person['age'])
