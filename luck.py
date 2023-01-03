#Import the required library
from tkinter import*
from datetime import *
from PIL import Image, ImageTk, ImageOps
import os
import random
import cartoon

#Create an instance of tkinter frame
main= Tk()

#Define geometry of the window
main.geometry("800x300")

def show_Image(choice):
    global imageLabel, imagePixel

    path2 = "scissors paper stone pics/" + str(choice) + ".png"
    myImage = Image.open(path2)
    myImage = myImage.resize((250, 250))
    loadImage = ImageTk.PhotoImage(myImage)
    imageLabel.image = loadImage
    imageLabel.config(image = loadImage, width = 250, height = 250)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoon.pixelised(path = path2)
    myImage = Image.open("kawaii.png")
    myImage = myImage.resize((250, 250))
    loadImage = ImageTk.PhotoImage(myImage)
    imagePixel.image = loadImage
    imagePixel.config(image = loadImage, width = 250, height = 250)

def change_img():
    for i in range(len(options)) :
        if options[i] == clicked.get():
            i = i+1
            if i == 2 and clickeds.get() > 29:
                test3 = False   
            elif clickeds.get() > 30:
                if i == 4 or i == 6 or i == 9 or i == 11:
                    test3 = False
                else: 
                    test3 = True
            else:
                test3 = True
    if test3 == True:
        label.config(text="Kindly, Input your DoB and Press the 'Enter' button")
        randomno = random.randint(1, 5)
        if randomno == 1:
            path = os.path.abspath('percentage pics') + '\\0.png' #edit 1 to the name of 0% pic
            files = path.replace('\\','/')
            #the 2 lines below for pop up img 
            myImage = Image.open(files)
            myImage.show()
            #send pic here to servo
            label2.config(text='')
            frame1.grid_forget()
        elif randomno == 2:
            path = os.path.abspath('percentage pics') + '\\25.png' #edit 2 to the name of 25% pic
            files = path.replace('\\','/')
            #the 2 lines below for pop up img 
            myImage = Image.open(files)
            myImage.show()
            #send pic here to servo
            label2.config(text='')
            frame1.grid_forget()
        elif randomno == 3:
            path = os.path.abspath('percentage pics') + '\\50.png' #edit 3 to the name of 50% pic
            files = path.replace('\\','/')
            #the 2 lines below for pop up img 
            myImage = Image.open(files)
            myImage.show()
            #send pic here to servo
            label2.config(text='')
            frame1.grid_forget()
        elif randomno == 4:
            path = os.path.abspath('percentage pics') + '\\75.png' #edit 4 to the name of 75% pic
            files = path.replace('\\','/')
            #the 2 lines below for pop up img 
            myImage = Image.open(files)
            myImage.show()
            label2.config(text='Would you like to play a game with me? Scissors, Paper, Stone!')
            frame1.grid(row=4, column=1)
            #send pic here to servo
        else:
            path = os.path.abspath('percentage pics') + '\\100.png' #edit 5 to the name of 100% pic
            files = path.replace('\\','/')
            #the 2 lines below for pop up img 
            myImage = Image.open(files)
            myImage.show()
            label2.config(text='Would you like to play a game with me? Scissors, Paper, Stone!')
            frame1.grid(row=4, column=1)
            #send pic here to servo
    else:
        label.config(text = "Please input a valid DoB", image='', font=('50px'))
        #label2.config(text='')

def game():
    frame1.grid_forget()  #WHAT IS grid_forget()
    randoms = random.randint(1,3)
    if randoms == 1:
        o = "paper"
    elif randoms == 2:
        o = "scissors"
    else:
        o = "stone"
    path = os.path.abspath('scissors paper stone pics') +'\\' + o + '.png'
    files = path.replace('\\','/')
    myImage = Image.open(files) #edit here onw to send the pic
    myImage.show()
        

# Dropdown menu options
options = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
optionss = []
d = 32
for x in range (1, d):
    optionss.append(x)

# datatype of menu text
clicked = StringVar()
clickeds = IntVar()

# initial menu text
#clicked.set("January")
#clickeds.set(1)
who = date.today()
whos = options[who.month-1]
clicked.set(whos)
clickeds.set(who.day)

title= Label (main, text="What's your luck today?", font=('100px'), bg='white')
title.grid(row=0, column=1)

# Create Dropdown menu
drop = OptionMenu(main , clicked , *options )
drop.grid(row=1, column=0)
drop.config(bg="#ffe4f2", fg="BLACK", activebackground="#e54ed0", activeforeground="WHITE")
drop["menu"].config(bg="#e54ed0", fg="WHITE", activebackground="#ffe4f2", activeforeground="BLACK")

# Create Dropdown menu
drops = OptionMenu(main , clickeds , *optionss )
drops.grid(row=2, column=0)
drops.config(bg="#9f45b0", fg="WHITE", activebackground="#44008b", activeforeground="WHITE")
drops["menu"].config(bg="#44008b", fg="WHITE", activebackground="#9f45b0", activeforeground="WHITE")

#Create a Label widget
label= Label(main, image='', text="Kindly, Input your DoB and Press the 'Enter' button", font=('100px'), bg='white')
label.grid(row=1, column=1)

#Create a Button to handle the update Image event
button= Button(main, text= "Enter", command= change_img,  bg="#00076f", fg="WHITE")
button.grid(row=2, column=1)

frame1 = Frame(main)
frame1.grid(row=4, column=1)
frame1.grid_forget()

label2 = Label(frame1, text = "", font='20px')
label2.grid(row=0, columnspan=3)

#heree
frame1 = Frame(main)
frame1.grid(row=1, column=0)

imageFrame = Frame(main)
imageFrame.grid(row=0, column=1)

# Image Window
imageLabel = Label(imageFrame, bg = 'white', width = 30, height = 15)
imageLabel.grid(row=0, column=0)
imagePixel = Label (imageFrame, bg = 'grey', width = 30, height = 15)
imagePixel.grid(row=0, column=1)

paths = os.path.abspath('scissors paper stone pics') +'\\paper.png'
file = paths.replace('\\','/')
img1= ImageTk.PhotoImage(Image.open(file))

paths = os.path.abspath('scissors paper stone pics') +'\\scissors.png'
file = paths.replace('\\','/')
img2= ImageTk.PhotoImage(Image.open(file))

paths = os.path.abspath('scissors paper stone pics') +'\\stone.png'
file = paths.replace('\\','/')
img3= ImageTk.PhotoImage(Image.open(file))

label3 = Button(frame1, image = img1, font='20px', command=game)
label3.grid(row=1, column=0)

label4 = Button(frame1, image = img2, font='20px', command=game)
label4.grid(row=1, column=1)

label5 = Button(frame1, image = img3, font='20px', command=game)
label5.grid(row=1, column=2)

label6 = Label(frame1, text='', font='20px')
label6.grid(row=2, columnspan=3)

main.bind("<Return>", change_img) 
main.mainloop()