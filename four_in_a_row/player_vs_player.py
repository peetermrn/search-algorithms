"""PvP game. Made it first to figure out the general structure of the game."""
class Board:
    def __init__(self):
        self.available_moves = [0, 1, 2, 3, 4, 5, 6]
        self.pos = []
        for _ in range(6):
            self.pos.append("|       |")
        self.pos.append("|-------|")
        self.pos.append("|0123456|\n")

    def get_available_moves(self):
        return self.available_moves

    def set_position(self, pos):
        self.pos = pos

    def x_move(self, nr):
        nr += 1
        for x in range(7):

            if self.pos[x][nr] != " ":
                self.pos[x - 1] = self.pos[x - 1][:nr] + "X" + self.pos[x - 1][nr + 1:]
                if x == 1:
                    self.available_moves.remove(nr - 1)
                break

    def o_move(self, nr):
        nr += 1
        for x in range(7):
            if self.pos[x][nr] != " ":
                self.pos[x - 1] = self.pos[x - 1][:nr] + "O" + self.pos[x - 1][nr + 1:]
                if x == 1:
                    self.available_moves.remove(nr - 1)
                break

    def get_current(self):
        return self.pos

    def check_winner(self):
        """Return 2 if game not over, 1 if draw, O if O player won and X in X player won"""
        for line in self.pos:  # check horizontal
            if "OOOO" in line:
                return "O"
            if "XXXX" in line:
                return "X"
        for x in range(1, 8):  # check vertical
            column = ""
            for y in range(6):
                column += self.pos[y][x]
            if "OOOO" in column:
                return "O"
            if "XXXX" in column:
                return "X"
        for x in range(1, 8):  # check diagonal
            for y in range(4):
                if x + 3 <= 7 and y + 3 <= 5 and self.pos[x][y] == self.pos[x + 1][y + 1] == self.pos[x + 2][y + 2] == \
                        self.pos[x + 3][y + 3] != " ":
                    return self.pos[x][y]
                if x - 3 >= 0 and self.pos[x][y] == self.pos[x - 1][y + 1] == self.pos[x - 2][y + 2] == self.pos[x - 3][
                    y + 3] \
                        != " ":
                    return self.pos[x][y]
        if len(self.available_moves) == 0:
            return "1"
        return "2"


def play_game(board: Board):
    playing = True
    current = "O"
    while playing:
        for line in board.get_current():
            print(line)
        print("Possible moves:", board.available_moves)
        if current == "O":
            move = input("O move? ")
            current = "X"
            board.o_move(int(move))
        else:
            move = input("X move? ")
            current = "O"
            board.x_move(int(move))
        if board.check_winner() != "2":
            break
    for line in board.get_current():
        print(line)
    if board.check_winner() != "1":
        print(board.check_winner(), "won.")
    else:
        print("Draw")


if __name__ == '__main__':
    board1 = Board()
    play_game(board1)
