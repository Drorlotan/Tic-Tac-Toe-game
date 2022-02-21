from tkinter import *

turn = 0


def user_click(position):
    global turn
    if turn == 8 and win() is not True:
        label.config(text=f"IT'S A TIE")
    if win() is not True and turn < 9:
        if squares[position]['text'] != "":
            pass
        elif turn % 2 == 0:
            squares[position].config(text="X")
            turn += 1
        else:
            squares[position].config(text="O")
            turn += 1
    win()


def win():
    values = [sign["text"] for sign in squares]
    for num in range(len(values)):
        if values[num] == "":
            values[num] = num

    rows = [values[:3], values[3:6], values[6:9]]
    columns = [values[::3], values[1::3], values[2::3]]
    diagonals = [values[::4], values[2:7:2]]
    win_possible = rows + columns + diagonals
    for option in win_possible:
        if len(set(option)) == 1:
            sign = option[0]
            label.config(text=f"GAME OVER {sign} WIN!", fg="#e7305b")
            return True


window = Tk()
window.title("Tic Tac Toe")
window.config(padx=50, pady=50, bg="#f7f5dd")

# canvas = Canvas(width=900, height=900)
# canvas.grid(row=0, column=0)
xy_points = []
squares = []
for row in range(3):
    for column in range(3):
        position = len(squares)
        square = Button(text="", highlightthickness=0, command=lambda pos=position: user_click(pos), height=10,
                        width=20)
        square.grid(column=column, row=row)
        squares.append(square)

label = Label(text="game on")
label.grid(row=3, column=1)

window.mainloop()
