import random
from tkinter import *


def eu():
    adj = ["piss ", "perma ", "shit ", "giga ", "cancer ", "trash ", "turbo "]
    adj_select = random.choice(adj)

    noun = ["dog ", "low ", "stuck ", "random ", "lowelo "]
    noun_select = random.choice(noun)

    if adj_select == "shit ":
        adj2 = ["cancer ", "disgusting ", "no-name ", "boosted ", "braindead "]
    elif adj_select == "cancer ":
        adj2 = ["shit ", "disgusting ", "no-name ", "boosted ", "braindead "]
    else:
        adj2 = ["disgusting ", "no-name ", "boosted ", "braindead ", "shit ", "cancer "]

    if noun_select == "dog ":
        noun2 = ["random ", "nerd ", "subhuman ", "animal ", "autist ", "retard "]
    elif noun_select == "random ":
        noun2 = ["dog ", "nerd ", "subhuman ", "animal ", "autist ", "retard "]
    else:
        noun2 = ["dog ", "random ", "nerd ", "subhuman ", "animal ", "autist ", "retard "]

    adj_select2 = random.choice(adj2)
    noun_select2 = random.choice(noun2)

    insult_gen = adj_select + noun_select
    insult_gen2 = adj_select2 + noun_select2

    coinflip = random.randrange(2)

    if coinflip == 0:
        insult = insult_gen + insult_gen2
    else:
        insult = insult_gen2 + insult_gen


    return insult

window = Tk()

window.title("Welcome to EU")

window.geometry('400x200')

def clicked():
  gap = eu()
  msg.config(text = gap)


msg = Label(window, font=(None, 16))
msg.place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(window,text='Click here if jg diff', padx=2, command=clicked)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

window.mainloop()








