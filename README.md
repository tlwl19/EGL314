# **Mental Wellness GUI**

The Mental Wellness GUI approaches different ways to improve one's positive state of mind. There are 4 available games which are of different ways where one could approach mental wellness. The games also leverages on electromechanical systems that manipulate polarization to synergize pixelized art forms. 


<br>

![Alt text](markdown%20imgs/mainpageSS.png)
<br>
*Mental Wellness GUI Main Page*

<br>

# **Features**

The Mental Wellness GUI provides the following features:

- <a href="https://github.com/tlwl19/EGL314#guess-the-horoscope">Guess the Horoscope</a>
- <a href="https://github.com/tlwl19/EGL314#whats-your-luck">What's Your Luck?</a>
- <a href="https://github.com/tlwl19/EGL314#iconcentrate">Test Your Concentration</a>
- <a href="https://github.com/tlwl19/EGL314#express-yourself">Express Yourself</a>

Upon clicking on any of the buttons they will be directed to each respective game, where more details will be given.

<br>

# **Getting Started**

## **Hardware** 
1. Single Board Computer: Raspberry Pi 4 Model B
2. Operating System: Raspbian Buster Full

![](markdown%20imgs/RaspberryPi.png)
*Fu YongWei, EGL314, Lecture notes 1*

<br>

## **Software** 
1. PuTTY 
2. VNC Viewer
3. Python

<br>

## **Tutorial**

For more details on installation of your software, refer to the following:
- <a href="https://github.com/tlwl19/finalchallenge#installation">Software Installation steps</a>

<br>

### **GUI Setup**

Firstly, we will need to import the tkinter library.

```
from tkinter import *
```
<br>

Next, we will need to create a main GUI window. Here, we changed the title to 'Mental Wellness'. You can change the title to your preference.
```
main = Tk()
main.title("Mental Wellness")
```

<br>

For the window to stay, we will need to loop it.
```
main.mainloop()
```

<br>

<font size = "3">Output</font>

![Alt text](markdown%20imgs/mentalwellnessSS.png)
<br>
*Main GUI Window*

<br>

---

# **Home Page** 
In the home page, there are 4 navigation buttons that user can use to navigate to each respective games. The 4 games which the user can play are Guess the Horoscope, What's you luck, ICONcentrate and lastly Express yourself.  
<br>

![](Demo%20Pics/Main%20Page.png)
*GUI Main Page*

<br>

---

# **Guess the Horoscope**

Let's begin with the "Guess the Horoscope" game.
<br>
The main objective of this game is to challenge the user's short-term memory skills and determine if the user has good memory by getting 4 correct horoscope guesses.

<br>

## Let's see how to play this game

From the home page, click on the "Guess the Horoscope" button.

![](Demo%20Pics/Select%20Horo.png)
*From Home page navigate to "Guess the Horoscope" page*

<br>

You will be redirected to the "Guess the Horoscope" page.
<br>

![](Demo%20Pics/Horo.png)
*Guess the Horoscope page*

<br>

Click on "Start Game" to begin

![](Demo%20Pics/HoroStart.png)
*Press 'Start Game' to play*

<br>

Once the game has started, all the images of the horosopes on the grid on the left side of the window will disappear, and will only display their respective names.

<br>

Next, click on the Guess button to generate a random Horoscope on the polarizer board.

![](Demo%20Pics/HoroGuess.png)
*Press on 'Guess!!' to send image to polariser board*

<br>

The polarizer board will generate a random horoscope image. You have to guess the horoscope that is shown on the polariser.

--> Insert polariser pic
*Image has been sent over to the polariser*

<br>

For example, if the polariser show Leo, click on the Leo button on the GUI.

![](Demo%20Pics/HoroSelectLeo.png)
*Click on the correct button*

<br>

If you have chosen the correct horocsope, the grid on the left will turn green and you gain a point.

