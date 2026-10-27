
import tkinter as tk
from game import SolitaireGame


class SolitaireGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Peg Solitaire")
        self.root.geometry("500x550")

        self.board_type = tk.StringVar(value="english")
        self.board_size = tk.IntVar(value=7)

        self.game = None
        self.selected = None

        tk.Label(root, text="Welcome to Peg Solitaire!").pack(pady=5)

        # Board type options
        tk.Radiobutton(
            root,
            text="English Board",
            variable=self.board_type,
            value="english"
        ).pack()

        tk.Radiobutton(
            root,
            text="Hexagonal Board",
            variable=self.board_type,
            value="hexagonal"
        ).pack()

        tk.Radiobutton(
            root,
            text="Diamond Board",
            variable=self.board_type,
            value="diamond"
        ).pack()

        # Board size
        tk.Label(root, text="Board Size").pack()

        tk.Spinbox(
            root,
            from_=5,
            to=11,
            increment=2,
            textvariable=self.board_size,
            width=5
        ).pack()

        # New Game button
        tk.Button(
            root,
            text="New Game",
            command=self.new_game
        ).pack(pady=5)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)

        self.canvas = tk.Canvas(root, width=420, height=330)
        self.canvas.pack()

        self.new_game()

    def draw_board(self):
        # Clear the old board
        self.canvas.delete("all")

        cell_size = min(35, 300 // self.game.size)

        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.board[row][col] == -1:
                    continue

                x = col * cell_size + 30
                y = row * cell_size + 25

                color = "blue" if self.game.board[row][col] == 1 else "white"

                # Highlight the selected peg
                if self.selected == (row, col):
                    color = "yellow"

                self.canvas.create_oval(
                    x - 12, y - 12,
                    x + 12, y + 12,
                    fill=color,
                    outline="black",
                    tags=f"peg_{row}_{col}"
                )

                self.canvas.tag_bind(
                    f"peg_{row}_{col}",
                    "<Button-1>",
                    lambda event, r=row, c=col: self.click_peg(r, c)
                )

    def click_peg(self, row, col):
        if self.selected is None:
            if self.game.board[row][col] == 1:
                self.selected = (row, col)

        else:
            start_row, start_col = self.selected

            if self.game.make_move(start_row, start_col, row, col):
                if self.game.is_game_over():
                    self.status_label.config(text="Game Over!")
                else:
                    self.status_label.config(text="Valid move!")
            else:
                self.status_label.config(text="Invalid move!")

            self.selected = None

        self.draw_board()

    def new_game(self):
        # Create a board using the selected settings
        self.game = SolitaireGame(
            self.board_type.get(),
            self.board_size.get()
        )

        self.selected = None
        self.status_label.config(text="New game started!")
        self.draw_board()


root = tk.Tk()
app = SolitaireGUI(root)
root.mainloop()
