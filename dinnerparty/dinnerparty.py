import random

num_of_friends = int(input('Enter the number of friends joining (including you):\n'))

if num_of_friends <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    friends = {input('> '): 0 for _ in range(num_of_friends)}

    total_amount = int(input('Enter the total amount:\n'))
    split_amount = round(total_amount / num_of_friends, 2)
    friends = {name: split_amount for name in friends}

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_choice == 'Yes':
        lucky_one = random.choice(list(friends.keys()))
        print(f'{lucky_one} is the lucky one!')
        split_amount = round(total_amount / (num_of_friends - 1), 2)
        for name in friends:
            friends[name] = 0 if name == lucky_one else split_amount
        print(friends)
    else:
        print('No one is going to be lucky')
        print(friends)
