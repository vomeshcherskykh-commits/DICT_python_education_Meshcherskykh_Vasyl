import math
import argparse

def format_months(n):
    years = n // 12
    months = n % 12
    parts = []
    if years == 1:
        parts.append("1 year")
    elif years > 1:
        parts.append(f"{years} years")
    if months == 1:
        parts.append("1 month")
    elif months > 1:
        parts.append(f"{months} months")
    return " and ".join(parts)

def validate(args):
    # --type обов'язковий і має бути annuity або diff
    if args.type not in ("annuity", "diff"):
        return False
    # --interest обов'язковий завжди
    if args.interest is None:
        return False
    # від'ємні значення заборонені
    for val in [args.principal, args.payment, args.periods, args.interest]:
        if val is not None and val < 0:
            return False
    # diff + payment — недопустима комбінація
    if args.type == "diff" and args.payment is not None:
        return False
    # має бути рівно 3 відомих параметри (4-й розраховується)
    # для diff: principal, periods, interest (payment не рахується)
    # для annuity: будь-які 3 з principal, payment, periods + interest
    if args.type == "diff":
        known = sum(x is not None for x in [args.principal, args.periods, args.interest])
        if known < 3:
            return False
    else:
        known = sum(x is not None for x in [args.principal, args.payment, args.periods, args.interest])
        if known < 4:
            return False
    return True

parser = argparse.ArgumentParser()
parser.add_argument("--type",      type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--payment",   type=float)
parser.add_argument("--periods",   type=int)
parser.add_argument("--interest",  type=float)
args = parser.parse_args()

if not validate(args):
    print("Incorrect parameters")
    exit()

i = args.interest / (12 * 100)

if args.type == "diff":
    P = args.principal
    n = args.periods
    total = 0
    for m in range(1, n + 1):
        dm = math.ceil(P / n + i * (P - P * (m - 1) / n))
        total += dm
        print(f"Month {m}: payment is {dm}")
    overpayment = round(total - P)
    print(f"\nOverpayment = {overpayment}")

elif args.type == "annuity":
    if args.principal is None:
        # розрахувати основну суму
        A = args.payment
        n = args.periods
        P = round(A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        overpayment = round(A * n - P)
        print(f"Your loan principal = {P}!")
        print(f"Overpayment = {overpayment}")

    elif args.periods is None:
        # розрахувати кількість місяців
        P = args.principal
        A = args.payment
        n = math.ceil(math.log(A / (A - i * P), 1 + i))
        overpayment = round(A * n - P)
        print(f"It will take {format_months(n)} to repay this loan!")
        print(f"Overpayment = {overpayment}")

    elif args.payment is None:
        # розрахувати щомісячний платіж
        P = args.principal
        n = args.periods
        A = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
        overpayment = round(A * n - P)
        print(f"Your annuity payment = {A}!")
        print(f"Overpayment = {overpayment}")