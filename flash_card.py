from tkinter import *
from time import sleep
import pandas as pd
import random


data = pd.read_csv("french_words.csv")

french = data["French"].to_list()
english = data["English"].to_list()

new_word_french= random.choice(french)
new_word_english = english[french.index(new_word_french)]

def change_data():
    canvas.itemconfig(card,image = src_back)
    canvas.itemconfig(language,text = "English",fill ="beige")
    canvas.itemconfig(word,text = new_word_english,fill ="white")

def time_out_display():
    canvas.after(5000,change_data)


def right_button(event):
    if len(french)==0:
        canvas.itemconfig(card,image = src_front)
        canvas.itemconfig(language,text = "Congratulations! you are all caught up",fill ="black")
        canvas.itemconfig(word,text = "Completed",fill ="grey")
    global new_word_french,new_word_english
    french.remove(new_word_french)
    english.remove(new_word_english)
    wrong_button(event)
    
    

def wrong_button(event):
    global new_word_french,new_word_english
    new_word_french= random.choice(french)
    new_word_english = english[french.index(new_word_french)]
    
    canvas.itemconfig(card,image = src_front)
    canvas.itemconfig(language,text = "French",fill ="grey")
    canvas.itemconfig(word,text = new_word_french,fill ="black")
    time_out_display()




window = Tk()
window.title("Flash Card Game")
window.config(width=820,height=660,bg="#7FDB96")   # padx=20,pady=20
src_front = PhotoImage(file="./images/card_front.png")
src_back = PhotoImage(file="./images/card_back.png")
cancel = PhotoImage(file="./images/wrong.png")
okHa = PhotoImage(file="./images/right.png")
canvas = Canvas(window,width=800,height=660,bg="#7FDB96",highlightthickness=0)
card = canvas.create_image(400,260,image = src_front)
right = canvas.create_image(580,580,image = okHa)
canvas.config(cursor="hand2")
canvas.tag_bind(right,'<ButtonPress-1>',right_button)
wrong = canvas.create_image(180,580,image = cancel)
canvas.tag_bind(wrong,'<ButtonPress-1>',wrong_button)


language = canvas.create_text(400,100,text="French",fill="grey",font=("monospace",20,"bold"))
word = canvas.create_text(400,220,text=new_word_french,fill="black",font=("monospace",44,"bold"))

time_out_display()

canvas.place(x=20,y=10)






window.mainloop()