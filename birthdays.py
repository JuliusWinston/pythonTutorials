# This program keeps track of my close friends birthdays

birthdays = {'Adwoa': 'Jun 6', 'Doris': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday information for ' + name)
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
        