## Write a program that gives a fortune prediction to players.

import random # import the random module

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes, definitely',
    'Reply hazy, try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

# print(messages[random.randint(0, len(messages) - 1)])
print(random.choice(messages))