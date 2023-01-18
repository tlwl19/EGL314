from tkinter import *
from PIL import Image, ImageTk, ImageOps
import os
import random
import cartoon
from datetime import *

def guess():
    global var 
    var = "THIS IS GUESS"
    middleframe.destroy()
    guessframe.grid(row=1, column=0)


def luck():
    global var 
    # var = "THIS IS LUCK"
    middleframe.grid(row=1, column=0)
    guessframe.destroy()



def show_Image(choice):

    if type(choice) == int:
        lucky = "percentage pics/" + str(choice) + ".png"
        myImage = Image.open(lucky)
    else:
        lucky = "scissors paper stone pics/" + choice + ".png"
        myImage = Image.open(lucky)

        #sending to cartoon.py
        #first path refers to input for img
        #path2 refers to variable
    cartoon.pixelised(path = lucky)
    myImage = Image.open("cartoon.png")


def change_img(): 
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
        label.config(text="Kindly, Input your DoB and Press the 'Enter' button")
        randomno = random.randint(0, 4)
        randomnolist = [0,25,50,75,100]
        if randomnolist[randomno] == 75 or randomnolist[randomno] == 100:
            label2.config(text='Would you like to play a game with me? Scissors, Paper, Stone!')
            frame1.grid(row=4, column=1)
            show_Image(randomnolist[randomno])
            imageLabel.config(image="", width = 30, height = 15)
            previewtitle.config(text="")
            previewtitle.grid(row=2, column=3)
            imageLabel.grid(rowspan=2, column=3)
            print(randomnolist[randomno])
        elif randomnolist[randomno] == 0 or randomnolist[randomno] == 25:
            label2.config(text='')
            frame1.grid_forget()
            show_Image(7)#insert genie pic name
            previewtitle.grid_forget()
            imageLabel.grid_forget()
            print(randomnolist[randomno])
        else:
            label2.config(text='')
            frame1.grid_forget()
            previewtitle.grid_forget()
            imageLabel.grid_forget()
            show_Image(randomnolist[randomno])
            print(randomnolist[randomno])
    else:
        label.config(text = "Please input a valid DoB", image='', font=('50px'))

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
    myImages = myImages.resize((250, 250))
    loadImage = ImageTk.PhotoImage(myImages)
    imageLabel.image = loadImage
    imageLabel.config(image = loadImage, width = 250, height = 250)
    previewtitle.config(text="You have choose " + choice)

def game(m):
    frame1.grid_forget()  
    randoms = random.randint(1,3)
    if randoms == 1:
        o = "scissors"
    elif randoms == 2:
        o = "paper"
    else:
        o = "stone"
    show_Image(o)
    preview_Image(m)

def focus():
    global var 
    var = "THIS IS FOCUS"
    tittle.config(text=var)

main = Tk()
main.title("Welcome!")
# main.state("zoom")
# main.geometry('1920x1080')


tittleframe = Frame(main)
tittleframe.grid(row=0, column=0)

middleframe = Frame(main)
# middleframe.grid(row=1, column=0)

modeframe = Frame(main)
modeframe.grid(row=2, column=0)

guessframe = Frame(main)
middlelabel = Label(guessframe, text="THIS IS MIDDLE FRAME")
middlelabel.grid(row=0, column=0)



var = "helloooooooo welcomeeee"
tittle = Label(tittleframe, text=var, font=("Courier", 45))
tittle.grid(row=0, column=0)

guessbtn = Button(modeframe, text="GUESS", font=("Courier", 25), command=guess)
guessbtn.grid(row=0, column=0)
luckbtn = Button(modeframe, text="LUCK", font=("Courier", 25), command=luck)
luckbtn.grid(row=0, column=1)
focusbtn = Button(modeframe, text="FOCUS", font=("Courier", 25), command=focus)
focusbtn.grid(row=0, column=2)

### LUCK GUI
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
clicked.set(whos)  #this refers to month
clickeds.set(who.day) #this refers to date

#This is for dropdown button
frame0 = Frame(middleframe)
frame0.grid(row=1, columnspan=3)

# Create Dropdown menu for month
drop = OptionMenu(frame0, clicked , *options )
drop.grid(row=1, column=0)
drop.config(bg="#ffe4f2", fg="BLACK", activebackground="#e54ed0", activeforeground="WHITE", width=30)
drop["menu"].config(bg="#e54ed0", fg="WHITE", activebackground="#ffe4f2", activeforeground="BLACK")

# Create Dropdown menu for date
drops = OptionMenu(frame0, clickeds , *optionss )
drops.grid(row=1, column=1)
drops.config(bg="#9f45b0", fg="WHITE", activebackground="#44008b", activeforeground="WHITE", width=30)
drops["menu"].config(bg="#44008b", fg="WHITE", activebackground="#9f45b0", activeforeground="WHITE")


#Header
lucktitle = Label(middleframe, text="How is your luck?", font=('Arial', 30))
lucktitle.grid(row=0, columnspan=4)

#Create a Button to handle the update Image event
button= Button(middleframe, text= "Enter", command=change_img,  bg="#00076f", fg="WHITE", width=30)
button.grid(row=1, column=2)

#Text
title= Label (middleframe, text="What's your luck today?", font=('100px'), bg='white', width=30)
title.grid(row=2, columnspan=3)


#Create a Label widget
label= Label(middleframe, image='', text="Kindly, Input your DoB and Press the 'Enter' button", font=('100px'), bg='white')
label.grid(row=3, columnspan=3)


#Pop up for scissors paper stone
frame1 = Frame(middleframe)
frame1.grid(row=4, column=0)
frame1.grid_forget()

#pop up title (scissors paper stone)
label2 = Label(frame1, text = "", font='20px')
label2.grid(row=0, columnspan=3)

paths = os.path.abspath('scissors paper stone pics') +'\\scissors.png'
file = paths.replace('\\','/')
img1= ImageTk.PhotoImage(Image.open(file))

paths = os.path.abspath('scissors paper stone pics') +'\\paper.png'
file = paths.replace('\\','/')
img2= ImageTk.PhotoImage(Image.open(file))

paths = os.path.abspath('scissors paper stone pics') +'\\stone.png'
file = paths.replace('\\','/')
img3= ImageTk.PhotoImage(Image.open(file))

#Scissor paper stone pop up button
label3 = Button(frame1, image = img1, command=lambda m=1:game(m))
label3.grid(row=1, column=0)

label4 = Button(frame1, image = img2, command=lambda m=2:game(m))
label4.grid(row=1, column=1)

label5 = Button(frame1, image = img3, command=lambda m=3:game(m))
label5.grid(row=1, column=2)

#preview image of what i have chosen for scissors paper stone
previewtitle = Label(middleframe, text="", font=('Arial', 15))
previewtitle.grid(row=2, column=3)
previewtitle.grid_forget()
imageLabel = Label(middleframe, bg = 'white', width = 30, height = 15)
imageLabel.grid(rowspan=2, column=3)
imageLabel.grid_forget()

main.bind("<Return>", change_img) 

main.mainloop()