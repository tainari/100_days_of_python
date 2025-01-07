import csv, random, time

import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

with open("data/french_words.csv") as file:
    rd = csv.reader(file)
    next(rd)
    word_list = list(rd)

random.shuffle(word_list)

window = tk.Tk()
window.title("Flashcards")
window.geometry("840x700")
window.configure(bg=BACKGROUND_COLOR, padx=20, pady=20)

card_back = tk.PhotoImage(file="images/card_back.png")
card_front = tk.PhotoImage(file="images/card_front.png")
canvas = tk.Canvas(window,width=800, height=526, background=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
# add card image
canvas.create_image(400,263,image=card_front)
# add language title
# current_language = "French"
language = canvas.create_text(400, 150, text="farts", font=("Arial", 40, "italic"), fill="black")
# current_word = "word"
word = canvas.create_text(400, 263, text="", font=("Arial", 65, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=3)

# card = tk.Label(window, text="", image=card_front, bg=BACKGROUND_COLOR, compound=tk.CENTER, font=("Arial", 20), fg="black")
# card.grid(column=0, row=0, columnspan=3)

def next_word():
    global english_word, french_word
    french_word, english_word  = word_list.pop(random.randint(0, len(word_list) - 1))
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=french_word)
    window.update()
    time.sleep(3)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=english_word)
    window.update()
    print(f"Words left: {len(word_list)}")

def all_done():
    canvas.itemconfig(language, text="")
    canvas.itemconfig(word, text="All words practiced!")

def mark_correct():
    if word_list:
        next_word()
    else:
        all_done()

def mark_incorrect():
    word_list.append([english_word, french_word])
    next_word()


wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong = tk.Button(window, command=mark_incorrect, image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, bd=0)
wrong.grid(column=0, row=1)
right_img = tk.PhotoImage(file="images/right.png")
right = tk.Button(window, command=mark_correct, image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
right.grid(column=2, row=1)

# get first word
next_word()

window.mainloop()
