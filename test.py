"""TESTING PHOTO SWAP"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open(".\static\PotionOfWeaknessNew.png")
tkpic = ImageTk.PhotoImage(image)
label = Label(root, image = tkpic)
label.grid(column = 1)

def change_pic():
    label.after(1000, label.master.destroy)
    image = Image.open(".\static\PotionOfWeaknessNew.png")
    tkpic = ImageTk.PhotoImage(image)
    new_label = Label(root, image = tkpic)
    new_label.grid(column=1)

button = Button(root, text = "test", command = change_pic)
button.grid(column = 1)

root.mainloop()