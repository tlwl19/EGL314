from tkinter import *   #import tkinter library
import random
import os 
from PIL import Image, ImageTk, ImageOps
import cartoon

def show_Image(choice):
    path2 = "horo/" + str(choice) + ".png"
    myImage = Image.open(path2)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoon.pixelised(path = path2)
    myImage = Image.open("cartoon.png")

#global score, number, prevent
#number = 15

##number = 15 is to signal that user need to press start game btn/game havent start
##number = 12 is to signal that user pressed start game btn/game started
##number = 13/14 is to signal that user need to press restart game/game havent restart
##number = 12 is to signal that user need to press guess btn after start game btn is pressed
##prevent[] is to stop the counter from adding score+1 if user click more than once on the correct horoscope btn

#The function is for start game
def startgame():
    global score, prevent, number
    #score = 0
    prevent = []
    if number == 15: # before starting the game
        score = 0
        btn0.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) #Show blue colour
        btn1.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn2.config(bg='#b0c8ed', fg="white", image='', width=10, height=5)
        btn3.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn4.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn5.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn6.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn7.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn8.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn9.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn10.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        btn11.config(bg='#b0c8ed', fg="white", image='', width=10, height=5) 
        scoreresults.config(text=str(score),font=('Arial',20))  #It will show 0 when press "Start game"
        number = 12 #to signal that user has pressed the start game btn n to ensure that when user click on the 3x4 grids bef guess btn, it will show press guess btn
        youwin.grid_forget()

#The function is for reset game
def restartgame():
    global score, prevent, number
    #score = 0
    prevent = []
    if number == 13 or number == 14: 
        for i in range(0, 12):
            paths = "horo/" + str(i) + ".png"
            myImages = Image.open(paths)
            myImages = myImages.resize((90, 90))
            loadImages = ImageTk.PhotoImage(myImages)
            widthy = 114
            heighty = 126
            if i == 0:
                btn0.image = loadImages
                btn0.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 1:
                btn1.image = loadImages
                btn1.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 2:
                btn2.image = loadImages
                btn2.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 3:
                btn3.image = loadImages
                btn3.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 4:
                btn4.image = loadImages
                btn4.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 5:
                btn5.image = loadImages
                btn5.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 6:
                btn6.image = loadImages
                btn6.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 7:
                btn7.image = loadImages
                btn7.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 8:
                btn8.image = loadImages
                btn8.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 9:
                btn9.image = loadImages
                btn9.config(image = loadImages, width=widthy, height=heighty, bg='white')
            elif i == 10:
                btn10.image = loadImages
                btn10.config(image = loadImages, width=widthy, height=heighty, bg='white')
            else:
                btn11.image = loadImages
                btn11.config(image = loadImages, width=widthy, height=heighty, bg='white')
        scoreresults.config(text="Press Start Game to Start",font=('Arial',12))  #It will show 0 when press "Reset game"
        number = 15
        youwin.grid_forget()


def guess():
    global number, prevent, numberx, numberxlist
    youwin.grid_forget()
    prevent = []  
    #number = list(range(0,11))
                        #green                          #red                            #blue
    if btn0.cget('bg') == '#7fff00' or btn0.cget('bg') == '#FF0800' or btn0.cget('bg') == '#b0c8ed':
        if btn0.cget('bg') != '#FF0800': #red color 
            numberx = random.randint(0,11) #generate a random no.
            if len(numberxlist) >= 1:
                while numberx == numberxlist[0]:
                    numberx = random.randint(0,11)
                else:
                    numberxlist[0] = numberx
                    print(numberx)
                    show_Image(numberx) #send to polariser the number
            else:
                numberxlist = [numberx]
                print(numberxlist[0])
            number = 0
            btn0.config(bg='#b0c8ed', fg="white")
            btn1.config(bg='#b0c8ed', fg="white") 
            btn2.config(bg='#b0c8ed', fg="white") 
            btn3.config(bg='#b0c8ed', fg="white") 
            btn4.config(bg='#b0c8ed', fg="white") 
            btn5.config(bg='#b0c8ed', fg="white") 
            btn6.config(bg='#b0c8ed', fg="white") 
            btn7.config(bg='#b0c8ed', fg="white") 
            btn8.config(bg='#b0c8ed', fg="white") 
            btn9.config(bg='#b0c8ed', fg="white") 
            btn10.config(bg='#b0c8ed', fg="white")
            btn11.config(bg='#b0c8ed', fg="white") 
        else:
            scoreresults.config(text="Try Again", font=('Arial',15))
    elif btn0.cget('bg') == '#a58fbe': #purple color
        scoreresults.config(text="Press Start Game to Start", font=('Arial',12))
        number = 15
    elif number == 13: # restart
        scoreresults.config(text="Press Reset Game to Reset", font=('Arial',10))
    else: 
        scoreresults.config(text="Press Start Game to Start", font=('Arial',12))


