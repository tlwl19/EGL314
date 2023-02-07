from tkinter import *   #import tkinter library
import random
import os 
from PIL import Image, ImageTk, ImageOps
from PIL import ImageDraw
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

##number = 17 is to signal game ended
##number = 16 is to signal user pressed guess
##number = 15 is to signal that user need to press start game btn/game havent start
##number = 13/14 is to signal that user need to press restart game/game havent restart
##number = 12 is to signal that user need to press guess btn after start game btn is pressed
##prevent[] is to stop the counter from adding score+1 if user click more than once on the correct horoscope btn

#The function is for start game
def startgame():
    global score, prevent, number, prevent2
    prevent = []
    prevent2 = 0
    if number == 15: # before starting the game
        score = 0
        btn0.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) #Show blue colour
        btn1.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn2.config(bg='#C3B1E1', fg="black", image='', width=10, height=5)
        btn3.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn4.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn5.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn6.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn7.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn8.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn9.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn10.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        btn11.config(bg='#C3B1E1', fg="black", image='', width=10, height=5) 
        scoreresults.config(text=str(score),font=('Arial',20))  #It will show 0 when press "Start game"
        number = 12 #to signal that user has pressed the start game btn n to ensure that when user click on the 3x4 grids bef guess btn, it will show press guess btn
        guess()
        lbl0.grid_forget()
        lbl1.grid_forget()
        lbl2.grid_forget()
        lbl3.grid_forget()
        lbl4.grid_forget()
        lbl5.grid_forget()
        lbl6.grid_forget()
        lbl7.grid_forget()
        lbl8.grid_forget()
        lbl9.grid_forget()
        lbl10.grid_forget()
        lbl11.grid_forget()
        startbtn['state']='disabled'
    elif number == 18:
        youwin.config(text="Press any button to continue ", font=('Arial',10))
        youwin.grid(row=4, column=2)


#The function is for reset game
def restartgame():
    global score, prevent, number, prevent2
    prevent = []  
    #prevent2 = 0
    if number == 13 or number == 14 or number == 17 or number == 18: #restart
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
        startbtn['state']='normal'
        youwin.grid_forget()
        btn0.grid(row=0, column=0)
        lbl0.grid(row=1, column=0)
        btn1.grid(row=0, column=1)
        lbl1.grid(row=1, column=1)
        btn2.grid(row=0, column=2)
        lbl2.grid(row=1, column=2)
        btn3.grid(row=0, column=3)
        lbl3.grid(row=1, column=3)

        btn4.grid(row=2, column=0)
        lbl4.grid(row=3, column=0)
        btn5.grid(row=2, column=1)
        lbl5.grid(row=3, column=1)
        btn6.grid(row=2, column=2)
        lbl6.grid(row=3, column=2)
        btn7.grid(row=2, column=3)
        lbl7.grid(row=3, column=3)

        btn8.grid(row=4, column=0)
        lbl8.grid(row=5, column=0)
        btn9.grid(row=4, column=1)
        lbl9.grid(row=5, column=1)
        btn10.grid(row=4, column=2)
        lbl10.grid(row=5, column=2)
        btn11.grid(row=4, column=3)
        lbl11.grid(row=5, column=3)

def guess():
    global number, prevent, numberx, numberxlist, prevent2, prevent3
    prevent = []  
    prevent2 = [2]
    prevent3 = 0
    if number == 12 or number == 18:
        number = 16
        youwin.config(text="Guess the horoscope!", font=('Arial',12))
        numberx = random.randint(0,11) #generate a random no.
        while len(numberxlist) == 12:
            numberxlist = []
        if len(numberxlist) >= 1: #to check if there is smth in the list
            while numberx in numberxlist:  #if hv smth in the list
                numberx = random.randint(0,11) #regenerate the number that is not the same as the previous
            else:
                numberxlist.append(numberx) #else store the random generated number when the list is empty
                print(numberxlist)
                show_Image(numberx) #send to polariser the number
        else:
            numberxlist = [numberx]
            print(numberxlist)
            show_Image(numberx) #send to polariser the number
        btn0.config(bg='#C3B1E1', fg="black")
        btn1.config(bg='#C3B1E1', fg="black") 
        btn2.config(bg='#C3B1E1', fg="black") 
        btn3.config(bg='#C3B1E1', fg="black") 
        btn4.config(bg='#C3B1E1', fg="black") 
        btn5.config(bg='#C3B1E1', fg="black") 
        btn6.config(bg='#C3B1E1', fg="black") 
        btn7.config(bg='#C3B1E1', fg="black") 
        btn8.config(bg='#C3B1E1', fg="black") 
        btn9.config(bg='#C3B1E1', fg="black") 
        btn10.config(bg='#C3B1E1', fg="black")
        btn11.config(bg='#C3B1E1', fg="black") 
    elif number == 13 or number == 17 or number == 14: # restart
        youwin.config(text="Press Reset Game to Reset", font=('Arial',12))
    elif number == 15: 
        youwin.config(text="Press Start Game to Start", font=('Arial',12))
    else:
        youwin.config(text="Select one horoscope!", font=('Arial',12))

