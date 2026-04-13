import random


def generate_full_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def distribute(full_set):
    while True:
        pieces = full_set[:]
        random.shuffle(pieces)
        stock    = pieces[:14]
        computer = pieces[14:21]
        player   = pieces[21:28]

        # знаходимо найбільший дубль
        best = None
        for p in sorted(computer + player, key=lambda x: x[0], reverse=True):
            if p[0] == p[1]:
                best = p
                break

        if best is None:
            continue

        if best in computer:
            computer.remove(best)
            status = "player"
        else:
            player.remove(best)
            status = "computer"

        return stock, computer, player, [best], status


def draw_snake(snake):
    if len(snake) <= 6:
        return "".join(str(p) for p in snake)
    left  = "".join(str(p) for p in snake[:3])
    right = "".join(str(p) for p in snake[-3:])
    return left + "..." + right


def print_board(stock, computer, player, snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print(draw_snake(snake))
    print("\nYour pieces:")
    for i, p in enumerate(player, 1):
        print(f"{i}:{p}")

    if status == "player":
        print("\nStatus: It's your turn to make a move. Enter your command.")
    elif status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    elif status == "win":
        print("\nStatus: The game is over. You won!")
    elif status == "lose":
        print("\nStatus: The game is over. The computer won!")
    elif status == "draw":
        print("\nStatus: The game is over. It's a draw!")


def check_draw(snake):
    left  = snake[0][0]
    right = snake[-1][1]
    if left != right:
        return False
    count = sum(p.count(left) for p in snake)
    return count >= 8


def can_place(piece, end_val):
    return end_val in piece


def place_piece(snake, piece, side):
    """side > 0 — праворуч, side < 0 — ліворуч"""
    p = piece[:]
    if side > 0:
        if p[0] != snake[-1][1]:
            p.reverse()
        snake.append(p)
    else:
        if p[1] != snake[0][0]:
            p.reverse()
        snake.insert(0, p)


def is_valid_move(move, pieces, snake):
    if move == 0:
        return True
    idx = abs(move) - 1
    if idx >= len(pieces):
        return False
    piece = pieces[idx]
    if move > 0:
        return can_place(piece, snake[-1][1])
    else:
        return can_place(piece, snake[0][0])


def player_turn(stock, player, snake):
    while True:
        try:
            move = int(input("> "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if abs(move) > len(player):
            print("Invalid input. Please try again.")
            continue

        if not is_valid_move(move, player, snake):
            print("Illegal move. Please try again.")
            continue

        if move == 0:
            if stock:
                player.append(stock.pop())
        else:
            piece = player.pop(abs(move) - 1)
            place_piece(snake, piece, move)
        break


def score_pieces(pieces, snake):
    all_pieces = pieces + snake
    counts = [0] * 7
    for p in all_pieces:
        counts[p[0]] += 1
        counts[p[1]] += 1

    scored = []
    for i, p in enumerate(pieces):
        s = counts[p[0]] + counts[p[1]]
        scored.append((s, i, p))
    scored.sort(reverse=True)
    return scored


def computer_turn(stock, computer, snake):
    input("> ")
    scored = score_pieces(computer, snake)

    for _, idx, piece in scored:
        # спробувати праворуч
        if can_place(piece, snake[-1][1]):
            computer.pop(idx)
            place_piece(snake, piece, 1)
            return
        # спробувати ліворуч
        if can_place(piece, snake[0][0]):
            computer.pop(idx)
            place_piece(snake, piece, -1)
            return

    # пропустити хід
    if stock:
        computer.append(stock.pop())


def get_game_status(stock, computer, player, snake):
    if not player:
        return "win"
    if not computer:
        return "lose"
    if check_draw(snake):
        return "draw"
    return None


def main():
    full_set = generate_full_set()
    stock, computer, player, snake, status = distribute(full_set)

    while True:
        end = get_game_status(stock, computer, player, snake)
        if end:
            print_board(stock, computer, player, snake, end)
            break

        print_board(stock, computer, player, snake, status)

        if status == "player":
            player_turn(stock, player, snake)
            status = "computer"
        else:
            computer_turn(stock, computer, snake)
            status = "player"


if __name__ == "__main__":
    main()