![](Demo%20Pics/HoroCorrect.png)
*Correct answer*

<br>

However, if you have chosen the wrong horoscope, the grid will turn red and you lose a point.

![](Demo%20Pics/HoroWrong.png)
*Wrong answer*

<br>

If you have -3 points, the grid will turn white and the game will end.

![](Demo%20Pics/HoroGameOver.png)
*Game over with -3 points*

<br>

Likewise, if you acheive a score of 4, the grid will turn white, 'YOU WIN' will appear and the game will end.

![](Demo%20Pics/HoroWin.png)
*Win the game with a maximum of 4 points*

<br>

You can click on the Reset Game button to start over

![](Demo%20Pics/HoroReset.png)
*Reset game*

<br>

You can click on the "Fun Ways to Approach MENTAL WELLNESS" navigation button on the top of the window to return to the home page. Or you can click on the bottom navigation button to play other games.

![](Demo%20Pics/HoroBack.png)

*Navigate to home or other games page*

<br>

---

# **What's Your Luck?**

Next, we will proceed on with "What's Your Luck?" game.
<br>
The luck game gives the user a surge of dopamine and it plays a part in controlling the movement a person makes, as well as their emotional response.

<br>

## Let's see how to play this game

From the home page, click on the "What's Your Luck?" button.

![](Demo%20Pics/SelectLuck.png)
*From home page navigate to "What's your luck?" page*

<br>

You will then be redirected to the "What's Your Luck?" page.

![](Demo%20Pics/Luck.png)
*What's Your Luck? page*

<br>

On this page, you can insert your date of birth, and it will generate a random luck percentage on the polarizer. 

![](Demo%20Pics/LuckSelectMonth.png)
*Select your birth month*

<br>

![](Demo%20Pics/LuckSelectDay.png)
*Select your birth date*

<br>

The luck percentages are as follows:
- Genie Lamp
    - 0-25% Luck
- 50% Luck
- 75% Luck
- 99% Luck

<br>

If the polarizer displays genie lamp, you can try again by entering another date of birth.

-->Insert Genie lamp on polariser pic
*Genie lamp shown on polariser*

<br>

However, if the polarizer displays 75% or 99% luck, the game will prompt you to play a game of rock, paper, scissors.

![](Demo%20Pics/LuckGame.png)
*Play rock, paper, scissors*

<br>

Once you have select either rock, paper or scissors, it will be displayed on the preview window.

![](Demo%20Pics/LuckChosen.png)
*Preview of rock, paper, scissors that you have choosen*

<br>

The game will generate rock, paper or scissors on the polariser. That will determine if you win or lose.

--> Insert polariser pic of rock, paper,scissor
*Either rock, paper or scissors will be shown on the polariser*

<br>

The game has ended after playing rock, paper or scissors. You can choose to play again by entering another date of birth or click on the "Fun Ways to Approach MENTAL WELLNESS" navigation button on the top of the window to return to the home page. Or you can click on the bottom navigation button to play other games.

![](Demo%20Pics/LuckBack.png)
*Navigate to home or other games page*

<br>

---

# **ICONcentrate**

ICONcentrate is a game that trains user's call-back memory.It is also built to test your concentration by seeing how fast you can react to guessing common brands that we see in our daily life.

<br>

## Lets see how to play this game

From the home page, click on the "Test Your Concentration" button.

![](Demo%20Pics/SelectIcon.png)
*From home page navigate to "ICONcentrate" page*

<br>

You will then be redirected to the ICONcentrate game page

![](Demo%20Pics/Icon.png)
*ICONcentrate page*

<br>

Click on the instructions button to learn how to play the game.

![](Demo%20Pics/IconInstructions.png)
*Press on 'Instruction' button to read the instructions of the game*

<br>

![](Demo%20Pics/Instructions.png)
*Instructions*

<br>

To start the game, press the start button on the right to begin.

![](Demo%20Pics/IconStart.png)
*Press 'Start' to play the game*

