import random

DEFAULT_OPTIONS = ["rock", "paper", "scissors"]

def load_rating(name):
    try:
        with open("rating.txt", "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2 and parts[0] == name:
                    return int(parts[1])
    except FileNotFoundError:
        pass
    return 0

def get_losers(options, choice):
    """Повертає множину варіантів, які програють вибраному."""
    n = len(options)
    idx = options.index(choice)
    # беремо варіанти після choice + варіанти до choice
    rotated = options[idx + 1:] + options[:idx]
    # друга половина програє вибраному
    return set(rotated[n // 2:])

def get_result(options, user, computer):
    if user == computer:
        return "draw"
    elif computer in get_losers(options, user):
        return "win"
    else:
        return "lose"

name = input("Enter your name: ").strip()
print(f"Hello, {name}")

score = load_rating(name)

raw = input("> ").strip()
options = [o.strip() for o in raw.split(",")] if raw else DEFAULT_OPTIONS

print("Okay, let's start")

while True:
    user = input("> ").strip()

    if user == "!exit":
        print("Bye!")
        break
    elif user == "!rating":
        print(f"Your rating: {score}")
    elif user in options:
        computer = random.choice(options)
        result = get_result(options, user, computer)
        if result == "draw":
            print(f"There is a draw ({computer})")
            score += 50
        elif result == "win":
            print(f"Well done. The computer chose {computer} and failed")
            score += 100
        else:
            print(f"Sorry, but the computer chose {computer}")
    else:
        print("Invalid input")