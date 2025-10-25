import random
import string

def play_game():

    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden = ['-' for _ in word]
    attempts = 8
    guessed = set()

    print('\nHANGMAN')

    while attempts > 0:
        print('\n' + ''.join(hidden))
        letter = input('Input a letter: > ')

        if len(letter) != 1:
            print('You should input a single letter')
            continue
        if letter not in string.ascii_lowercase:
            print('Please enter a lowercase English letter')
            continue
        if letter in guessed:
            print('You\'ve already guessed this letter')
            continue

        guessed.add(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden[i] = letter
        else:
            print('That letter doesn\'t appear in the word')
            attempts -= 1

        if '-' not in hidden:
            print(f'You guessed the word {word}!')
            print('You survived!')
            return

    print('You lost!')

print('HANGMAN')
while True:
    choice = input('Type "play" to play the game, "exit" to quit: > ')
    if choice == 'play':
        play_game()
    elif choice == 'exit':
        break
