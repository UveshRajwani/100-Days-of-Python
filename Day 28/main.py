import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_count = 1
mark = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global mark
    global timer_count
    mark = ""
    timer_count = 1
    check_mark.config(text=mark)
    canvas.itemconfig(timer, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global mark
    if timer_count < 8:
        if timer_count % 2 == 0:
            count_down(SHORT_BREAK_MIN*60)
        else:
            count_down(WORK_MIN*60)
            mark += "✓"
            check_mark.config(text=mark)
    elif timer_count == 8:
        count_down(LONG_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        timer_count += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(row=0, column=1)
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
stop_button = Button(text="Reset")
stop_button.grid(row=2, column=2)
check_mark = Label(text=mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_mark.grid(row=3, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

window.mainloop()
