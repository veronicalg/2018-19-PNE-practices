#--File for printing information about different people from personn.json file

import json
import termcolor

# -- Open the json file
f = open("personn.json", 'r')

# Read the data from the file
# Now people_dict is a dictionary with all the information (3 people)
people_dict = json.load(f)

#--For printing the total people in the data base
print("Total people in the data base: ", len(people_dict["People"]))

#--Returns the list of people saved in the keyword people of the json file.
people_list = people_dict["People"]

#--Making a loop for printing all information.
for person in people_list:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])