def button(c):
    global number, score, prevent, numberx
    youwin.grid_forget()
    if btn0.cget('bg') == 'white':
        if number == 15:
            scoreresults.config(text="Press Start Game to Start", font=('Arial',12))
        else:
            scoreresults.config(text="Press Reset Game to Reset", font=('Arial',10))
    elif btn0.cget('bg') == '#a58fbe' : #purple color
        scoreresults.config(text="Press Start Game to Start", font=('Arial',12))
    elif number == 12:
        scoreresults.config(text="Press Guess to Start Guessing", font=('Arial',10))
    else :
        if c == numberx:
            #prevent.append(0) #prevent[] is to stop the counter from adding score+1 if user click more than once on the correct horoscope btn
            if prevent == [2]:
                if score >= 1:
                    scoreresults.config(text=str(score), font=('Arial',20))
                else:
                    number = 13
                    scoreresults.config(text=str(score), font=('Arial',20))
            else:
                btn0.config(bg='#7fff00') #show green colour
                btn1.config(bg='#7fff00') 
                btn2.config(bg='#7fff00') 
                btn3.config(bg='#7fff00') 
                btn4.config(bg='#7fff00') 
                btn5.config(bg='#7fff00') 
                btn6.config(bg='#7fff00') 
                btn7.config(bg='#7fff00') 
                btn8.config(bg='#7fff00') 
                btn9.config(bg='#7fff00') 
                btn10.config(bg='#7fff00')
                btn11.config(bg='#7fff00') 
                score = score+1
                number = 13
                prevent = [2]
                print(prevent)
                if score >= 4:
                    scoreresults.config(text='YOU WIN', font=('Arial',20))
                    youwin.grid(row=4, column=2)
                    number = 13
                    btn0.config(bg='white', fg='black')
                    btn1.config(bg='white', fg='black')
                    btn2.config(bg='white', fg='black')
                    btn3.config(bg='white', fg='black')
                    btn4.config(bg='white', fg='black')
                    btn5.config(bg='white', fg='black')
                    btn6.config(bg='white', fg='black')
                    btn7.config(bg='white', fg='black')
                    btn8.config(bg='white', fg='black')
                    btn9.config(bg='white', fg='black')
                    btn10.config(bg='white', fg='black')
                    btn11.config(bg='white', fg='black')
                elif score <= 0:
                    scoreresults.config(text=str(score), font=('Arial',20))
                else:
                    scoreresults.config(text=str(score), font=('Arial',20))
        elif btn0.cget('bg') == '#7fff00':
            prevent.append(0)
            scoreresults.config(text=str(score), font=('Arial',20))
        else:
            btn0.config(bg='#FF0800')  #Show red colour
            btn1.config(bg='#FF0800')
            btn2.config(bg='#FF0800')
            btn3.config(bg='#FF0800')
            btn4.config(bg='#FF0800')
            btn5.config(bg='#FF0800')
            btn6.config(bg='#FF0800')
            btn7.config(bg='#FF0800')
            btn8.config(bg='#FF0800')
            btn9.config(bg='#FF0800')
            btn10.config(bg='#FF0800')
            btn11.config(bg='#FF0800')
            score = score-1
            scoreresults.config(text=str(score), font=('Arial',20))
            print(score)
            #can add number = 13 to restart game
            if score <= 0:
                scoreresults.config(text=str(score), font=('Arial',15))
                if score < -2:
                    scoreresults.config(text='GAME OVER', font=('Arial',20))
                    number = 13
                    btn0.config(bg='white', fg='black')
                    btn1.config(bg='white', fg='black')
                    btn2.config(bg='white', fg='black')
                    btn3.config(bg='white', fg='black')
                    btn4.config(bg='white', fg='black')
                    btn5.config(bg='white', fg='black')
                    btn6.config(bg='white', fg='black')
                    btn7.config(bg='white', fg='black')
                    btn8.config(bg='white', fg='black')
                    btn9.config(bg='white', fg='black')
                    btn10.config(bg='white', fg='black')
                    btn11.config(bg='white', fg='black')


            
main = Tk()   #Create a main window
main.title("Guess the Horoscope") #Title will be shown on the GUI window


