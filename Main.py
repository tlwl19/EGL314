from tkinter import *   #import tkinter library
import os 
from PIL import Image, ImageTk, ImageOps
import cartoon
import random
from datetime import *
from datetime import datetime
from tkinter import messagebox, simpledialog

#Mode function
def luckappear(): 
    guessframe.grid_forget()
    focusframe.grid_forget()
    luckframe.grid(row=0, column=0)


def guessappear():
    luckframe.grid_forget()
    focusframe.grid_forget()
    guessframe.grid(row=0, column=0)


def focusappear():
    luckframe.grid_forget()
    guessframe.grid_forget()
    focusframe.grid(row=0, column=0)


################## LUCK FUNCTION ###################
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


################## GUESS FUNCTION ######################
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
    global score, prevent, number, prevent2
    #score = 0
    prevent = []
    prevent2 = 0
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
    #score = 0
    prevent = []
    prevent2 = 0
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
    global number, prevent, numberx, numberxlist, prevent2
    youwin.grid_forget()
    prevent = []  
    #number = list(range(0,11))
                        #green                          #red                            #blue
    if btn0.cget('bg') == '#7fff00' or btn0.cget('bg') == '#FF0800' or btn0.cget('bg') == '#b0c8ed':
        if btn0.cget('bg') != '#FF0800': #red color
            if prevent2 == 0:
                numberx = random.randint(0,11) #generate a random no.
                if len(numberxlist) >= 1:
                    while numberx in numberxlist:
                        numberx = random.randint(0,11)
                    else:
                        numberxlist.append(numberx)
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
                prevent2 = 1
                print(prevent2)
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
    global number, score, prevent, numberx, prevent2
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
                prevent2 = 0
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


################### FOCUS FUNCTION #################
counter = 0   #Time starts from 0
running = False  #Timer is not running

def show_Image(choice):
    global icons
    path2 = "icons/" + str(icons[choice]) + ".png"
    myImage = Image.open(path2)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoon.pixelised(path = path2)
    myImage = Image.open("cartoon.png")

def getinstruction():
    messagebox.showinfo("Instructions", "1. Press on 'START' button to begin the game.\n2. Select the correct button corresponding to the image shown on the polariser.\n3. You will proceed on to the next level if you choose the correct button\n4. Game will reset if you choose wrongly")



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
    show_Image(numberx) #send to polariser the number

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
            icons = ['KFC', 'Jollibee', 'McDonalds', 'Pizza Hut', 'Mos Burger', 'Texas \nChicken']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 2:
            icons = ['Puma', 'A&W', 'Fila', 'BMW', 'Subway', 'Ferrari']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 3:
            icons = ['Hawkeye', 'Hulk', 'Nissan', 'Rolls Royce', 'Burger King', 'Dominos']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        else:
            icons = ['Netflix', 'Tiktok', 'Youtube', 'Twitter', 'Instagram', 'Facebook']  #Level 0
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

main = Tk()
main.title("Main Page")

#Mode FRAME
topframe = Frame(main) #header
topframe.grid(row=0, column=0)
middleframe = Frame(main) #feature
middleframe.grid(row=1, column=0, padx=20, pady=20)
modeframe = Frame(main) #mode
modeframe.grid(row=2, column=0)

header = Label(topframe, text="Fun Ways to approach WELLNESS", font=("Arial", 30), padx=325)
header.grid(row=0, column=0)

descvar = ""
desc = Label(middleframe, text="What is Wellness?", font=('Arial', 20), border=50) 
desc.grid(row=0, column=0)

horoscopebtn = Button(modeframe, text="Guess the Horoscope", font=("Courier", 15), width=25, height=2, bg='#b0c8ed', command=guessappear)
horoscopebtn.grid(row=0, column=0)

luckbtn = Button(modeframe, text="What's Your Luck?", font=("Courier", 15), width=25, height=2, bg='pink', command=luckappear)
luckbtn.grid(row=0, column=1)

focusbtn = Button(modeframe, text="Test your concentration", font=("Courier", 15), width=25, height=2, bg='pink', command=focusappear)
focusbtn.grid(row=0, column=2)

################## LUCK #######################
luckframe = Frame(middleframe)

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

#Header
lucktitle = Label(luckframe, text="How is your luck?", font=('Arial', 30))
lucktitle.grid(row=0, columnspan=4)

#This is for dropdown button
frame0 = Frame(luckframe)
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

#Create a Button to handle the update Image event
button= Button(frame0, text= "Enter", command=change_img,  bg="#00076f", fg="WHITE", width=30)
button.grid(row=1, column=2)

