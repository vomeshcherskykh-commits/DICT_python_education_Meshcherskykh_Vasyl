import sqlite3
import random


def init_db(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS card (
            id      INTEGER PRIMARY KEY,
            number  TEXT    NOT NULL,
            pin     TEXT    NOT NULL,
            balance INTEGER DEFAULT 0
        )
    """)
    conn.commit()


def luhn_checksum(number_str):
    """Повертає контрольну суму за алгоритмом Луна (без останньої цифри)."""
    digits = [int(d) for d in number_str]
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10


def generate_card_number():
    """Генерує 16-значний номер картки, що проходить алгоритм Луна."""
    account_id = str(random.randint(0, 999999999)).zfill(9)
    base = "400000" + account_id        # 15 цифр
    checksum = luhn_checksum(base)
    last_digit = (10 - checksum) % 10
    return base + str(last_digit)


def luhn_valid(number_str):
    """Перевіряє номер картки алгоритмом Луна."""
    digits = [int(d) for d in number_str]
    last = digits.pop()
    digits.reverse()
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return (sum(digits) + last) % 10 == 0


def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)


def create_account(conn):
    cur = conn.cursor()
    while True:
        number = generate_card_number()
        cur.execute("SELECT id FROM card WHERE number = ?", (number,))
        if not cur.fetchone():
            break

    pin = generate_pin()
    cur.execute("INSERT INTO card (number, pin, balance) VALUES (?, ?, 0)", (number, pin))
    conn.commit()
    print("\nYour card has been created")
    print("Your card number:")
    print(number)
    print("Your card PIN:")
    print(pin)


def log_into_account(conn):
    cur = conn.cursor()
    number = input("\nEnter your card number:\n>").strip()
    cur.execute("SELECT id, pin, balance FROM card WHERE number = ?", (number,))
    row = cur.fetchone()
    if not row:
        print("\nWrong card number!")
        return

    pin = input("Enter your PIN:\n>").strip()
    if pin != row[1]:
        print("\nWrong PIN!")
        return

    print("\nYou have successfully logged in!")
    account_menu(conn, number)


def account_menu(conn, number):
    while True:
        print("\n1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        choice = input(">").strip()

        if choice == "1":
            cur = conn.cursor()
            cur.execute("SELECT balance FROM card WHERE number = ?", (number,))
            print(f"\nBalance: {cur.fetchone()[0]}")

        elif choice == "2":
            amount = int(input("\nEnter income:\n>").strip())
            cur = conn.cursor()
            cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, number))
            conn.commit()
            print("Income was added!")

        elif choice == "3":
            do_transfer(conn, number)

        elif choice == "4":
            cur = conn.cursor()
            cur.execute("DELETE FROM card WHERE number = ?", (number,))
            conn.commit()
            print("\nThe account has been closed!")
            return

        elif choice == "5":
            print("\nYou have successfully logged out!")
            return

        elif choice == "0":
            print("\nBye!")
            exit()


def do_transfer(conn, from_number):
    print("\nTransfer")
    to_number = input("Enter card number:\n>").strip()

    if to_number == from_number:
        print("You can't transfer money to the same account!")
        return

    if not luhn_valid(to_number):
        print("Probably you made a mistake in the card number. Please try again!")
        return

    cur = conn.cursor()
    cur.execute("SELECT balance FROM card WHERE number = ?", (to_number,))
    row = cur.fetchone()
    if not row:
        print("Such a card does not exist.")
        return

    amount = int(input("Enter how much money you want to transfer:\n>").strip())

    cur.execute("SELECT balance FROM card WHERE number = ?", (from_number,))
    balance = cur.fetchone()[0]
    if amount > balance:
        print("Not enough money!")
        return

    cur.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (amount, from_number))
    cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, to_number))
    conn.commit()
    print("Success!")


def main():
    conn = sqlite3.connect("card.s3db")
    init_db(conn)

    while True:
        print("\n1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = input(">").strip()

        if choice == "1":
            create_account(conn)
        elif choice == "2":
            log_into_account(conn)
        elif choice == "0":
            print("\nBye!")
            break


if __name__ == "__main__":
    main()