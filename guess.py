from tkinter import *   #import tkinter library
import random
import os 
from PIL import Image, ImageTk
from PIL import student_pub

main = Tk()   #Create a main window
main.title("Guess the Horoscope") #Title will be shown on the GUI window

global score, number, prevent
number = 15
#The function is for start game
def startgame():
    global score, prevent, number
    score = 0
    prevent = []
    if number == 15:
        for r in range(inputrow):
            for c in range(inputcolumn):
                button[c][r].config(bg='#b0c8ed', fg="white") #Show blue colour
        scoreresults.config(text=str(score),font=('Arial',20))  #It will show 0 when press "Start game"
        number = 12 #to signal that userr has press start game btn n to ensure that when user click on the 3x4 grids bef guess btn, it will show press guess btn
        
#The function is for reset game
def restartgame():
    global score, prevent, number
    score = 0
    prevent = []
    if number == 13 or number == 14:
        for r in range(inputrow):
            for c in range(inputcolumn):
                button[c][r].config(bg='#a58fbe', fg="white") #Show purple colour
        scoreresults.config(text="Press Start Game to Start",font=('Arial',12))  #It will show 0 when press "Reset game"
        number = 15


def guess():
    global number, prevent
    
    prevent = []  #WHAT IS prevent[]
    if button[0][0].cget('bg') == '#7fff00' or button[0][0].cget('bg') == '#FF0800' or button[0][0].cget('bg') == '#b0c8ed':
        if button[0][0].cget('bg') != '#FF0800':
            number = random.randint(0,11) #generate a random no. 
            for r in range(inputrow):
                for c in range(inputcolumn):
                    button[c][r].config(bg='#b0c8ed', fg="white")
            print(horoscope[number])#edit this line onw and send the pic over
            path = os.path.abspath('horoscope pics') +'\\' + horoscope[number] + '.png'
            files = path.replace('\\','/')
            myImage = Image.open(files)
            myImage.show()
        else:
            scoreresults.config(text="Try Again", font=('Arial',15))
    elif button[0][0].cget('bg') == '#a58fbe':
        scoreresults.config(text="Press Start Game to Start", font=('Arial',12))
        number = 15
    elif number == 13:
        scoreresults.config(text="Press Reset Game to Reset", font=('Arial',10))
    else: 
        scoreresults.config(text="Press Start Game to Start", font=('Arial',12))


def click(c):
    global number, score, prevent
    if button[0][0].cget('bg') == 'white':
        if number == 15:
            scoreresults.config(text="Press Start Game to Start", font=('Arial',12))
        else:
            scoreresults.config(text="Press Reset Game to Reset", font=('Arial',10))
    elif button[0][0].cget('bg') == '#a58fbe' :
        scoreresults.config(text="Press Start Game to Start", font=('Arial',12))
    elif number == 12:
        scoreresults.config(text="Press Guess to Start Guessing", font=('Arial',10))
    else :
        if c == number:
            prevent.append(0)
            if len(prevent) > 1:
                number = 13
                scoreresults.config(text=str(score), font=('Arial',20))
            else:
                for r in range(inputrow):
                    for c in range(inputcolumn):
                        button[c][r].config(bg='#7fff00') #Show green colour
                score = score+1
                if score <= 0:
                    scoreresults.config(text='+1', font=('Arial',20))
                else:
                    scoreresults.config(text=str(score), font=('Arial',20))
        elif button[0][0].cget('bg') == '#7fff00':
            scoreresults.config(text=str(score), font=('Arial',20))
        else:
            for r in range(inputrow):
                for c in range(inputcolumn):
                    button[c][r].config(bg='#FF0800') #Show red colour
            score = score-1
            scoreresults.config(text=str(score), font=('Arial',20))
            print(score)
            if score <= 0:
                scoreresults.config(text='Try Again', font=('Arial',15))
                if score < -2:
                    scoreresults.config(text='GAME OVER', font=('Arial',20))
                    number = 13
                    prevent.append(0)
                    for r in range(inputrow):
                        for c in range(inputcolumn):
                            button[c][r].config(bg='white', fg='black')


#Header for the game
headername = Label(text="Guess the Horoscope", font=('Arial', 30)) 
headername.grid(row=0, columnspan=3)

#First frame is created for the 3x4 grid
frame1 = Frame(main)
frame1.grid(row=1, column=0)

inputrow = 3    #indicate the number of rows
inputcolumn = 4 #indicate the number of cols
counter = 0
horoscope = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

button = [[r for r in range(inputrow)] for c in range(inputcolumn)]
for r in range(inputrow):
    for c in range(inputcolumn):
        button[c][r] = Button(frame1, text=horoscope[counter], font=('Arial',15), height=5, width=10, bg='white', command=lambda r=counter :click(r)) #button[c][r] start from column first instead of row 
        button[c][r].grid(row=r, column=c) 
        counter = counter+1


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

scoreresults = Label(frame3, text="0", font=('Arial', 20))
scoreresults.grid(row=3, column=2)

main.mainloop()  #for the window to stay
