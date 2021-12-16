from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_passowrd():
    password.delete(0, END)
    nr_letters = random.randint(3, 7)
    nr_symbols = random.randint(3, 7)
    nr_numbers = random.randint(3, 7)

    answer = []
    fpassword = ""
    for _ in range(0, nr_letters):
        answer.append(random.choice(letters))

    for _ in range(0, nr_symbols):
        answer.append(random.choice(symbols))

    for _ in range(0, nr_numbers):
        answer.append(random.choice(numbers))

    for i in answer:
        fpassword = fpassword + i
    hard_password = ''
    random.shuffle(answer)
    for i in answer:
        hard_password = hard_password + i
    pyperclip.copy(hard_password)
    password.insert(0, hard_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_password():
    data = ""
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
            data = data[website.get()]
    except KeyError:
        messagebox.showinfo(title="error", message="Website not found")
    else:
        messagebox.showinfo(title=website.get(), message=f"Email: {data['email']}\nPassword: {data['password']}")
        pyperclip.copy(data["password"])


def add_password():
    new_data = {
        website.get(): {
            "email": email.get(),
            "password": password.get()
        }
    }
    if website.get() == "" or email.get() == "" or password.get() == "":
        messagebox.showinfo(title="error", message="Please fill all the fields ")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password")
window.config(pady=20, padx=20)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label1 = Label(text="Email/Username:")
label1.grid(row=2, column=0)
label1 = Label(text="Password:")
label1.grid(row=3, column=0)

website = Entry()
website.grid(row=1, column=1, )
email = Entry(width=35)
email.grid(row=2, columnspan=2, column=1)
password = Entry()
password.grid(row=3, column=1)

gen_button = Button(text="Generate Password", command=gen_passowrd)
gen_button.grid(row=3, column=2)
add_button = Button(width=35, text="Add", command=add_password)
add_button.grid(row=4, column=1)
search = Button(text="Search", command=search_password)
search.grid(row=1, column=2)
window.mainloop()
