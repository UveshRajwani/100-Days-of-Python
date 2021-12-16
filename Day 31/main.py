from tkinter import *
import pandas
import random


csv = pandas.read_csv("data/french_words.csv")
to_learn = csv.to_dict(orient="records")
current_card = {}
word_to_learn = []


def func_right():
    to_learn.remove(current_card)
    get_word()


def func_wrong():
    global word_to_learn
    word_to_learn.append(current_card)
    data = pandas.DataFrame(word_to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    get_word()


def change_card():
    canvas.itemconfig(img, image=card_back)
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(lang, text="English")


def get_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(img, image=card_front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word, text=current_card["French"])
    canvas.itemconfig(lang, text="French")
    flip_timer = window.after(3000, func=change_card)


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, func=change_card)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
img = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="Pass", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Pass", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, rowspan=1)
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
right_button = Button(image=right, highlightthickness=0, command=func_right)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong, highlightthickness=0,command=func_wrong)
wrong_button.grid(row=1, column=1)
get_word()
window.mainloop()
