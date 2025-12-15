import random
import chess

def print_board(board: chess.Board) -> None:
    print(board)
    print()

def get_human_move(board: chess.Board) -> chess.Move:
    while True:
        s = input("Your move (UCI, e.g. e2e4, g1f3, e7e8q): ").strip().lower()
        try:
            move = chess.Move.from_uci(s)
        except ValueError:
            print("Bad format. Use UCI like e2e4.")
            continue

        if move in board.legal_moves:
            return move

        print("Illegal move.")

def get_computer_move(board: chess.Board) -> chess.Move:
    return random.choice(list(board.legal_moves))

def main() -> None:
    board = chess.Board()
    print("Text Chess (Python) — You are White.")
    print("Enter moves in UCI (e2e4). Promotion example: e7e8q\n")

    while not board.is_game_over():
        print_board(board)

        if board.turn == chess.WHITE:
            board.push(get_human_move(board))
        else:
            move = get_computer_move(board)
            print(f"Computer plays: {move.uci()}\n")
            board.push(move)

    print_board(board)
    outcome = board.outcome()
    print("Game over:", board.result(), "-", outcome.termination if outcome else "Unknown")

if __name__ == "__main__":
    main()
