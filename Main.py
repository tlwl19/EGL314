from tkinter import *   #import tkinter library
import os 
from PIL import Image, ImageTk, ImageOps
import cartoon
import random
from datetime import *
from datetime import datetime
from tkinter import messagebox, simpledialog
from tkinter.font import Font
from tkinter import ttk
from student_pub import *

main = Tk()
main.title("Mental Wellness")
main.rowconfigure(1, weight=1)
main.columnconfigure(0, weight=1)

#MAIN PAGE
#To navigate to MAIN page
def mainappear(): 
    guessframe.grid_forget()
    focusframe.grid_forget()
    luckframe.grid_forget()
    drawingframe.grid_forget()
    mainframe.grid(row=0, column=0)

#Create my own font for header
header_font = Font(
    family = 'Times', 
    size = 30,
    weight = 'bold',
    slant = 'roman',
)

quote_font = Font(
    family = 'Typewriter', 
    size = 15,
    weight = 'bold',
    slant = 'roman',
)

#FRAME for Top/Middle/Mode
topframe = Frame(main) #Header
topframe.grid(row=0, column=0)

middleframe = Frame(main) #Feature
middleframe.grid(row=1, column=0)

modeframe = Frame(main) #Mode
modeframe.grid(row=2, column=0)

#ALWAYS APPEAR IN ALL GAME PAGE
headertitle = Button(topframe, text="Fun Ways to Approach MENTAL WELLNESS", font=header_font, fg = '#6495ED', activeforeground='#C3B1E1', command=mainappear, padx=250)
headertitle.grid(row=0, column=0)



#MAIN PAGE GUI
mainframe = Frame(middleframe)
mainframe.grid(row=0, column=0)

quotevar = "Mental Health.. is not a destination, but a process. It's about how you drive, not where you're going.\n \n-NOAM SHPANCER, PHD"
quote = Label(mainframe, text=quotevar, font=quote_font, bg='#DBDBDB', padx=50 ,pady=50)
quote.grid(row=0, column=0)

descvar = "Mental Wellness is an internal resource that helps us THINK, FEEL, CONNECT, and FUNCTION."
desc = Label(mainframe, text=descvar, font=('Arial', 20), pady=25) 
desc.grid(row=1, column=0)

mentalpath = "wellness/mental.jpg"
myImage = Image.open(mentalpath)
mentalImage = ImageTk.PhotoImage(myImage)
mentalpic = Label(mainframe, image=mentalImage)
mentalpic.grid(row=2, column=0)


#GUESS PAGE
 ################## GUESS FUNCTION ######################
def show_Image(choice1):
    path2 = "horo/" + str(choice1) + ".png"
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
    #prevent2 = 0
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

def horobutton(c):
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
   #quotelist = ['1']
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
            quote.config(text=quotelist[quoteno])
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
                quote.config(text=quotelist[quoteno])
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

# To navigate to GUESS page
def guessappear(): #guess appear but the rest disappear
    luckframe.grid_forget()
    focusframe.grid_forget()
    mainframe.grid_forget()
    drawingframe.grid_forget()
    guessframe.grid(row=0, column=0)

#GUESS GUI
# ################## GUESS #######################
guessframe = Frame(middleframe)

#Header for the game
headername = Label(guessframe, text="Guess the Horoscope", font=('Arial', 30)) 
headername.grid(row=0, columnspan=3)

#Variable Declaration
score = 0
number = 15
numberxlist = []
prevent = [0]
prevent2 = [2]
quoteno = -1

#First frame is created for the 3x4 grid
inguessframe = Frame(guessframe)
inguessframe.grid(row=1, column=0)

imageFrame = Frame(guessframe)
imageFrame.grid(row=0, column=1)

inputrow = 6    #indicate the number of rows
inputcolumn = 4 #indicate the number of cols

