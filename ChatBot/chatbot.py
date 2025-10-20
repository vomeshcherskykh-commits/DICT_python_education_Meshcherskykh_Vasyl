BOT_NAME = 'DICT_Bot'
BIRTH_YEAR = 2025

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input('> '))
    rem5 = int(input('> '))
    rem7 = int(input('> '))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count_to_number():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input('> '))
    for i in range(0, num + 1):
        print(f'{i} !')

def programming_test():
    print("Let's test your programming knowledge.")
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')

    while True:
        answer = input('> ')
        if answer.strip() == '2':
            print('Completed, have a nice day!')
            break
        else:
            print('Please, try again.')

def main():
    print(f'Hello! My name is {BOT_NAME}.')
    print(f'I was created in {BIRTH_YEAR}.')
    print('Please, remind me your name.')
    name = input('> ')
    print(f'What a great name you have, {name}!')
    guess_age()
    count_to_number()
    programming_test()
    print('Congratulations, have a nice day!')

if __name__ == '__main__':
    main()