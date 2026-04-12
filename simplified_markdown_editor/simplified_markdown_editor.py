FORMATTERS = [
    "plain", "bold", "italic", "header", "link",
    "inline-code", "ordered-list", "unordered-list", "new-line"
]
SPECIAL_COMMANDS = ["!help", "!done"]


def show_help():
    print("Available formatters: " + " ".join(FORMATTERS))
    print("Special commands: " + " ".join(SPECIAL_COMMANDS))


def get_rows():
    while True:
        try:
            rows = int(input("Number of rows: > "))
            if rows > 0:
                return rows
            print("The number of rows should be greater than zero.")
        except ValueError:
            print("The number of rows should be greater than zero.")


def format_text(formatter, markdown):
    if formatter == "new-line":
        return markdown + "\n"

    if formatter == "plain":
        text = input("Text: > ")
        return markdown + text

    if formatter == "bold":
        text = input("Text: > ")
        return markdown + f"**{text}**"

    if formatter == "italic":
        text = input("Text: > ")
        return markdown + f"*{text}*"

    if formatter == "inline-code":
        text = input("Text: > ")
        return markdown + f"`{text}`"

    if formatter == "header":
        while True:
            try:
                level = int(input("Level: > "))
                if 1 <= level <= 6:
                    break
                print("The level should be within the range of 1 to 6.")
            except ValueError:
                print("The level should be within the range of 1 to 6.")
        text = input("Text: > ")
        return markdown + f"{'#' * level} {text}\n"

    if formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        return markdown + f"[{label}]({url})"

    if formatter == "ordered-list":
        rows = get_rows()
        items = [input(f"Row #{i + 1}: > ") for i in range(rows)]
        return markdown + "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items)) + "\n"

    if formatter == "unordered-list":
        rows = get_rows()
        items = [input(f"Row #{i + 1}: > ") for i in range(rows)]
        return markdown + "\n".join(f"* {item}" for item in items) + "\n"

    return markdown


def main():
    markdown = ""

    while True:
        formatter = input("Choose a formatter: > ").strip()

        if formatter == "!help":
            show_help()
        elif formatter == "!done":
            with open("output.md", "w") as f:
                f.write(markdown)
            break
        elif formatter in FORMATTERS:
            markdown = format_text(formatter, markdown)
            print(markdown)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()