#Text
title= Label (luckframe, text="What's your luck today?", font=('100px'), bg='white', width=30)
title.grid(row=2, columnspan=3)


#Create a Label widget
label= Label(luckframe, image='', text="Kindly, Input your DoB and Press the 'Enter' button", font=('100px'), bg='white')
label.grid(row=3, columnspan=3)


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
imageLabel.grid(rowspan=2, column=3)
imageLabel.grid_forget()

main.bind("<Return>", change_img) 



################## GUESS #######################
guessframe = Frame(middleframe)

#Header for the game
headername = Label(guessframe, text="Guess the Horoscope", font=('Arial', 30)) 
headername.grid(row=0, columnspan=3)

#Variable Declaration
score = 0
number = 15
numberxlist = []
prevent = [0]
prevent2 = 0

#First frame is created for the 3x4 grid
framehoro = Frame(guessframe)
framehoro.grid(row=1, column=0)

imageFrame = Frame(guessframe)
imageFrame.grid(row=0, column=1)

inputrow = 6    #indicate the number of rows
inputcolumn = 4 #indicate the number of cols

for r in range(inputrow):
    for c in range(inputcolumn):
        # Button Section
        btn0 = Button(framehoro, text = "Aquarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=0:button(m))
        lbl0 = Label(framehoro, text="Aquarius", font=("Arial", 15), fg='black')
        btn1 = Button(framehoro, text = "Aries", font = ("Arial", 15), height=5, width=10, bg='white', fg='black', command=lambda m=1:button(m))
        lbl1 = Label(framehoro, text="Aries", font=("Arial", 15), fg='black')
        btn2 = Button(framehoro, text = "Cancer", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=2:button(m))
        lbl2 = Label(framehoro, text="Cancer", font=("Arial", 15), fg='black')
        btn3 = Button(framehoro, text = "Capricorn", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=3:button(m))
        lbl3 = Label(framehoro, text="Capricorn", font=("Arial", 15), fg='black')
        btn4 = Button(framehoro, text = "Gemini", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=4:button(m))
        lbl4 = Label(framehoro, text="Gemini", font=("Arial", 15), fg='black')
        btn5 = Button(framehoro, text = "Leo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=5:button(m))
        lbl5 = Label(framehoro, text="Leo", font=("Arial", 15), fg='black')
        btn6 = Button(framehoro, text = "Libra", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=6:button(m))
        lbl6 = Label(framehoro, text="Libra", font=("Arial", 15), fg='black')
        btn7 = Button(framehoro, text = "Pisces", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=7:button(m))
        lbl7 = Label(framehoro, text="Pisces", font=("Arial", 15),fg='black')
        btn8 = Button(framehoro, text = "Sagittarius", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=8:button(m))
        lbl8 = Label(framehoro, text="Sagittarius", font=("Arial", 15), fg='black')
        btn9 = Button(framehoro, text = "Scorpio", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=9:button(m))
        lbl9 = Label(framehoro, text="Scorpio", font=("Arial", 15), fg='black')
        btn10 = Button(framehoro, text = "Taurus", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=10:button(m))
        lbl10 = Label(framehoro, text="Taurus", font=("Arial", 15), fg='black')
        btn11 = Button(framehoro, text = "Virgo", font = ("Arial", 15), height=5, width=10, bg='white', fg='black',command=lambda m=11:button(m))
        lbl11 = Label(framehoro, text="Virgo", font=("Arial", 15), fg='black')

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

#Second frame is created for the button "GUESS!"
frame2 = Frame(guessframe)
frame2.grid(row=1, column=1)

guessbtn = Button(frame2, text="GUESS!!", font=('Arial',20), command=guess)
guessbtn.grid(row=0, column=1)


#Third frame is created for the 'START/RESET/SCORE' 
frame3 = Frame(guessframe)
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


#################### FOCUS GUI ####################
focusframe = Frame(middleframe)

numberxlist = []
Lno = 0
storetime = 0

#Header for the game
headername = Label(focusframe, text="ICONcentrate", font=('Arial', 30), fg='#96DED1') 
headername.grid(row=0, column=0)

#Instructions
instrubtn = Button(focusframe, text='Instruction', font=('Arial', 15), bg = '#b0c8ed', fg='white', command=getinstruction)
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
    btn[i] = Button(frameone, text=icons[i], state='disabled', width=10, height=2, font=("Courier", 15), command=lambda m=i:Stop(m))
    btn[i].grid(row=0, column=i)

main.mainloop()