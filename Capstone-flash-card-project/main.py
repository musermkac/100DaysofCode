BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

#----UI SETUP----
window = Tk()
window.title("Have fun learning with MK's Interactive Flash Cards!")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
bg_image = PhotoImage(file = "images/card_front.png")
answer_bg_image = PhotoImage(file = "images/card_back.png")
background_image = canvas.create_image(400,263, image = bg_image)
title = canvas.create_text(400,150,text="",font=("Ariel",45,"italic"),fill="black")
word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"),fill="black")
canvas.config(bg= BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row =0, column=0, columnspan=2)
card = {}

#-----READ THE CSV DATA------
flash_data =  pandas.read_csv("data/french_words.csv")
flash_data_dict = flash_data.to_dict(orient="records")

# -----FUNCTION FOR CARD NEXT IN LINE-------
def next_in_line():
    global card, card_timer
    window.after_cancel(card_timer)
    card = random.choice(flash_data_dict)
    print(card)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=card["French"], fill="black")
    canvas.itemconfig(background_image, image=bg_image)
    card_timer = window.after(5000, func=english_answer)

# -----FUNCTION FOR ENGLISH TRANSLATION-------
def english_answer():
    canvas.itemconfig(title, text="English", fill = "white")
    canvas.itemconfig(word, text=card['English'], fill = "white")
    canvas.itemconfig(background_image, image=answer_bg_image)

#------BUTTONS--------
right_image = PhotoImage(file="images/right.png")
answer_button = Button(image=right_image, highlightthickness=0, command = next_in_line)
answer_button.grid(row = 1, column =0)

wrong_image = PhotoImage(file="images/wrong.png")
check_button = Button(image=wrong_image, highlightthickness=0, command = next_in_line)
check_button.grid(row = 1, column =1)
card_timer = window.after(5000, func=english_answer)
next_in_line()

#-----WINDOW-----
window.mainloop()
