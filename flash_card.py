from tkinter import *
from time import sleep
import pandas as pd
import random
import sys


data = pd.read_csv("language_words.csv")


print("""\nChoose from following language models:
      1- French
      2- English
      3- Chinese
      4- Japnese
      5- Urdu
      6- Arabic\n\n""")

learn_lang = input("Enter language to learn: ").capitalize()

your_lang = input("Enter your native language : ").capitalize()






try:
    learn_lang_list = data[learn_lang].to_list()
    your_language_list = data[your_lang].to_list()
except Exception as e:
    print("Language model ",e, " is not available")
    sys.exit()
    

new_word_learn_lang= random.choice(learn_lang_list)
new_word_your_language = your_language_list[learn_lang_list.index(new_word_learn_lang)]

def change_data():
    canvas.itemconfig(card,image = src_back)
    canvas.itemconfig(language,text = your_lang,fill ="beige")
    canvas.itemconfig(word,text = new_word_your_language,fill ="white")

def time_out_display():
    canvas.after(5000,change_data)


def right_button(event):
    global new_word_learn_lang,new_word_your_language
    learn_lang_list.remove(new_word_learn_lang)
    your_language_list.remove(new_word_your_language)
    wrong_button(event)
    
    

def wrong_button(event):
    global new_word_learn_lang,new_word_your_language
    if len(learn_lang_list)==0:
        new_word_learn_lang= "Congratulations! you are all caught up."
        new_word_your_language = "Completed"
        
        canvas.itemconfig(card,image = src_front)
        canvas.itemconfig(language,text =new_word_learn_lang ,font=("monospace",12,"normal"),fill ="black")
        canvas.itemconfig(word,text = new_word_your_language ,fill ="green")
        window.after(2500,window.quit)
        return
    
    else:
        new_word_learn_lang= random.choice(learn_lang_list)
        new_word_your_language = your_language_list[learn_lang_list.index(new_word_learn_lang)]
        
        canvas.itemconfig(card,image = src_front)
        canvas.itemconfig(language,text = learn_lang ,fill ="grey")
        canvas.itemconfig(word,text = new_word_learn_lang, fill ="black")
        time_out_display()




window = Tk()
window.title("Flash Card Game")
window.config(width=820,height=660,bg="#7FDB96")   # padx=20,pady=20
window.focus_force()
window.lift()
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


language = canvas.create_text(400,100,text=learn_lang,fill="grey",font=("monospace",20,"bold"))
word = canvas.create_text(400,220,text=new_word_learn_lang,fill="black",font=("monospace",44,"bold"))


canvas.place(x=20,y=10)

time_out_display()





window.mainloop()