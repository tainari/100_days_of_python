import csv, random, time, tkinter
from tkinter import messagebox as mb

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#98c4ac"
CARD_FRONT_COLOR = "#FFFFFF"
ROW_CONFIG = "\n\n\n\n"

DEBUG = False

current_card_index = None

# --------------------- IMPORT WORDS ---------------------
word_pairs = []
try:
    with open("./data/french_words.csv") as f:
        rd = csv.reader(f)
        for wd1, wd2 in rd:
            word_pairs.append((wd1, wd2))
except FileNotFoundError:
    mb.showerror(title="Error", message="Language file not found.")


# ------------------- DEFINE FUNCTIONS -------------------
def mark_correct():
    discard = word_pairs.pop(current_card_index)
    if DEBUG:
        print(discard)
    select_card()


def select_card():
    start_button.config(state="normal")
    wrong_button.config(image=blank_image, state="disabled")
    right_button.config(image=blank_image, state="disabled")
    global current_card_index
    current_card_index = random.randint(0, len(word_pairs))
    card_front_text = "French"
    card_back_text = word_pairs[current_card_index][0]
    language.config(text=card_front_text)
    word.config(text=f"{ROW_CONFIG}{card_back_text}")


def show_answer():
    global current_card_index
    card_front_text = "English"
    card_back_text = word_pairs[current_card_index][1]
    language.config(text=card_front_text)
    word.config(text=f"{ROW_CONFIG}{card_back_text}")
    start_button.config(state="disabled")
    wrong_button.config(image=wrong_image, state="normal")
    right_button.config(image=right_image, state="normal")


def start_learning():
    start_button.config(text="Show Answer", command=show_answer)
    select_card()


# ---------------------- CREATE SCREEN ----------------------

screen = tkinter.Tk()
screen.title("Flashcards!")
screen.config(background=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0, height=600)
screen.resizable(width=False, height=False)

front_of_card = tkinter.PhotoImage(file="./images/card_front.png")
back_of_card = tkinter.PhotoImage(file="./images/card_back.png")
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
right_image = tkinter.PhotoImage(file="./images/right.png")
blank_image = tkinter.PhotoImage(file="./images/blank.png")

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_of_card)
canvas.grid(row=0, column=0, columnspan=3, rowspan=2)

word = tkinter.Label(text="\n\n\n\n", foreground='black', background='white', font=('Arial', 40, "bold"), anchor="n")
word.grid(row=0, column=1)

language = tkinter.Label(text="", foreground='black', background='white', font=('Arial', 30, "italic"))
language.grid(row=0, column=1)

wrong_button = tkinter.Button(image=blank_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                              command=select_card)
wrong_button.grid(row=2, column=0)

start_button = tkinter.Button(text="Start", highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                              command=start_learning)
start_button.grid(row=2, column=1)

right_button = tkinter.Button(image=blank_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                              command=mark_correct)
right_button.grid(row=2, column=2)


screen.mainloop()
