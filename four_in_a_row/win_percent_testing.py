import random
from monte_carlo import Board, simulate


def pure_mc(board: Board, n=200):
    """Monte Carlo."""
    win_counts = dict((move, [0, 0, 0]) for move in board.available_moves)
    for move in board.available_moves:
        for _ in range(n):
            result = simulate(board.copy(), move)
            value = win_counts[move]
            if result == 1:
                value[0] += 1
            if result == 0:
                value[1] += 1
            if result == 0.5:
                value[2] += 1

    return win_counts


if __name__ == '__main__':
    board1 = Board()
    pos = ["|       |",
           "|       |",
           "|       |",
           "|   X   |",
           "|  OOX  |",
           "| OXXXO |",
           "---------",
           "|0123456|"]
    pos2 = ["|       |",
           "|       |",
           "|       |",
           "|       |",
           "|       |",
           "|   O   |",
           "---------",
           "|0123456|"]
    board1.set_position(pos2)
    board1.print_pos()
    for key, value in pure_mc(board1, 1000).items():
        print(f"move: {key}, wins {value[0]}, losses {value[1]}, draws {value[2]}")
        print(f"win %: {round(value[0] / (value[0] + value[1] + value[2]) * 100, 1)}\n")
