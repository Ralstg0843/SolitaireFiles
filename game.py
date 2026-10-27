
class SolitaireGame:
    # 1 = peg, 0 = empty hole, -1 = outside board

    def __init__(self, board_type="english", size=7):
        self.board_type = board_type
        self.size = size
        self.board = []
        self.create_board()

    def create_board(self):
        self.board = []

        for row in range(self.size):
            new_row = []

            for col in range(self.size):
                if self.board_type == "english":
                    corner = self.size // 3
                    valid = (
                        corner <= row < self.size - corner
                        or corner <= col < self.size - corner
                    )

                elif self.board_type == "diamond":
                    center = self.size // 2
                    valid = (
                        abs(row - center) + abs(col - center)
                        <= center
                    )

                else:  # Hexagonal board
                    center = self.size // 2
                    valid = (
                        abs(row - center)
                        + abs(col - center)
                        + abs(row + col - 2 * center)
                        <= self.size - 1
                    )

                if valid:
                    new_row.append(1)
                else:
                    new_row.append(-1)

            self.board.append(new_row)

        # Leave the middle hole empty
        center = self.size // 2
        self.board[center][center] = 0

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        # Check that the positions are on the board
        if not (0 <= start_row < self.size and
                0 <= start_col < self.size and
                0 <= end_row < self.size and
                0 <= end_col < self.size):
            return False

        if self.board[start_row][start_col] != 1:
            return False

        if self.board[end_row][end_col] != 0:
            return False

        row_diff = end_row - start_row
        col_diff = end_col - start_col

        # Horizontal, vertical, or diagonal jump
        if not ((abs(row_diff) == 2 and col_diff == 0) or
                (abs(col_diff) == 2 and row_diff == 0) or
                (abs(row_diff) == 2 and abs(col_diff) == 2)):
            return False

        # Check for a peg in the middle
        middle_row = (start_row + end_row) // 2
        middle_col = (start_col + end_col) // 2

        return self.board[middle_row][middle_col] == 1

    def make_move(self, start_row, start_col, end_row, end_col):
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            return False

        middle_row = (start_row + end_row) // 2
        middle_col = (start_col + end_col) // 2

        # Move the peg and remove the jumped peg
        self.board[start_row][start_col] = 0
        self.board[middle_row][middle_col] = 0
        self.board[end_row][end_col] = 1

        return True

    def is_game_over(self):
        # Check if any valid moves are left
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 1:
                    for dr, dc in [
                        (2, 0), (-2, 0),
                        (0, 2), (0, -2),
                        (2, 2), (2, -2),
                        (-2, 2), (-2, -2)
                    ]:
                        if self.is_valid_move(
                            row, col, row + dr, col + dc
                        ):
                            return False

        return True
