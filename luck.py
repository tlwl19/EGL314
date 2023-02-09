#Import the required library
from tkinter import*
from datetime import *
from PIL import Image, ImageTk, ImageOps
import random
import cartoon


def show_Image_luck(choice2):
    if type(choice2) == int:
        lucky = "percentage pics/" + str(choice2) + ".png"
        myImage = Image.open(lucky)
    else:
        lucky = "scissors paper stone pics/" + choice2 + ".png"
        myImage = Image.open(lucky)

        #sending to cartoon.py
        #path refers to input for img
        #lucky refers to variable
    cartoon.pixelised(path = lucky)
    myImage = Image.open("cartoon.png")


def change_img(): 
    global name
    for i in range(len(options)) : #check if is a valid DOB
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

    if test3 == True:   #If is valid, execute below command
        label.config(text="Input your date of birth and click on the 'Enter' button.")
        randomno = random.randint(0, 2) #randomly generate a number 0-4
        randomnolist = [7,75,100]
        if randomnolist[randomno] == 75 or randomnolist[randomno] == 100:  #when randomly generated number is 3 or 4, will show 75% or 99%, and activate game
            label2.config(text='Would you like to play a game with me? Scissors, Paper, Stone!')
            frame1.grid(row=4, columnspan=3)  #For the selection of scissors,paper,stone
            show_Image_luck(randomnolist[randomno])
            imageLabel.config(image="", width = 35, height = 18)
            previewtitle.config(text="")
            previewtitle.grid(row=2, column=3)
            imageLabel.grid(row=4, column=3)
            luckpic.config(image = "")
            print(randomnolist[randomno])

        else: #when randomly generated number is 2, will show 50% pic
            label2.config(text='')
            frame1.grid_forget()
            previewtitle.grid_forget()
            imageLabel.grid_forget()
            luckpic.grid(row=4, column=0)
            luckpiclist = ["come","conquer","control","hang","happy","important","living","openup","tough","turnout","luckmain"]
            name = name+1
            if name > len(luckpiclist)-1:
                name = 0
            path = "motivationalquotes/" + luckpiclist[name] + ".png"
            myImages = Image.open(path)
            loadImage = ImageTk.PhotoImage(myImages)
            luckpic.image = loadImage
            luckpic.config(image = loadImage)
            show_Image_luck(randomnolist[randomno])
            print(randomnolist[randomno])

    else:
        label.config(text = "Please input a valid date of birth.", image='', font=('Arial', 25))

def preview_Image(choice):
    global imageLabel
    if choice == 1:
        choice = "scissors"
    elif choice == 2:
        choice = "paper"
    else:
        choice = "stone"
    path = "scissors paper stone pics/" + str(choice) + ".png"
    myImages = Image.open(path)
    myImages = myImages.resize((300, 300))
    loadImage = ImageTk.PhotoImage(myImages)
    imageLabel.image = loadImage
    imageLabel.config(image = loadImage, width = 300, height = 300)
    previewtitle.config(text="You have chosen " + choice)

def game(m):
    frame1.grid_forget()  
    randoms = random.randint(1,3)
    if randoms == 1:
        o = "scissors"
    elif randoms == 2:
        o = "paper"
    else:
        o = "stone"
    show_Image_luck(o) #send to polariser
    preview_Image(m) #for game preview at the side (what user has chosen)


#Create an instance of tkinter frame
main= Tk()  

# Dropdown menu options
options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
optionss = []
d = 32
for x in range (1, d):
    optionss.append(x)

# datatype of menu text
clicked = StringVar()
clickeds = IntVar()


who = date.today()
whos = options[who.month-1]
clicked.set(whos)  #this refers to month
clickeds.set(who.day) #this refers to date

#Header
lucktitle = Label(main, text="What's Your Luck?", font=('Arial', 35))
lucktitle.grid(row=0, columnspan=4)

#This is for dropdown button
frame0 = Frame(main)
frame0.grid(row=1, columnspan=3)

# Create Dropdown menu for month
drop = OptionMenu(frame0, clicked , *options )
drop.grid(row=1, column=0)
drop.config(bg="#ffe4f2", fg="BLACK", activebackground="#ffb3c6", activeforeground="black", height=2, width=30, font=('Arial',15))
drop["menu"].config(bg="#e18aaa", fg="black", activebackground="#ffe4f2", activeforeground="BLACK", font=('Arial',15))

# Create Dropdown menu for date
drops = OptionMenu(frame0, clickeds , *optionss )
drops.grid(row=1, column=1)
drops.config(bg="#ffc2d1", fg="black", activebackground="#ffb7b2", activeforeground="black", height=2, width=30, font=('Arial',15))
drops["menu"].config(bg="#ff9aa2", fg="black", activebackground="#ffb7b2", activeforeground="black", font=('Arial',15))

#Create a Button to handle the update Image event
button= Button(frame0, text= "Enter", command= change_img,  bg="#ff8fab", fg="black", height=2, width=30, font=('Arial',15))
button.grid(row=1, column=2)

#Text
title= Label (main, text="How lucky are you today?", font=('Arial', 25))
title.grid(row=2, columnspan=3)


#Create a Label widget
label= Label(main, image='', text="Input your date of birth and click on the 'Enter' button.", font=('Arial', 25))
label.grid(row=3, columnspan=3)

name = -1
luckpath = "motivationalquotes/luckmain.png"
myImage = Image.open(luckpath)
luckyyImage = ImageTk.PhotoImage(myImage)
luckpic = Label(main, image=luckyyImage)
luckpic.grid(row=4, columnspan=3)

#Pop up for scissors paper stone
frame1 = Frame(main)
frame1.grid(row=4, column=0)
frame1.grid_forget()

#pop up title (scissors paper stone)
label2 = Label(frame1, text = "", font=('Arial', 20))
label2.grid(row=0, columnspan=3)

paths0 = 'scissors paper stone pics/scissors.png'
file0 = Image.open(paths0)
Images0 = file0.resize((300, 300))
img1= ImageTk.PhotoImage(Images0)

paths1 = 'scissors paper stone pics/paper.png'
file1 = Image.open(paths1)
Images1 = file1.resize((300, 300))
img2= ImageTk.PhotoImage(Images1)

paths2 = 'scissors paper stone pics/stone.png'
file2 = Image.open(paths2)
Images2 = file2.resize((300, 300))
img3= ImageTk.PhotoImage(Images2)

#Scissor paper stone pop up button
label3 = Button(frame1, image = img1, command=lambda m=1:game(m), width=300, height=300)
label3.grid(row=1, column=0)

label4 = Button(frame1, image = img2, command=lambda m=2:game(m), width=300, height=300)
label4.grid(row=1, column=1)

label5 = Button(frame1, image = img3, command=lambda m=3:game(m), width=300, height=300)
label5.grid(row=1, column=2)

#preview image of what i have chosen for scissors paper stone
previewtitle = Label(main, text="", font=('Arial', 20))
previewtitle.grid(row=2, column=3)
previewtitle.grid_forget()
imageLabel = Label(main, bg = 'white', width = 30, height = 15)
imageLabel.grid(row=4, column=3)
imageLabel.grid_forget()

main.bind("<Return>", change_img) 
main.mainloop()

