from tkinter import *
from time import sleep

def change_data():
    canvas.itemconfig(card,image = src_back)
    canvas.itemconfig(language,text = "French",fill ="beige")
    canvas.itemconfig(word,text = "Kuch Bhi",fill ="white")

def time_out_display():
    canvas.after(5000,change_data)


def right_button():
    pass

def wrong_button():
    pass




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
wrong = canvas.create_image(180,580,image = cancel)


language = canvas.create_text(400,100,text="English",fill="grey",font=("monospace",20,"bold"))
word = canvas.create_text(400,220,text="AnyThing",fill="black",font=("monospace",44,"bold"))

time_out_display()

canvas.place(x=20,y=10)






window.mainloop()