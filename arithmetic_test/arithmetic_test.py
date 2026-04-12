import random

LEVELS = {
    1: "simple operations with numbers 2-9",
    2: "integral squares of 11-29"
}

def choose_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        try:
            level = int(input("> "))
            if level in LEVELS:
                return level
            print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

def generate_task(level):
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        question = f"{a} {op} {b}"
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        else:
            answer = a * b
        return question, answer
    else:
        a = random.randint(11, 29)
        return str(a), a ** 2

def ask_task(level):
    question, correct = generate_task(level)
    print(question)

    while True:
        try:
            user = int(input("> "))
            break
        except ValueError:
            print("Wrong format! Try again.")

    if user == correct:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False

def save_result(name, score, level):
    with open("results.txt", "a") as f:
        f.write(f"{name}: {score}/5 in level {level} ({LEVELS[level]}).\n")
    print('The results are saved in "results.txt".')

def main():
    level = choose_level()
    score = 0

    for _ in range(5):
        if ask_task(level):
            score += 1

    print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
    answer = input("> ").strip()

    if answer.lower() in ("yes", "y"):
        print("What is your name?")
        name = input("> ").strip()
        save_result(name, score, level)
    else:
        return

if __name__ == "__main__":
    main()