def button(c):
    global number, score, prevent, numberx, prevent2, quoteno, quotelist, prevent3
    quotelist = ["'You don’t have to control your thoughts. You just have to stop letting them control you.' — Dan Millman",
     "'There is a crack in everything, that’s how the light gets in.' ― Leonard Cohen",
     "'Deep breathing is our nervous system’s love language.' — Dr. Lauren Fogel Mersy",
     "'You are not your illness. You have an individual story to tell. You have a name, a history, a personality. Staying yourself is part of the battle.' — Julian Seifter",
     "'Happiness can be found even in the darkest of times, if one only remembers to turn on the light.' — Albus Dumbledore",
     "'Vulnerability sounds like truth and feels like courage. Truth and courage aren’t always comfortable, but they're never weakness.' — Brené Brown",
     "'Promise me you’ll always remember: You’re braver than you believe, and stronger than you seem, and smarter than you think.' — Christopher Robin from Winnie the Pooh",
     "'Just because no one else can heal or do your inner work for you doesn’t mean you can, should, or need to do it alone.' – Lisa Olivera",
     "'There is hope, even when your brain tells you there isn’t.' — John Green",
     "'There is no normal life that is free of pain. It's the very wrestling with our problems that can be the impetus for our growth.' — Fred Rogers",
     "'You don’t have to be positive all the time. It’s perfectly okay to feel sad, angry, annoyed, frustrated, scared and anxious. Having feelings doesn’t make you a negative person. It makes you human.' — Lori Deschene",
     "'Nothing can dim the light that shines from within.' — Maya Angelou"]
    if number == 15:
        youwin.config(text="Press Start Game to Start", font=('Arial',12))
    elif number == 17: #after game ended 
        youwin.config(text="Press Reset Game to Reset", font=('Arial',12))
    elif number == 14:
        scoreresults.config(text='YOU WIN', font=('Arial',20))
        youwin.config(text="Press Reset Game to Reset", font=('Arial',12))
        youwin.grid(row=4, column=2)
    elif number == 13:
        youwin.config(text="Press Start Game to Start", font=('Arial',12))
    elif number == 12:
        youwin.config(text="Press Guess to Start Guessing", font=('Arial',10))
    else: #number = 16 guess is pressed
        if c == numberx:
            if quoteno >= len(quotelist)-1:
                quoteno = -1
            quoteno=quoteno+1
            quote.config(text=quotelist[quoteno], bg='white')
            prevent2 = [0]
            if prevent == [2]:
                number = 18 #restart
                guess()
            else:
                if c == 0:
                    btn0.config(bg="#7fff00")
                elif c == 1:
                    btn1.config(bg="#7fff00")
                elif c == 2:
                    btn2.config(bg="#7fff00")
                elif c == 3:
                    btn3.config(bg="#7fff00")
                elif c == 4:
                    btn4.config(bg="#7fff00")
                elif c == 5:
                    btn5.config(bg="#7fff00")
                elif c == 6:
                    btn6.config(bg="#7fff00")
                elif c == 7:
                    btn7.config(bg="#7fff00")
                elif c == 8:
                    btn8.config(bg="#7fff00")
                elif c == 9:
                    btn9.config(bg="#7fff00")
                elif c == 10:
                    btn10.config(bg="#7fff00")
                else:
                    btn11.config(bg="#7fff00")
                score = score+1
                prevent = [2]
                number = 18
                print(prevent)
                if score >= 4:
                    scoreresults.config(text='YOU WIN', font=('Arial',20))
                    youwin.config(text="Press Reset Game to Reset", font=('Arial',12))
                    youwin.grid(row=4, column=2)
                    number = 14
                    color = '#cbc3e3'
                    btn0.config(bg=color, fg='black')
                    btn1.config(bg=color, fg='black')
                    btn2.config(bg=color, fg='black')
                    btn3.config(bg=color, fg='black')
                    btn4.config(bg=color, fg='black')
                    btn5.config(bg=color, fg='black')
                    btn6.config(bg=color, fg='black')
                    btn7.config(bg=color, fg='black')
                    btn8.config(bg=color, fg='black')
                    btn9.config(bg=color, fg='black')
                    btn10.config(bg=color, fg='black')
                    btn11.config(bg=color, fg='black')
                else:
                    scoreresults.config(text=str(score), font=('Arial',20))
                    youwin.config(text="Press any button to continue ", font=('Arial',10))
                    youwin.grid(row=4, column=2)
        else:
            if prevent3 == 0:
                if quoteno >= len(quotelist)-1:
                    quoteno = -1
                quoteno=quoteno+1
                prevent3 = 1
                quote.config(text=quotelist[quoteno], bg='white')
            if prevent2 == [0]:
                number = 18
                guess()
            else:
                if c == 0:
                    btn0.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 1:
                    btn1.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 2:
                    btn2.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 3:
                    btn3.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 4:
                    btn4.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 5:
                    btn5.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 6:
                    btn6.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 7:
                    btn7.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 8:
                    btn8.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 9:
                    btn9.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                elif c == 10:
                    btn10.config(bg="#FF0800")
                    prevent2 = [4]
                    prevent3 = 1
                else:
                    btn11.config(bg="#FF0800")
                    prevent3 = 1
                    prevent2 = [4]

                if prevent2 == [4] or prevent3 == 1:
                    quoteno = quoteno
                    youwin.config(text="Choose another horoscope", font=('Arial',12))
            print(score)
            
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
prevent2 = [2]
quoteno = -1

