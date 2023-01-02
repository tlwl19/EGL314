from tkinter import *   #import tkinter library
import random

main = Tk()   #Create a main window
main.title("Guess the Horoscope") #Title will be shown on the GUI window

score = 0 #create a global score variable

#The function is for reset and start game
def game():
    for r in range(inputrow):
        for c in range(inputcolumn):
            button[c][r].config(bg='white')

#The function is for the scores 
def results():
    score = score + 1
    scoreresults.config(text=score)

#The function is for guess btn to take from random generator
def guess():
    n = random.randint(0,11) #number indicating the horoscope
    print(n) #have to change it to print image


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
        button[c][r] = Button(frame1, text=horoscope[counter], font=('Arial',15), height=5, width=10, bg='white') #button[c][r] start from column first instead of row 
        button[c][r].grid(row=r, column=c) 
        counter = counter+1


#Second frame is created for the button "GUESS!"
frame2 = Frame(main)
frame2.grid(row=1, column=1)

guessbtn = Button(frame2, text="GUESS!!", font=('Arial',20))
guessbtn.grid(row=0, column=1)


#Third frame is created for the 'START/RESET/SCORE' 
frame3 = Frame(main)
frame3.grid(row=1, column=2)

startbtn = Button(frame3, text="START GAME", font=('Arial', 20), command=game)
startbtn.grid(row=0, column=2)

resetbtn = Button(frame3, text="RESET GAME", font=('Arial', 20), command=game)
resetbtn.grid(row=1, column=2)

scorename = Label(frame3, text="Score", font=('Arial', 25)) 
scorename.grid(row=2, column=2)

scoreresults = Label(frame3, text="0", font=('Arial', 20))
scoreresults.grid(row=3, column=2)



main.mainloop()  #for the window to stay