<br>

Once the game has begun, a random brand icon will be displayed on the polarizer board. 

-->Insert polariser pic of random icon
*Random image icon is generated and send to polariser*

<br>

You will have 20 seconds to guess the icon from the selection of choices below. 

![](Demo%20Pics/IconSelect.png)
*Choose the correct icon corresponding to that being shown on the polariser*

<br>

Once 20 seconds has passed, the game will end.

![](Demo%20Pics/IconGameOver.png)
*Time's Up*

<br>

If you guessed the wrong icon, a message box will appear to notify you that you have guessed the wrong brand and the game will end

![](Demo%20Pics/IconWrong.png)         
*Game ended once you guessed wrongly*

<br>

If you guessed a correct icon, you will move on to the next level, and you can click the start button to display the next icon on the polarizer.

![](Demo%20Pics/IconNext.png)
*Next level*

<br>

In order to beat the game, you have to guess the correct icon through 4 levels, with each level progressing with higher difficulty where lesser-known brands are displayed or where some brand icons are harder to distinguish. You only have one attempt.

![](Demo%20Pics/IconLastLv.png)
*Final level*

<br>

Once you have beaten all 4 levels, you will be prompted to enter your name

![](Demo%20Pics/IconName.png)

*Enter your name*

<br>
Once you have entered your name, a messaage box with your name will appear to notify you that you have beaten the game and the time taken to beat the game.

![](Demo%20Pics/IconWin.png)
*Total time taken to complete the game*

<br>

You can click on the "Fun Ways to Approach MENTAL WELLNESS" navigation button on the top of the window to return to the home page. Or you can click on the bottom navigation button to play other games.

![](Demo%20Pics/IconBack.png)
*Navigate to home or other games page*

<br>

---

# **Express Yourself**

The main objective of this game is to help user express their feelings through drawing. As some people may be afraid to voice out their inner thoughts, instead they can draw it out.

<br>

## Let's see how to play this game

From the home page, click on the "Express Yourself" button.

![](Demo%20pics/SelectDraw.png)
*From home page navigate to "Express Yourself" page*

<br>

You will be redirected to the "Express Yourself" page.

![](Demo%20Pics/Draw.png)
*Express Yourself page*

<br>

The game features a grid consisting of 32 x 32 pixels. You can change the colour of each pixel by clicking on the available shades of black on the right. 

![](Demo%20Pics/DrawSelectColour.png)
*Select the colour that you want to use*

<br>

Next, click on the 32 x 32 pixel and change the colour of the grid. You can also select the grid and draw something out.

![](Demo%20Pics/DrawColourGrid.png)
*Click on the respective pixels on the grid to change their respective colours*

<br>

Alternatively, you can also paint the grid by changing to the draw mode located on the top left hand corner of the grid.

![](Demo%20Pics/DrawChange.png)
*Change to draw mode*

<br>

Once you have changed to draw mode, the grid will be changed into a canvas.

![](Demo%20Pics/DrawCanvas.png)
*Draw mode will show canvas*

<br>

You can choose any shades of black that is on the right and begin to draw on the canvas.

![](Demo%20Pics/DrawDrawn.png)
*I am the modern day Picasso*

<br>

Once you are done drawing, you can convert your drawing into a pixelised form on the grid. In order to do that, we will have to save the drawing.

![](Demo%20Pics/DrawSave.png)
*Save drawing on canvas*

<br>

Once you have saved the drawing, it will be pixelised in the grid mode. If you want to see your pixelised drawing, you can change back to the grid form by clicking the grid button on the top left hand corner of the cavnvas.

![](Demo%20Pics/DrawChangeGrid.png)
*Change to grid mode to see pixelised form*

<br>

And voilà! You have successfully converted your drawing into a pixelised form.

![](Demo%20Pics/DrawConvertGrid.png)
*Pixelised form on grid*

<br>

