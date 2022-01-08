import random


class Board:
    def __init__(self):
        self.available_moves = [0, 1, 2, 3, 4, 5, 6]
        self.pos = []
        for _ in range(6):
            self.pos.append("|       |")
        self.pos.append("---------")
        self.pos.append("|0123456|\n")

    def get_available_moves(self):
        return self.available_moves

    def set_position(self, pos):
        self.pos = pos

    def copy(self):
        new_board = Board()
        new_board.set_position(self.pos.copy())
        new_board.available_moves = self.available_moves.copy()
        return new_board

    def computer_move(self, nr):
        nr += 1
        for x in range(7):

            if self.pos[x][nr] != " ":
                self.pos[x - 1] = self.pos[x - 1][:nr] + "X" + self.pos[x - 1][nr + 1:]
                if x == 1:
                    self.available_moves.remove(nr - 1)
                break

    def player_move(self, nr):
        nr += 1
        for x in range(7):
            if self.pos[x][nr] != " ":
                self.pos[x - 1] = self.pos[x - 1][:nr] + "O" + self.pos[x - 1][nr + 1:]
                if x == 1:
                    self.available_moves.remove(nr - 1)
                break

    def get_current(self):
        return self.pos

    def print_pos(self):
        for line in self.pos:
            print(line)

    def check_winner(self):
        """Return 1 if game not over, 2 if draw, 3 if Player(O) won and 4 in computer(X) won"""
        for line in self.pos:  # check horizontal
            if "OOOO" in line:
                return 3
            if "XXXX" in line:
                # self.pos[self.pos.index(line)] = line[line.index("XXXX")] + "----" + line[line.index("XXXX") + 4:]
                return 4
        for x in range(1, 8):  # check vertical
            column = ""
            for y in range(6):
                column += self.pos[y][x]
            if "OOOO" in column:
                return 3
            if "XXXX" in column:
                return 4
        for x in range(1, 8):  # check diagonal
            for y in range(4):
                if x + 3 <= 7 and y + 3 <= 6 and self.pos[x][y] == self.pos[x + 1][y + 1] == self.pos[x + 2][y + 2] == \
                        self.pos[x + 3][y + 3] != " ":
                    if self.pos[x][y] == "O":
                        return 3
                    return 4
                if x - 3 >= 0 and self.pos[x][y] == self.pos[x - 1][y + 1] == self.pos[x - 2][y + 2] == self.pos[x - 3][
                    y + 3] \
                        != " ":
                    if self.pos[x][y] == "O":
                        return 3
                    return 4
        if len(self.available_moves) == 0:
            return 1
        return 2


def simulate(board: Board, move):
    """Helper method to simulate thru games."""
    current = "Player"
    board.computer_move(move)
    while True:
        if board.check_winner() != 2:
            break

        if current == "Player":
            board.player_move(random.choice(board.available_moves))
            current = "Computer"
        else:
            board.computer_move(random.choice(board.available_moves))
            current = "Player"

    if board.check_winner() == 3:
        return 0
    elif board.check_winner() == 4:
        return 1
    else:
        return 0.5


def pure_mc(board: Board, n=200):
    """Monte Carlo."""
    win_counts = dict((move, 0) for move in board.available_moves)
    for move in board.available_moves:
        for _ in range(n):
            win_counts[move] += simulate(board.copy(), move)

    return max(win_counts, key=win_counts.get)


def play_game(board: Board):
    current = "Player"
    while True:
        if current == "Player":
            for line in board.get_current():
                print(line)
            print("Possible moves:", board.available_moves, "\n")
            move = input("Your move? ")
            board.player_move(int(move))
            current = "Computer"
        else:
            board.computer_move(pure_mc(board.copy()))
            current = "Player"
        if board.check_winner() != 2:
            break
    for line in board.get_current():
        print(line)
    if board.check_winner() == 3:
        print("PLAYER WON.")
    elif board.check_winner() == 4:
        print("COMPUTER WON.")
    else:
        print("DRAW")


if __name__ == '__main__':
    board1 = Board()
    pos = ["|       |",
           "|       |",
           "|    X  |",
           "|  OXO  |",
           "| OXXO  |",
           "|OXXXO  |",
           "---------",
           "|0123456|"]
    board1.set_position(pos)
    print(board1.check_winner())
