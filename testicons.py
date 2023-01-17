from tkinter import *
from datetime import datetime
import random
import cartoonluck
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

def show_Image(choice):
    global icons
    icons=['']
    path2 = "food/" + str(icons[choice]) + ".png"
    myImage = Image.open(path2)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoonluck.pixelised(pathway = path2)
    myImage = Image.open("kawaii.png")


show_Image(0)