You can send your pixelised drawing to the polariser by clicking on the 'Send Image' button and it will display your pixelised drawing.

![](Demo%20Pics/DrawConvertGridSend.png)
*Click on 'Send Image' to see pixelised form on the polariser*

-->Insert pic on final outcome from the polariser
*Final outcome on the polariser*

<br>

### Additional Features: Express Yourself
<br>

1. All White
<br>

Click on the 'All White' button to turn the entire grid and canvas to white.

![](Demo%20Pics/DrawAllWhite.png)
*Change the grid and canvas to white*

<br>

![](Demo%20Pics/Draw.png)
*All White on grid*

<br>

![](Demo%20Pics/DrawCanvas.png)
*All White on canvas*

<br>

2. All Black
<br>

Turns the entire grid and canvas to black. This can be extremely helpful if you want to draw with lighter shades such as white colour to Grey 3

<br>
Click on the 'All Black' button to turn the entire grid and canvas to black.

![](Demo%20Pics/DrawAllBlack.png)
*Change the grid and canvas to black*

<br>

![](Demo%20Pics/DrawGridAllBlack.png)
*All Black on grid*

<br>

![](Demo%20Pics/DrawCanvasAllBlack.png)
*All Black on canvas*

<br>

If you want to clear your canvas or grid, you can press the clear button.

![](Demo%20Pics/DrawClear.png)
*Clear everything that is drawn either on grid or canvas*

<br>

![](Demo%20Pics/Draw.png)
*Clear everything that is drawn either on grid or canvas*

<br>

---

# **Creating the Overall GUI**

## **Overall frame structure**

<br>

Header frame:
```
topframe = Frame(main)
topframe.grid(row=0, column=0)
```
<br>

Feature frame:
```
middleframe = Frame(main)
middleframe.grid(row=1, column=0)
```
<br>

Footer frame:
```
modeframe = Frame(main)
modeframe.grid(row=2, column=0)
```

<br>

## **Title**
```
headertitle = Button(topframe, text="Fun Ways to Approach MENTAL WELLNESS", font=header_font, fg = '#6495ED', activeforeground='#C3B1E1', command=mainappear, padx=250)
headertitle.grid(row=0, column=0)
```

<br>

## **Creating the main page**

<br>

Main Page Frame:
```
mainframe = Frame(middleframe)
mainframe.grid(row=0, column=0)
```

<br>

Quote & Description:
```
quotevar = "Mental Health.. is not a destination, but a process. It's about how you drive, not where you're going.\n \n-NOAM SHPANCER, PHD"
quote = Label(mainframe, text=quotevar, font=quote_font, bg='#DBDBDB', padx=50 ,pady=50)
quote.grid(row=0, column=0)

descvar = "Mental Wellness is an internal resource that helps us THINK, FEEL, CONNECT, and FUNCTION."
desc = Label(mainframe, text=descvar, font=('Arial', 20), pady=25) 
desc.grid(row=1, column=0)
```

<br>

Image:
```
mentalpath = "wellness/mental.jpg"
myImage = Image.open(mentalpath)
mentalImage = ImageTk.PhotoImage(myImage)
mentalpic = Label(mainframe, image=mentalImage)
mentalpic.grid(row=2, column=0)
```
<br>

---

# **Guess the Horoscope**


## **Creating the Frames**
<br>

Overall frame

```
guessframe = Frame(middleframe)
```

We will need to create the first frame, which is for the 3x4 grid.

```
inguessframe = Frame(guessframe)
inguessframe.grid(row=1, column=0)

imageFrame = Frame(guessframe)
imageFrame.grid(row=0, column=1)

```

Next, we will create the second frame, which is for the GUESS button.

```
inguessframe2 = Frame(guessframe)
inguessframe2.grid(row=1, column=1)

guessbtn = Button(inguessframe2, text="GUESS!!", font=('Arial',20), command=guess)
guessbtn.grid(row=0, column=1)

```

