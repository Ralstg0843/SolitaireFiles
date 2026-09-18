import tkinter as tk


root = tk.Tk()
root.title("Peg Solitaire")
root.geometry("500x500")


some_label = tk.Label(
    root,
text="Welcome to Peg Solitaire!",
)
board_type = tk.StringVar()
button = tk.Radiobutton(
    root,
    text="English Board",
    variable=board_type,
    value="english",
)
button2 = tk.Radiobutton(
    root,
    text="Hexagonal Board",
    variable=board_type,
    value="hexagonal",
)
button3 = tk.Radiobutton(
    root,
    text="Diamond Board",
    variable=board_type,
    value="diamond",
)

v1 = tk.BooleanVar()

checkbox = tk.Checkbutton(
    root,
    text="Record Game",
    variable=v1
)

lines = tk.Canvas(root, width=300, height=300)
lines.create_line(100, 0, 150, 150, fill="blue")
lines.create_line(0, 0, 150, 150, fill="blue")
some_label.pack()
button.pack()
button2.pack()
button3.pack()
checkbox.pack()
lines.pack()

root.mainloop()
