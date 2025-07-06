from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv('./31.Flashcard Project/data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv('./31.Flashcard Project/data/french_words.csv').to_dict(orient='records')
current_card = {}

def next_card():
    global current_card, flip_timer
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    data.remove(current_card)
    Data = pandas.DataFrame(data)
    Data.to_csv('./31.FlashCard Project/data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='./31.Flashcard Project/images/card_front.png')
card_back_img = PhotoImage(file='./31.Flashcard Project/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0 ,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

wrong_image = PhotoImage(file='./31.Flashcard Project/images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=is_known)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='./31.Flashcard Project/images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()