Lastly, we will need to create the third frame, which is for the START button, RESET button, and SCORE.

```
inguessframe3 = Frame(guessframe)
inguessframe3.grid(row=1, column=2)

```

Guess game title

```
headername = Label(guessframe, text="Guess the Horoscope", font=('Arial', 30)) 
headername.grid(row=0, columnspan=3)

```

After the frames have been created, we will start to create the buttons in the 3x4 grid. 

```
inputrow = 6    
inputcolumn = 4

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

```

We will then need to insert the images of the horoscope symbols onto our buttons.

```
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
```

After which, we'll need to create a guess button

```
guessbtn = Button(inguessframe2, text="GUESS!!", font=('Arial',20), command=guess)
guessbtn.grid(row=0, column=1)
```

After which, we'll need to create buttons/labels for start, reset, score and result

```
startbtn = Button(inguessframe3, text="START GAME", font=('Arial', 20), bg='yellow', command=startgame)
startbtn.grid(row=0, column=2)

resetbtn = Button(inguessframe3, text="RESET GAME", font=('Arial', 20), bg='pink', command=restartgame)
resetbtn.grid(row=1, column=2)

scorename = Label(inguessframe3, text="Score", font=('Arial', 25)) 
scorename.grid(row=2, column=2)

scoreresults = Label(inguessframe3, text=str(score), font=('Arial', 20))
scoreresults.grid(row=3, column=2)
```

After which, we'll need to create label for prompt on reset game

```
youwin = Label(inguessframe3, text="Press Reset Game to Reset", font=('Arial', 12))
youwin.grid(row=4, column=2)
```

After which, we'll need to remove the reset prompt at intial boot(appear only when triggered)

```
youwin.grid_forget()
```
<br>

---

<br>

# **What's Your Luck?**

<br>

## **Creating the Frames**

Overall frame

```
guessframe = Frame(middleframe)
```

We will need to create the first frame, which is for the dropdown menus.

```
frame0 = Frame(luckframe)
frame0.grid(row=1, columnspan=3)

```

Next, we will create the second frame, which is for the scissors, paper, stone game.

```
frame1 = Frame(luckframe)
frame1.grid(row=4, column=0)

```

After which, we'll need to remove the game at intial boot(appear only when triggered)

```
frame1.grid_forget()
```

Here, we set the title to 'What's Your Luck?'. You can change the title to your preference.

```
lucktitle = Label(luckframe, text="What's Your Luck?", font=('Arial', 30))
lucktitle.grid(row=0, columnspan=4)
```
## **Creating the Calendar Dropdown Menu**
<br>

We will first need to create an array of the months in a year.

```
options = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
```

We will first need to create an array of the days in a month.

```
optionss = []
d = 32
for x in range (1, d):
    optionss.append(x)
```

Datatype of menu text (??)

```
clicked = StringVar()
clickeds = IntVar()

who = date.today()
whos = options[who.month-1]
clicked.set(whos)  #this refers to month
clickeds.set(who.day) #this refers to date
```

To create the dropdown menu for Month:

```
drop = OptionMenu(frame0, clicked , *options )
drop.grid(row=1, column=0)
drop.config(bg="#ffe4f2", fg="BLACK", activebackground="#e54ed0", activeforeground="WHITE", width=30)
drop["menu"].config(bg="#e54ed0", fg="WHITE", activebackground="#ffe4f2", activeforeground="BLACK")
```

To create the dropdown menu for Date:

```
drops = OptionMenu(frame0, clickeds , *optionss )
drops.grid(row=1, column=1)
drops.config(bg="#9f45b0", fg="WHITE", activebackground="#44008b", activeforeground="WHITE", width=30)
drops["menu"].config(bg="#44008b", fg="WHITE", activebackground="#9f45b0", activeforeground="WHITE")
```

