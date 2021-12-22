from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    work = 5  # 25 * 60
    rest = 3  # 5 * 60
    long_rest = 4  # 20 * 60
    global reps
    if reps % 8 == 0:
        countdown(long_rest)
        check.config(text="")
    elif reps % 2 == 0:
        check["text"] += "✔"
        countdown(rest)
    else:
        countdown(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        canvas.itemconfig(time_text, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        global reps
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
heading.grid(row=0, column=1)

canvas = Canvas(height=224, width=204, bg=YELLOW, highlightthickness=0)
filename = PhotoImage(file="tomato.png")
image = canvas.create_image(102, 112, image=filename)
time_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=3, column=2)

check = Label(text="", fg=GREEN, bg=YELLOW, font=20)
check.grid(row=4, column=1)

reps = 1

window.mainloop()
