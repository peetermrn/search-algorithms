import random


class Pos:
    def __init__(self, pos):
        self.pos = pos
        self.conflicts = self.calculate_conflicts(pos)
        self.n = len(self.pos)

    def get_queens_amount(self):
        """Calculate queens amount on board."""
        queens = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.pos[i][j] == "1":
                    queens += 1
        return queens

    @staticmethod
    def calculate_conflicts(pos):
        """Calculate conflicts on board."""
        conflicts = 0
        n = len(pos)
        for i in range(n):
            queens_in_row = pos[i].count("1")  # check how many queens in a row
            if queens_in_row:
                conflicts += queens_in_row - 1
            queens_in_col = 0
            for j in range(n):
                if pos[j][i] == "1":  # check how many queens in a column
                    # for every queen i will start going down the board diagonally in both directions checking for
                    # conflicts
                    queens_in_col += 1
                    queens_in_diag = 0
                    for d in range(1, n):
                        try:
                            if pos[j + d][i + d] == "1":
                                queens_in_diag += 1
                                break
                        except IndexError:  # happens when checking position out of board.
                            break
                    for d in range(1, n):
                        try:
                            if i - d >= 0 and pos[j + d][i - d] == "1":
                                queens_in_diag += 1
                                break
                        except IndexError:  # happens when checking position out of board.
                            break
                    conflicts += queens_in_diag
            if queens_in_col:
                conflicts += queens_in_col - 1
        return conflicts

    def best_move(self):
        """Find best move and it's conflicts. Try all possible moves for all queens."""
        conflicts = self.conflicts
        best_move = self.pos
        for i in range(self.n):
            for j in range(self.n):
                if self.pos[i][j] == "1":
                    for x in range(self.n):
                        for y in range(self.n):
                            temp_e = self.pos[x][y]
                            temp_pos = self.pos.copy()
                            temp_pos[x] = self.pos[x][:y] + "1" + self.pos[x][y + 1:]
                            temp_pos[i] = temp_pos[i][:j] + temp_e + temp_pos[i][j + 1:]

                            if self.calculate_conflicts(temp_pos) < conflicts:
                                conflicts = self.calculate_conflicts(temp_pos)
                                best_move = temp_pos

        return best_move, conflicts


class LocalSearch:

    @staticmethod
    def hill_climbing(pos: Pos):
        curr_value = pos.conflicts
        while True:
            move, new_value = pos.best_move()
            if new_value >= curr_value:
                # best move doesnt have less conflicts. This can happen if there are too many queens on the board or if
                # queens are in a bad formation, for example all on the diagonal.
                if pos.get_queens_amount() > pos.n:
                    # too many queens on the board to remove all conflicts
                    return "Too many queens"
                else:
                    # best move doesnt reduce conflicts so will shuffle the board and start over.
                    random_pos = ["0" * len(move)] * len(move)
                    for nr in range(len(move)):
                        i = random.randint(0, len(move) - 1)
                        random_pos[nr] = random_pos[nr][:i] + "1" + random_pos[nr][i + 1:]
                    pos = Pos(random_pos)
                    curr_value = pos.calculate_conflicts(random_pos)
            else:
                # position improves, keep searching
                curr_value = new_value
                pos = Pos(move)
                if new_value == 0:
                    return pos.pos

    def nxn_queens_diagonal(self, n):
        """Generate n by n board with n queens on the diagonal. Also generate the solution."""
        data = ["0" * n] * n
        print(f"{n}x{n} diagonal queens")
        for i in range(n):
            data[i] = data[i][:i] + "1" + data[i][i + 1:]

        for row in data:
            print(row)
        print("\nsolution\n")

        big_board = Pos(data)
        for line in self.hill_climbing(big_board):
            print(line)
        print("-" * n, "\n")

    def nxn_queens_random(self, n):
        """Generate n by n board with n queens randomly placed. Also generate the solution."""
        data = ["0" * n] * n
        print(f"{n}x{n} randomly placed queens")
        for nr in range(n):
            i = random.randint(0, n - 1)
            data[nr] = data[nr][:i] + "1" + data[nr][i + 1:]
        for row in data:
            print(row)
        print("\nsolution\n")

        big_board = Pos(data)
        for line in self.hill_climbing(big_board):
            print(line)
        print("-" * n, "\n")


if __name__ == '__main__':
    s = LocalSearch()
    s.nxn_queens_diagonal(8)
    s.nxn_queens_random(8)

    s.nxn_queens_diagonal(10)
    s.nxn_queens_random(10)

    bad_data_example = ["0011", "1100", "1010", "0001"]  # too many queens
    b = Pos(bad_data_example)
    print(s.hill_climbing(b))  # => too many queens