#First frame is created for the 3x4 grid
frame1 = Frame(main)
frame1.grid(row=1, column=0)

imageFrame = Frame(main)
imageFrame.grid(row=0, column=1)

inputrow = 6    #indicate the number of rows
inputcolumn = 4 #indicate the number of cols

for r in range(inputrow):
    for c in range(inputcolumn):
        # Button Section
        btn0 = Button(frame1, text = "Aquarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=0:button(m))
        lbl0 = Label(frame1, text="Aquarius", font=("Arial", 15), fg='black')
        btn1 = Button(frame1, text = "Aries", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=1:button(m))
        lbl1 = Label(frame1, text="Aries", font=("Arial", 15), fg='black')
        btn2 = Button(frame1, text = "Cancer", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=2:button(m))
        lbl2 = Label(frame1, text="Cancer", font=("Arial", 15), fg='black')
        btn3 = Button(frame1, text = "Capricorn", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=3:button(m))
        lbl3 = Label(frame1, text="Capricorn", font=("Arial", 15), fg='black')
        btn4 = Button(frame1, text = "Gemini", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=4:button(m))
        lbl4 = Label(frame1, text="Gemini", font=("Arial", 15), fg='black')
        btn5 = Button(frame1, text = "Leo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=5:button(m))
        lbl5 = Label(frame1, text="Leo", font=("Arial", 15), fg='black')
        btn6 = Button(frame1, text = "Libra", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=6:button(m))
        lbl6 = Label(frame1, text="Libra", font=("Arial", 15), fg='black')
        btn7 = Button(frame1, text = "Pisces", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=7:button(m))
        lbl7 = Label(frame1, text="Pisces", font=("Arial", 15),fg='black')
        btn8 = Button(frame1, text = "Sagittarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=8:button(m))
        lbl8 = Label(frame1, text="Sagittarius", font=("Arial", 15), fg='black')
        btn9 = Button(frame1, text = "Scorpio", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=9:button(m))
        lbl9 = Label(frame1, text="Scorpio", font=("Arial", 15), fg='black')
        btn10 = Button(frame1, text = "Taurus", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=10:button(m))
        lbl10 = Label(frame1, text="Taurus", font=("Arial", 15), fg='black')
        btn11 = Button(frame1, text = "Virgo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=11:button(m))
        lbl11 = Label(frame1, text="Virgo", font=("Arial", 15), fg='black')

btn0.grid(row=0, column=0)
lbl0.grid(row=1, column=0)
btn1.grid(row=0, column=1)
lbl1.grid(row=1, column=1)
btn2.grid(row=0, column=2)
lbl2.grid(row=1, column=2)
btn3.grid(row=0, column=3)
lbl3.grid(row=1, column=3)
btn4.grid(row=2, column=0)
lbl4.grid(row=3, column=0)
btn5.grid(row=2, column=1)
lbl5.grid(row=3, column=1)
btn6.grid(row=2, column=2)
lbl6.grid(row=3, column=2)
btn7.grid(row=2, column=3)
lbl7.grid(row=3, column=3)

btn8.grid(row=4, column=0)
lbl8.grid(row=5, column=0)
btn9.grid(row=4, column=1)
lbl9.grid(row=5, column=1)
btn10.grid(row=4, column=2)
lbl10.grid(row=5, column=2)
btn11.grid(row=4, column=3)
lbl11.grid(row=5, column=3)

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
        

#Second frame is created for the 'START/RESET/SCORE' 
frame2 = Frame(main)
frame2.grid(row=1, column=2)

startbtn = Button(frame2, text="START GAME", font=('Arial', 20), bg='#E0B0FF', command=startgame)
startbtn.grid(row=0, column=2)

resetbtn = Button(frame2, text="RESET GAME", font=('Arial', 20), bg='#B47EE5', command=restartgame)
resetbtn.grid(row=1, column=2)

scorename = Label(frame2, text="Score", font=('Arial', 25)) 
scorename.grid(row=2, column=2)

scoreresults = Label(frame2, text=str(score), font=('Arial', 20))
scoreresults.grid(row=3, column=2)

youwin = Label(frame2, text="Press Start Game to Start", font=('Arial', 12))
youwin.grid(row=4, column=2)

quote = Label(frame2, text="", font=('Arial', 12), wraplength=300)
quote.grid(row=5, column=2)

main.mainloop()  #for the window to stay