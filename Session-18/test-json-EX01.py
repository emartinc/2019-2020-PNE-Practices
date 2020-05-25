import json
import termcolor
from pathlib import Path

# Reading the json file
jsonstring = Path("people-EX01.json").read_text()

# Creating the object person from the json string
people = json.loads(jsonstring)

for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phoneNumbers = person['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for element, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(element), 'blue')

        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])