import random

def ask_pencils():

    while True:

        n = input('How many pencils would you like to use:\n')
        if not n.isdigit():
            print('The number of pencils should be numeric')
            continue

        n = int(n)
        if n <= 0:
            print('The number of pencils should be positive')
            continue

        return n


def ask_first(players):

    while True:

        name = input(f'Who will be the first ({players[0]}, {players[1]}):\n')
        if name not in players:
            print(f"Choose between '{players[0]}' and '{players[1]}'")
            continue

        return name


def ask_move(name, remaining):

    while True:

        move = input(f"{name}'s turn:\n")
        if move not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            continue

        move = int(move)
        if move > remaining:
            print('Too many pencils were taken')
            continue

        return move


def bot_move(remaining):


    if remaining % 4 == 0:
        move = 3
    elif remaining % 4 == 3:
        move = 2
    elif remaining % 4 == 2:
        move = 1
    else:
        move = random.randint(1, 3)

    return move


players = ['John', 'Jack']
num = ask_pencils()
current = ask_first(players)

print('|' * num)

while num > 0:

    if current == 'Jack':  # бот
        print("Jack's turn:")
        move = bot_move(num)
        print(move)

    else:
        move = ask_move(current, num)

    num -= move
    if num > 0:
        print('|' * num)

    current = players[1] if current == players[0] else players[0]

print(f'{current} won!')