To create an enter button:
```
enterbtn= Button(frame0, text= "Enter", command=change_img,  bg="#00076f", fg="WHITE", width=30)
enterbtn.grid(row=1, column=2)
```
## **Creating instructions and scissors, paper, stone game**
<br>

### *Instructions*
---

We will need to create two label for two instructions:
```
title= Label (luckframe, text="How lucky are you today?", font=('100px'), bg='white', width=30)
title.grid(row=2, columnspan=3)
```
```
label= Label(luckframe, image='', text="Input your date of birth and click on the 'Enter' button.", font=('100px'), bg='white')
label.grid(row=3, columnspan=3)
```

### *Scissors, Paper, Stone Game*
---

We will need to create a prompt to notify users to play: 

```
label2 = Label(frame1, text = "", font='20px')
label2.grid(row=0, columnspan=3)
```
After that, we will create each of the scissors, paper, stone picture on the GUI.

```
paths = os.path.abspath('scissors paper stone pics') +'\\scissors.png'
file = paths.replace('\\','/')
img1= ImageTk.PhotoImage(Image.open(file))

paths = os.path.abspath('scissors paper stone pics') +'\\paper.png'
file = paths.replace('\\','/')
img2= ImageTk.PhotoImage(Image.open(file))

paths = os.path.abspath('scissors paper stone pics') +'\\stone.png'
file = paths.replace('\\','/')
img3= ImageTk.PhotoImage(Image.open(file))
```

Scissors, paper, stonoe button for user to input their choice
```
label3 = Button(frame1, image = img1, command=lambda m=1:game(m))
label3.grid(row=1, column=0)

label4 = Button(frame1, image = img2, command=lambda m=2:game(m))
label4.grid(row=1, column=1)

label5 = Button(frame1, image = img3, command=lambda m=3:game(m))
label5.grid(row=1, column=2)
```

Next, We will create the preview of what the user have choose:

Text:
```
previewtitle = Label(luckframe, text="", font=('Arial', 15))
previewtitle.grid(row=2, column=3)
```
We will need to remove the preview tile from the inital boot(appear when trigger)
```
previewtitle.grid_forget()
```
Image:
```
imageLabel = Label(luckframe, bg = 'white', width = 30, height = 15)
imageLabel.grid(rowspan=2, column=3)
```
We will need to remove the preview image from the inital boot(appear when trigger)
```
imageLabel.grid_forget()
```
Last, we will need to bind the change_img function to main:(link in gp chat, i forgor whats this for)
```
main.bind("<Return>", change_img) 
```
## **Creating the Functions Used**
---
<br>

### *Line 512*

### *Assign functions to*

Use ? statement to create function for ?
```
insert function here
```
output


<br>

---

<br>

# **Test Your Concentration**

**Test Your Concentration** is a game where it challenges the users' ability to focus and select the correct answer within the given time limit. The game is called 'ICONcentrate', in which it has 4 stages, with the difficulty increasing each round. The program will randomly generate icons for each round, prompting the player to guess the correct icon shown on the polarizer panel.

<br>

![](markdown%20imgs/iconSS.png)
*Test Your Concentration GUI*

<br>

---

<br>

## **Code**

<br>

Create the frame first
```
focusframe = Frame(middleframe)
```
focus frame 
```
midframe = Frame(focusframe)
midframe.grid(row=2, columnspan=6)
```
button frame
```
frameone = Frame(focusframe)
frameone.grid(row=3, column=0)
```
Firstly, we set the title to 'ICONcentrate'. You can change the title to your preference.

```
headername = Label(focusframe, text="ICONcentrate", font=('Arial', 30), fg='#96DED1') 
headername.grid(row=0, column=0)
```

Next, we created the **Instructions** button for the game, in which the user would need to click on the button so that a pop-up window would appear and show them the instructions.

```
instrubtn = Button(focusframe, text='Instructions', font=('Arial', 15), bg = '#b0c8ed', fg='white', command=getinstruction)
instrubtn.grid(row=1, column=0)
```