#Header for the game
headername = Label(text="Guess the Horoscope", font=('Arial', 30)) 
headername.grid(row=0, columnspan=3)

#Variable Declaration
score = 0
number = 15
numberxlist = []
prevent = [0]

#First frame is created for the 3x4 grid
frame1 = Frame(main)
frame1.grid(row=1, column=0)

imageFrame = Frame(main)
imageFrame.grid(row=0, column=1)

inputrow = 3    #indicate the number of rows
inputcolumn = 4 #indicate the number of cols

for r in range(inputrow):
    for c in range(inputcolumn):
        # Button Section
        btn0 = Button(frame1, text = "Aquarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=0:button(m))
        btn1 = Button(frame1, text = "Aries", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=1:button(m))
        btn2 = Button(frame1, text = "Cancer", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=2:button(m))
        btn3 = Button(frame1, text = "Capricorn", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=3:button(m))
        btn4 = Button(frame1, text = "Gemini", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=4:button(m))
        btn5 = Button(frame1, text = "Leo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=5:button(m))
        btn6 = Button(frame1, text = "Libra", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=6:button(m))
        btn7 = Button(frame1, text = "Pisces", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=7:button(m))
        btn8 = Button(frame1, text = "Sagittarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=8:button(m))
        btn9 = Button(frame1, text = "Scorpio", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=9:button(m))
        btn10 = Button(frame1, text = "Taurus", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=10:button(m))
        btn11 = Button(frame1, text = "Virgo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=11:button(m))

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=1, column=3)
btn8.grid(row=2, column=0)
btn9.grid(row=2, column=1)
btn10.grid(row=2, column=2)
btn11.grid(row=2, column=3)

for i in range(0, 12):
    path = "horo/" + str(i) + ".png"
    myImage = Image.open(path)
    myImage = myImage.resize((100, 100))
    loadImage = ImageTk.PhotoImage(myImage)
    widthx = 114
    heightx = 126
    if i == 0:
        btn0.image = loadImage
        btn0.config(image = loadImage, width=widthx, height=heightx)
    elif i == 1:
        btn1.image = loadImage
        btn1.config(image = loadImage, width=widthx, height=heightx)
    elif i == 2:
        btn2.image = loadImage
        btn2.config(image = loadImage, width=widthx, height=heightx)
    elif i == 3:
        btn3.image = loadImage
        btn3.config(image = loadImage, width=widthx, height=heightx)
    elif i == 4:
        btn4.image = loadImage
        btn4.config(image = loadImage, width=widthx, height=heightx)
    elif i == 5:
        btn5.image = loadImage
        btn5.config(image = loadImage, width=widthx, height=heightx)
    elif i == 6:
        btn6.image = loadImage
        btn6.config(image = loadImage, width=widthx, height=heightx)
    elif i == 7:
        btn7.image = loadImage
        btn7.config(image = loadImage, width=widthx, height=heightx)
    elif i == 8:
        btn8.image = loadImage
        btn8.config(image = loadImage, width=widthx, height=heightx)
    elif i == 9:
        btn9.image = loadImage
        btn9.config(image = loadImage, width=widthx, height=heightx)
    elif i == 10:
        btn10.image = loadImage
        btn10.config(image = loadImage, width=widthx, height=heightx)
    else:
        btn11.image = loadImage
        btn11.config(image = loadImage, width=widthx, height=heightx)

#Second frame is created for the button "GUESS!"
frame2 = Frame(main)
frame2.grid(row=1, column=1)

guessbtn = Button(frame2, text="GUESS!!", font=('Arial',20), command=guess)
guessbtn.grid(row=0, column=1)


#Third frame is created for the 'START/RESET/SCORE' 
frame3 = Frame(main)
frame3.grid(row=1, column=2)

startbtn = Button(frame3, text="START GAME", font=('Arial', 20), bg='yellow', command=startgame)
startbtn.grid(row=0, column=2)

resetbtn = Button(frame3, text="RESET GAME", font=('Arial', 20), bg='pink', command=restartgame)
resetbtn.grid(row=1, column=2)

scorename = Label(frame3, text="Score", font=('Arial', 25)) 
scorename.grid(row=2, column=2)

scoreresults = Label(frame3, text=str(score), font=('Arial', 20))
scoreresults.grid(row=3, column=2)

youwin = Label(frame3, text="Press Reset Game to Reset", font=('Arial', 12))
youwin.grid(row=4, column=2)
youwin.grid_forget()

main.mainloop()  #for the window to stay
