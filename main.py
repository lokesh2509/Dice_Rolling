from tkinter import *
import random

root = Tk()
root.title("Dice Rolling By Lokesh Vyas")
root.geometry("400x400")

l1 = Label(root,font=("Helvetica",200))

def dice_roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=random.choice(dice))
    l1.pack()


button = Button(root,text="Roll the dice", command=dice_roll)
button.place(x=160,y=300)



root.mainloop()