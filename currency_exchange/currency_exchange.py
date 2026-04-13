import requests

def get_rates(code):
    url = f"http://www.floatrates.com/daily/{code.lower()}.json"
    response = requests.get(url)
    return response.json()

base = input("> ").strip().upper()
data = get_rates(base)

cache = {}
if base != "USD":
    cache["USD"] = data["usd"]["rate"]
if base != "EUR":
    cache["EUR"] = data["eur"]["rate"]

while True:
    target = input("> ").strip().upper()
    if not target:
        break

    amount = float(input("> ").strip())

    print("Checking the cache...")

    if target == base:
        result = amount
        print(f"You received {round(result, 2)} {target}.")
        continue

    if target in cache:
        print("It is in the cache!")
        rate = cache[target]
    else:
        print("Sorry, but it is not in the cache!")
        rates = get_rates(base)
        rate = rates[target.lower()]["rate"]
        cache[target] = rate

    result = round(amount * rate, 2)
    print(f"You received {result} {target}.")