Before creating the buttons, create these variable

```
numberxlist = []
Lno = 0
storetime = 0
```
level button
```
level = Label(midframe, text='Level '+ str(Lno), font=('Arial', 15))
level.grid(row=2, column=0)
```
timer
```
timer = Label(midframe, text='Welcome', font=('Arial', 15))
timer.grid(row=2, column=1, padx=100)
```
start button
```
start = Button(midframe, text='Start', font=('Arial', 15), command=lambda:Start(timer))
start.grid(row=2, column=2, ipadx=30)
```
answer button
```
icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']
btn = [i for i in range(len(icons))] 

for i in range (0, 6):
    btn[i] = Button(frameone, text=icons[i], state='disabled', width=10, height=2, font=("Courier", 15), command=lambda m=i:Stop(m), wraplength=130) #so that texaschicken text can fully show on the button
    btn[i].grid(row=0, column=i)
```
<br>

---
<br>

# **Express Yourself**

![](Demo%20Pics/Draw.png)
*Express Yourself GUI*

---
<br>

## **Creating the Frames**

Overall frame

```
drawingframe = Frame(middleframe)
```

Canvas frame

```
master = ttk.Notebook(drawingframe)
```
Frame for both tabs
```
tabgrid = Frame(master) #new frame for tab grid
tabdraw = Frame(master)
```
Frame for grid button
```
gridframe = Frame(tabgrid, width=800, height=800)
gridframe.grid(row=0, column=0)
```
Frame for shades selection
```
shadeframe = Frame(drawingframe)
shadeframe.grid(row=0, column=1)
```
Frame for color preset n send btn
```
colourframe = Frame(drawingframe)
colourframe.grid(row=1, column=0)
```
Next, tab position:
```
master.add(tabgrid,text="Grid")
master.add(tabdraw,text="Draw")
master.grid(row=0, column = 0)
```
Creating the grid:
```
button = [[r for r in range(32)] for c in range(32)]
value = [[0 for r in range(32)] for c in range(32)]

for r in range (32):
  for c in range (32):
    button[r][c] = Button(gridframe, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda x=r, y=c:colour_picker(x, y))
    button[r][c].grid(row=r, column=c)
```
Shades button:
```
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
```
Save button:
```
savebtn = Button(shadeframe, text="Save", font=("Calibri, 10"), bg='light blue', fg='black', width=13, height=2, command=savecanvas)
savebtn.grid(row=9, column=0)
```
Color selection button:
```
allwhite = Button(colourframe, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(colourframe, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)
```
Clear button:
```
clear = Button(colourframe, text="Clear",font=("Calibri, 12"), bg='gold', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=2)
```
Send button:
```
send = Button(colourframe, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=3)
```
Creating the canvas:
```
canvas = Canvas(tabdraw, width=800, height=800, bg='white')  
canvas.grid(row=0, column=0)
```
Binding the canvas:
```
canvas.bind('<Button-1>', get_x_and_y)
canvas.bind('<B1-Motion>',paint)
canvas.bind('<Enter>', get_x_and_y)
```
Color choice variable:
```
colour = 0
```
Canvas arrray:
```
canvasdraw = [[0 for r in range(800)] for c in range(800)]
```
---
<br>

# **Open file in Raspberry Pi**

In order to view the values from the terminal, you will need to change the directory to the folder of the file. After changing the directory, you will need to enter `python3 filename.py` to print the output.


1. Open the terminal on Raspberry Pi.
2. In the terminal, type the following commands under this format: 

```
cd /Directory
```
<br>

Example:

```
cd /home/pi/Documents/EGL314/
```

<br>

3. Once inside the directory folder of your file, type in the following:

```
python3 main.py
```

<br>

<font size = "3">Output:</font>

<br>

![](Demo%20Pics/Main%20Page.png)
*Output*





