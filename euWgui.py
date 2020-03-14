import random
from tkinter import *


def eu():
    adj = ["piss ", "perma ", "shit ", "giga ", "cancer ", "trash ", "turbo "]
    adj_select = random.choice(adj)

    noun = ["dog ", "low ", "stuck ", "random "]
    noun_select = random.choice(noun)

    insult_gen = adj_select + noun_select

    if adj_select == "shit ":
        adj2 = ["cancer ", "disgusting ", "no-name ", "boosted ", "braindead "]
        adj_select2 = random.choice(adj2)
    elif adj_select == "cancer ":
        adj2 = ["shit ", "disgusting ", "no-name ", "boosted ", "braindead "]
        adj_select2 = random.choice(adj2)
    else:
        adj2 = ["disgusting ", "no-name ", "boosted ", "braindead ", "shit ", "cancer "]
        adj_select2 = random.choice(adj2)

    if noun_select == "dog ":
        noun2 = ["random ", "nerd ", "subhuman ", "animal ", "autist "]
        noun_select2 = random.choice(noun2)
    elif noun_select == "random ":
        noun2 = ["dog ", "nerd ", "subhuman ", "animal ", "autist "]
        noun_select2 = random.choice(noun2)
    else:
        noun2 = ["dog ", "random ", "nerd ", "subhuman ", "animal ", "autist "]
        noun_select2 = random.choice(noun2)

    insult_gen2 = adj_select2 + noun_select2

    coinflip = random.randrange(2)

    if coinflip == 0:
        insult = insult_gen + insult_gen2
    else:
        insult = insult_gen2 + insult_gen


    return insult

window = Tk()

window.title("Welcome to EU")

window.geometry('350x200')

def clicked():
  gap = eu()
  msg.config(text = gap)


msg = Label(window, font=(None, 16))
msg.place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(window,text='Click here if jg diff', command=clicked)

btn.place(relx=0.5, rely=0.7, anchor=CENTER)

window.mainloop()








