from tkinter import*
from random import randint
def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1,15)))
window = Tk()
text = Text(window, width=8, height=8)
buttonA = Button(window, text='Press to Roll', command=roll)
text.pack()
buttonA.pack()