for r in range(inputrow):
    for c in range(inputcolumn):
        # Button Section
        btn0 = Button(inguessframe, text = "Aquarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=0:horobutton(m))
        lbl0 = Label(inguessframe, text="Aquarius", font=("Arial", 15), fg='black')
        btn1 = Button(inguessframe, text = "Aries", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=1:horobutton(m))
        lbl1 = Label(inguessframe, text="Aries", font=("Arial", 15), fg='black')
        btn2 = Button(inguessframe, text = "Cancer", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=2:horobutton(m))
        lbl2 = Label(inguessframe, text="Cancer", font=("Arial", 15), fg='black')
        btn3 = Button(inguessframe, text = "Capricorn", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=3:horobutton(m))
        lbl3 = Label(inguessframe, text="Capricorn", font=("Arial", 15), fg='black')
        btn4 = Button(inguessframe, text = "Gemini", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=4:horobutton(m))
        lbl4 = Label(inguessframe, text="Gemini", font=("Arial", 15), fg='black')
        btn5 = Button(inguessframe, text = "Leo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=5:horobutton(m))
        lbl5 = Label(inguessframe, text="Leo", font=("Arial", 15), fg='black')
        btn6 = Button(inguessframe, text = "Libra", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=6:horobutton(m))
        lbl6 = Label(inguessframe, text="Libra", font=("Arial", 15), fg='black')
        btn7 = Button(inguessframe, text = "Pisces", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=7:horobutton(m))
        lbl7 = Label(inguessframe, text="Pisces", font=("Arial", 15),fg='black')
        btn8 = Button(inguessframe, text = "Sagittarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=8:horobutton(m))
        lbl8 = Label(inguessframe, text="Sagittarius", font=("Arial", 15), fg='black')
        btn9 = Button(inguessframe, text = "Scorpio", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=9:horobutton(m))
        lbl9 = Label(inguessframe, text="Scorpio", font=("Arial", 15), fg='black')
        btn10 = Button(inguessframe, text = "Taurus", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=10:horobutton(m))
        lbl10 = Label(inguessframe, text="Taurus", font=("Arial", 15), fg='black')
        btn11 = Button(inguessframe, text = "Virgo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=11:horobutton(m))
        lbl11 = Label(inguessframe, text="Virgo", font=("Arial", 15), fg='black')

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
inguessframe2 = Frame(guessframe)
inguessframe2.grid(row=1, column=2)

startbtn = Button(inguessframe2, text="START GAME", font=('Arial', 20), bg='#E0B0FF', command=startgame)
startbtn.grid(row=0, column=2)

resetbtn = Button(inguessframe2, text="RESET GAME", font=('Arial', 20), bg='#B47EE5', command=restartgame)
resetbtn.grid(row=1, column=2)

scorename = Label(inguessframe2, text="Score", font=('Arial', 25)) 
scorename.grid(row=2, column=2)

scoreresults = Label(inguessframe2, text=str(score), font=('Arial', 20))
scoreresults.grid(row=3, column=2)

youwin = Label(inguessframe2, text="Press Start Game to Start", font=('Arial', 12))
youwin.grid(row=4, column=2)

quote = Label(inguessframe2, text="",bg='white', font=('Arial', 12), wraplength=300)
quote.grid(row=5, column=2)



# LUCK PAGE
# ################## LUCK FUNCTION ###################
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
            frame1.grid(row=4, column=0)  #For the selection of scissors,paper,stone
            show_Image_luck(randomnolist[randomno])
            imageLabel.config(image="", width = 30, height = 15)
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
        label.config(text = "Please input a valid date of birth.", image='', font=('50px'))

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

# To navigate to LUCK page
def luckappear(): 
    guessframe.grid_forget()
    focusframe.grid_forget()
    mainframe.grid_forget()
    drawingframe.grid_forget()
    luckframe.grid(row=0, column=0)


#LUCK GUI
# ################## LUCK #######################
luckframe = Frame(middleframe)

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
lucktitle = Label(luckframe, text="What's Your Luck?", font=('Arial', 30))
lucktitle.grid(row=0, columnspan=4)

#This is for dropdown button
frame0 = Frame(luckframe)
frame0.grid(row=1, columnspan=3)

# Create Dropdown menu for month
drop = OptionMenu(frame0, clicked , *options )
drop.grid(row=1, column=0)
drop.config(bg="#ffe4f2", fg="BLACK", activebackground="#ffb3c6", activeforeground="black", width=30)
drop["menu"].config(bg="#e18aaa", fg="black", activebackground="#ffb3c6", activeforeground="BLACK")

# Create Dropdown menu for date
drops = OptionMenu(frame0, clickeds , *optionss )
drops.grid(row=1, column=1)
drops.config(bg="#ffc2d1", fg="black", activebackground="#ffb7b2", activeforeground="black", width=30)
drops["menu"].config(bg="#ff9aa2", fg="black", activebackground="#ffb7b2", activeforeground="black")

#Create a Button to handle the update Image event
button= Button(frame0, text= "Enter", command= change_img,  bg="#ff8fab", fg="black", width=30)
button.grid(row=1, column=2)

#Text
title= Label (luckframe, text="How lucky are you today?", font=('100px'), width=30)
title.grid(row=2, columnspan=3)


#Create a Label widget
label= Label(luckframe, image='', text="Input your date of birth and click on the 'Enter' button.", font=('100px'))
label.grid(row=3, columnspan=3)

name = -1
luckpath = "motivationalquotes/luckmain.png"
myImage = Image.open(luckpath)
luckyyImage = ImageTk.PhotoImage(myImage)
luckpic = Label(luckframe, image=luckyyImage)
luckpic.grid(row=4, column=0)

#Pop up for scissors paper stone
frame1 = Frame(luckframe)
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
previewtitle = Label(luckframe, text="", font=('Arial', 15))
previewtitle.grid(row=2, column=3)
previewtitle.grid_forget()
imageLabel = Label(luckframe, bg = 'white', width = 30, height = 15)
imageLabel.grid(row=4, column=3)
imageLabel.grid_forget()

main.bind("<Return>", change_img)  


#FOCUS PAGE
# ################### FOCUS FUNCTION #################
counter = 0   #Time starts from 0
running = False  #Timer is not running

def show_Image_focus(choice3):
    global icons
    path2 = "icons/" + str(icons[choice3]) + ".png"
    myImage = Image.open(path2)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoon.pixelised(path = path2)
    myImage = Image.open("cartoon.png")

def getinstruction():
    messagebox.showinfo("Instructions", "1. Click on the 'START' button to begin.\n2. Click on the correct button corresponding to the image shown on the polariser.\n3. You will proceed on to the next level if you select the correct answer.\n4. The game will reset if you select the incorrect answer.")


def click():
    global numberxlist
    numberx = random.randint(0,5) #generate a random no.
    if len(numberxlist) >= 1:   #If there is number inside
        while numberx == numberxlist[0]: #To check if the random int is the same as the previous random generate int
            numberx = random.randint(0,5)
        else:
            numberxlist[0] = numberx #New random int 
            print(numberx)
    else:
        numberxlist = [numberx]  #To store the first random generator int
        print(numberxlist[0])
    show_Image_focus(numberx) #send to polariser the number

def getname():
    name = simpledialog.askstring("Test", "What's your Name?:")
    return name

def correctbox():
    global storetime
    name = getname()
    messagebox.showinfo("Congrats {}".format(name)+" !","You're 100% focus! You've completed in {} s".format(storetime)+" !")

def wrongbox():
    messagebox.showinfo("Try Again!", "You need to improve on your focus!")

def timeup():
    messagebox.showinfo("TIMES UP!!", "TIMESS UPP!!, You need to improve on your concentration")
    

# start function of the stopwatch
def Start(label):
    global running, Lno
    running=True
    counter_label(label) #To start the timer
    start['state']='disabled'  #Start btn will be disabled once my start btn is pressed
    for i in range (0, 6): 
        btn[i]['state']='normal' #Selection btn will be enabled
    click()  #Generate random int and send to the polarizer (show_image)
   
# Stop function of the stopwatch
def Stop(m):
    global running, numberxlist, Lno, counter, storetime, display
    running = False
    print('stop')
    for i in range (0, 6): 
        btn[i]['state']='disabled'
    if m == numberxlist[0]:  #If what i choose is the same as what is being sent, 
        Lno = Lno+1  #Level increase by 1
        storetime = storetime + counter-1
        Reset(timer) #Timer reset to 0
        if Lno == 4: #Level will stop till level 3
            Lno = 0
            Reset(timer)
            correctbox() #User pop up will appear
            storetime = 0
    elif m == 10: #When timer reach 10sec,
        Lno = 0  #Level reset to 0
        Reset(timer)
        timeup()
    else:
        Lno = 0     #When user select wrg btn, level goes back to 0
        wrongbox()
        Reset(timer)
        print('wrong')

# Reset function of the stopwatch
def Reset(label):
    global counter, Lno, icons, storetime
    counter=0
   
    # If rest is pressed after pressing stop.
    if running==False:  #When timer is not running
        start['state']='normal'      
        label['text']='Welcome!'
        level['text']='Level '+ str(Lno)
        if Lno == 1:
            icons = ['KFC', 'Jollibee', 'Popeyes', 'Pizza Hut', 'Mos Burger', 'Texas Chicken']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 2:
            icons = ['Puma', 'Converse', 'Fila', 'Nike', 'Under Armour', 'Reebok']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 3:
            icons = ['Ferrari', 'Mazda', 'Mitsubishi', 'Rolls Royce', 'Honda', 'Mercedes']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        else:
            icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']  #Level 0
            for i in range (0, 6):
                btn[i]['text']=icons[i]

def counter_label(label):
    def count():
        if running:
            global counter, display

            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("00:00:%S")
            display=string
            label['text']=display
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            timer.after(1000, count) 
            counter += 1
            #print(counter)
            if counter > 20:
                Stop(10)
           
    # Triggering the start of the counter.
    count()


# To navigate to FOCUS page
def focusappear():
    luckframe.grid_forget()
    guessframe.grid_forget()
    mainframe.grid_forget()
    drawingframe.grid_forget()
    focusframe.grid(row=0, column=0)


# FOCUS GUI
#################### FOCUS GUI ####################
focusframe = Frame(middleframe)

numberxlist = []
Lno = 0
storetime = 0

#Header for the game
headername = Label(focusframe, text="ICONcentrate", font=('Arial', 30), fg='#4542fb') 
headername.grid(row=0, column=0)

#Instructions
instrubtn = Button(focusframe, text='Instructions', font=('Arial', 15), bg = '#a4c6eb', fg='black', command=getinstruction)
instrubtn.grid(row=1, column=0)

midframe = Frame(focusframe)
midframe.grid(row=2, columnspan=6)

#Level
level = Label(midframe, text='Level '+ str(Lno), font=('Arial', 15))
level.grid(row=2, column=0)

#Timer
timer = Label(midframe, text='Welcome', font=('Arial', 15))
timer.grid(row=2, column=1, padx=100)

start = Button(midframe, text='Start', font=('Arial', 15), command=lambda:Start(timer))
start.grid(row=2, column=2, ipadx=30)


#Answer btn
frameone = Frame(focusframe)
frameone.grid(row=3, column=0)

icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']  #Level 0
btn = [i for i in range(len(icons))]  #defining the number of buttons

for i in range (0, 6):  #Assigning array values into btn 
    btn[i] = Button(frameone, text=icons[i], state='disabled', width=10, height=2, font=("Courier", 15), command=lambda m=i:Stop(m), wraplength=130) #so that texaschicken text can fully show on the button
    btn[i].grid(row=0, column=i)



#DRAW PAGE
########################### DRAW FUNCTION #########################
# Function to choose colour
def choose_colour(m):
    global colour #Value of the colour selected
    colour = m


def colour_picker(r, c):
  global colour
  if colour == 0:
      button[r][c].config(bg='grey99') #to configure the background colour of the grid selected with the selected colour
      value[r][c] = colour #assign the grid's angle value based on the colour selected
  elif colour == 20:
      button[r][c].config(bg='grey88')
      value[r][c] = colour
  elif colour == 30:
      button[r][c].config(bg='grey77')
      value[r][c] = colour
  elif colour == 40:
      button[r][c].config(bg='grey66')
      value[r][c] = colour
  elif colour == 50:
      button[r][c].config(bg='grey44')
      value[r][c] = colour
  elif colour == 60:
      button[r][c].config(bg='grey33')
      value[r][c] = colour
  elif colour == 70:
      button[r][c].config(bg='grey11')
      value[r][c] = colour
  else:
      button[r][c].config(bg='grey1') 
      value[r][c] = colour


def sendbtn():
  global value
  print(value)
  #pubpic(value)


def allwht():
  for r in range (32):
    for c in range (32):
      button[r][c].config(bg='grey99')
      value[r][c] = 0  #This is the angle of grey99
  canvas.config(bg = 'white')
  for r in range(800):
    for c in range(800):
      canvasdraw[r][c] = 0


def allblk():
  for r in range (32):
    for c in range (32):
      button[r][c].config(bg='grey1')
      value[r][c] = 90 #This is the angle of grey1
  canvas.config(bg = 'black')
  for r in range(800):
    for c in range(800):
      canvasdraw[r][c] = 90

 

def get_x_and_y(event): #get coordinates on canvas
   global getx, gety
   getx, gety = event.x, event.y


def paint(event):   #creating line
    global getx, gety, value
    if getx >= 0 and getx <= 799 and gety >= 0 and gety <= 799:
      if colour == 0: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey99',width=4)  #event.x is the position of the mouse relative to the widget
          canvasdraw[getx][gety] = 0   #store position in canvasdraw
      elif colour == 20:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey88',width=4)
          canvasdraw[getx][gety] = 20
      elif colour == 30:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey77',width=4)
          canvasdraw[getx][gety] = 30
      elif colour == 40: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey66',width=4)
          canvasdraw[getx][gety] = 40
      elif colour == 50:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey44',width=4)
          canvasdraw[getx][gety] = 50
      elif colour == 60: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey33',width=4)
          canvasdraw[getx][gety] = 60
      elif colour == 70:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey22',width=4)
          canvasdraw[getx][gety] = 70
      else: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey11',width=4)
          canvasdraw[getx][gety] = 90
      get_x_and_y(event)


def save_draw_colour(list):  #number convert to colour
  global value
  for r in range(32):    
    for c in range(32):
      if list[r][c] == 0: 
        button[c][r].config(bg='grey99')
        value[c][r] = 0
      elif list[r][c] == 20: 
        button[c][r].config(bg='grey88')
        value[c][r] = 20
      elif list[r][c] == 30:
        button[c][r].config(bg='grey77')
        value[c][r] = 30
      elif list[r][c] == 40: 
        button[c][r].config(bg='grey66')
        value[c][r] = 40
      elif list[r][c] == 50:
        button[c][r].config(bg='grey44')  
        value[c][r] = 50
      elif list[r][c] == 60: 
        button[c][r].config(bg='grey33')
        value[c][r] = 60
      elif list[r][c] == 70:
        button[c][r].config(bg='grey22')
        value[c][r] = 70
      else: 
        button[c][r].config(bg='grey1')
        value[c][r] = 90


def savecanvas():  #convert 800x800 to 32x32 grid
  global value, list4 
  list3 = []  #one row only (1x18)
  list4 = []  #final output of 32x32 array that will convert to grid
  for r in range(0, 800, 25):
    list3 = []   #it will be empty once it is done getting the value for list4, will keep repeating 
    for c in range(0 , 800, 25): #will only loop 32times that is 1x18
      getnumber = f0(r, c)    #returning only 1 value
      list3.append(getnumber) #store that 1 value for 32 times
    list4.append(list3)       #row will loop 32 times
  save_draw_colour(list4)
  print(list4)
  

def f0(x, y): #get the starting x, y of a 25x25 and to return 1 value back to rep the 25x25, to scale down a 25x25 to a 1x1
  global list0
  list0 = []  #To store the value of 25x25 to store in 1 array,
  for r in range(x ,25+x):
    for c in range(y ,25+y):
      list0.append(canvasdraw[r][c])
  freq = min(set(list0), key = list0.count) #using min instead cause if max almost everytime will get 0,harder for the draw to show; once the 18x18 grid got 1 value change, then return that value
  return freq  #Returning min value 


def clearbtn():
  allwht()
  for r in range(800):
    for c in range(800):
      canvasdraw[r][c] = 0
  canvas.delete('all')
  print(canvasdraw)

#To navigate to Draw GUI
def drawappear(): 
    guessframe.grid_forget()
    focusframe.grid_forget()
    luckframe.grid_forget()
    mainframe.grid_forget()
    drawingframe.grid(row=1, column=0)

#################### DRAW GUI ####################
drawingframe = Frame(middleframe)

master = ttk.Notebook(drawingframe) #widget that manages a collection of windows/displays

tabgrid = Frame(master) #new frame for tab grid
tabdraw = Frame(master) #new frame for tab draw

#Placement is at the top left corner
master.add(tabgrid,text="Grid")
master.add(tabdraw,text="Draw")
master.grid(row=0, column = 0)

gridframe = Frame(tabgrid, width=800, height=800) #32x32 btn
gridframe.grid(row=0, column=0)

shadeframe = Frame(drawingframe) #shades btn
shadeframe.grid(row=0, column=1)

colourframe = Frame(drawingframe)
colourframe.grid(row=1, column=0) #all white/black btns and send btn 


#Set canvas background colour to white
canvas = Canvas(tabdraw, width=800, height=800, bg='white')  
canvas.grid(row=0, column=0)

canvas.bind('<Button-1>', get_x_and_y)
canvas.bind('<B1-Motion>',paint)
canvas.bind('<Enter>', get_x_and_y)

#This variable to store the colour choice 
colour = 0
canvasdraw = [[0 for r in range(800)] for c in range(800)]  # save eventxy into an array 

# 32x32 grid
button = [[r for r in range(32)] for c in range(32)]
value = [[0 for r in range(32)] for c in range(32)]  #angle

for r in range (32):
  for c in range (32):
    button[r][c] = Button(gridframe, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda x=r, y=c:colour_picker(x, y))
    button[r][c].grid(row=r, column=c)

#shades button
white = Button(shadeframe, text="White", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=lambda m=0:choose_colour(m))
white.grid(row=1, column=0)
grey1 = Button(shadeframe, text="Grey1", font=("Calibri, 10"), bg='grey88', width=13, height=2, command=lambda m=20:choose_colour(m))
grey1.grid(row=2, column=0)
grey2 = Button(shadeframe, text="Grey2", font=("Calibri, 10"), bg='grey77', width=13, height=2, command=lambda m=30:choose_colour(m))
grey2.grid(row=3, column=0)
grey3 = Button(shadeframe, text="Grey3", font=("Calibri, 10"), bg='grey66', width=13, height=2, command=lambda m=40:choose_colour(m))
grey3.grid(row=4, column=0)
grey4 = Button(shadeframe, text="Grey4", font=("Calibri, 10"), bg='grey44', width=13, height=2, command=lambda m=50:choose_colour(m))
grey4.grid(row=5, column=0)
grey5 = Button(shadeframe, text="Grey5", font=("Calibri, 10"), bg='grey33', fg='white', width=13, height=2, command=lambda m=60:choose_colour(m))
grey5.grid(row=6, column=0)
grey6 = Button(shadeframe, text="Grey6", font=("Calibri, 10"), bg='grey11', fg='white', width=13, height=2, command=lambda m=70:choose_colour(m))
grey6.grid(row=7, column=0)
black = Button(shadeframe, text="Black", font=("Calibri, 10"), bg='grey1', fg='white', width=13, height=2, command=lambda m=90:choose_colour(m))
black.grid(row=8, column=0)

#save button
savebtn = Button(shadeframe, text="Save", font=("Calibri, 10"), bg='#ece75f', fg='black', width=13, height=2, command=savecanvas)
savebtn.grid(row=9, column=0)

#colour button
allwhite = Button(colourframe, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(colourframe, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

clear = Button(colourframe, text="Clear",font=("Calibri, 12"), bg='#e6cc00', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=2)

#send btn
send = Button(colourframe, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=3)



#MODE FRAME
#Buttons at the bottom to navigate to the different games
horoscopetitlebtn = Button(modeframe, text="Guess the Horoscope", font=("Courier", 15), width=25, height=2, bg='#CBC3E3', command=guessappear)
horoscopetitlebtn.grid(row=0, column=0)

luckbtn = Button(modeframe, text="What's Your Luck?", font=("Courier", 15), width=25, height=2, bg='#F6D2E0', command=luckappear)
luckbtn.grid(row=0, column=1)

focusbtn = Button(modeframe, text="Test Your Concentration", font=("Courier", 15), width=25, height=2, bg='#C8E7F5', command=focusappear)
focusbtn.grid(row=0, column=2)

drawbtn = Button(modeframe, text="Express Yourself", font=("Courier", 15), width=25, height=2, bg='yellow', command=drawappear)
drawbtn.grid(row=0, column=3)


main.mainloop()






















