from tkinter import *
from datetime import datetime
import random
import cartoon
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

def show_Image():
    global icons
    icons='Adidas'
    path2 = "icons/" + icons + ".png"
    myImage = Image.open(path2)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoon.pixelised(pathway = path2)
    myImage = Image.open("cartoon.png")

