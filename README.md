# **Mental Wellness GUI**

The Mental Wellness GUI approaches different ways to improve one's positive state of mind. There are 4 available games which are of different ways where one could approach mental wellness. The games also leverages on electromechanical systems that manipulate polarization to synergize pixelized art forms. 


<br>

![Alt text](markdown%20imgs/Main%20Page.png)
<br>
*Mental Wellness GUI Main Page*

<br>

# **Features**

The Mental Wellness GUI provides the following features:

- <a href="https://github.com/tlwl19/EGL314#guess-the-horoscope">Guess the Horoscope</a>
- <a href="https://github.com/tlwl19/EGL314#whats-your-luck">What's Your Luck?</a>
- <a href="https://github.com/tlwl19/EGL314#whats-your-luck">Test Your Concentration</a>

Upon clicking on any of the buttons they will be directed to each respective game, where more details will be given.

<br>

---

<br>

# **Getting Started**

## **Hardware** 
1. Single Board Computer: Raspberry Pi 4 Model B
2. Operating System: Raspbian Buster Full

![](markdown%20imgs/RaspberryPi.png)
<br>
*Fu YongWei, EGL314, Lecture notes 1*

<br>

## **Software** 
1. PuTTY 
2. VNC Viewer
3. Python

<br>

---
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

Next, we will need to create a main GUI window. Here, we changed the title to 'Mental Wellness'. You can change the title to your preference.
```
main = Tk()
main.title("Mental Wellness")
```

For the window to stay, we will need to loop it.
```
main.mainloop()
```

<font size = "3">Output</font>

![Alt text](markdown%20imgs/mentalwellnessSS.png)
<br>
*Main GUI Window*

<br>

---

# **Guess the Horoscope**

Let's begin with the "Guess the Horoscope" game.
<br>
The main objective of this game is to challenge the user's sbort-term memory skills and determine if the user has good memory by getting 4 correct horoscope guesses.

<br>

![](Demo%20Pics/Main%20Page.png)
*GUI Main Page*

<br>

## Let's see how to play this game.

From the main page, click on the "Guess the Horoscope" button.

![](Demo%20Pics/Select%20Horo.png)
*Navigate to Guess the Horoscope*

You will be redirected to the "Guess the Horoscope" page.
<br>

![](Demo%20Pics/Horo.png)
*Guess the Horoscope*

Click on "Start Game" to begin

![](Demo%20Pics/HoroStart.png)

Once the game has started, all the images of the horosopes on the grid on the left side of the window will disappear, and will only display their respective names.

Next, click on the Guess button to generate a random Horoscope on the polarizer board.

![](Demo%20Pics/HoroGuess.png)

The polarizer board will generate a random horoscope image. If you are having a hard time figuring out the horoscsope image, you can click on the guess button again to generate a different horoscope image on the polarizer board.

If you have chosen the correct horocsope, the grid on the left will turn green and you gain a point.

![](Demo%20Pics/HoroCorrect.png)

However, if you have chosen the wrong horoscope, the grid will turn red and you lose a point.

![](Demo%20Pics/HoroWrong.png)

If you have -3 points, the grid will turn white and the game will end.

![](Demo%20Pics/HoroGameOver.png)

You can click on the Reset Game button to start over

Likewise, if you acheive a score of 4, the grid will turn white and the game will end.

You can click on the big "Fun Ways to Approach MENTAL WELLNESS" button on the top of the window to return to the main page.

![](Demo%20Pics/HoroBack.png)

<br>

## What's Your Luck?
---

Next, we will proceed with the "What's Your Luck?" game.

From the main page, click on the "What's Your Luck?" button.

![](Demo%20Pics/SelectLuck.png)

You will then be redirected to the "What's Your Luck?" page.

![](Demo%20Pics/Luck.png)
*What's Your Luck?*

On this page, you can insert your date of birth, and it will generate a random luck percentage on the polarizer. 

The luck percentages are as follows:
- Genie Lamp
    - 0-25% Luck
- 50% Luck
- 75% Luck
- 99% Luck

If the polarizer displays 75% or 99% luck, the game will prompt you to play a game of rock, paper, scissors.

![](Demo%20Pics/LuckGame.png)

Depending on your luck percentage, you may have a higer or lower chance of winning the game.

Once you have made your choice, it will be displayed on the window while the game will display its choice at the polarizer board.

![](Demo%20Pics/LuckChosen.png)

You can reset by entering another date of birth.
<br>

As always, you can return to the main page by clicking on the big "Fun Ways to Approach MENTAL WELLNESS" button on the top of the window.
<br>

## ICONcentrate
---
Lastly, we will see how to play ICONcentrate, a game built to test your concentration by seeing how fast you can react to guessing common brands of everything under the sun.

To begin, let's open the ICONcentrate game by clicking on the "Test Your Concentration" button from the main page.

![](Demo%20Pics/SelectIcon.png)

You will then be redirected to the ICONcentrate game page

![](Demo%20Pics/Icon.png)
*ICONcentrate*

Click on the instructions button to learn how to play the game.

![](Demo%20Pics/Instructions.png)

To start the game, press the start button on the right to begin.

![](Demo%20Pics/IconStart.png)

Once the game has begun, a random brand icon will be displayed on the polarizer board. You will have 20 seconds to guess the icon from the selection of choices below. Once 20 seconds has passed, the game will end.

![](Demo%20Pics/IconGameOver.png)

If you guessed a wrong icon, a message box will appear to notify you that you have guessed the wrong brand and the game will end

![](Demo%20Pics/IconWrong.png)

If you guessed a correct icon, you will move on to the next level, and you can click the start button to display the next icon on the polarizer.

In order to beat the game, you have to guess the correct icon through 4 levels, with each level progressing with higher diffuulty where lesser-known brands are displayed or where some brand icons are harder to distinguish. You only have one attempt.

Once you have beaten all 4 levels, you will be prompted to enter your name

![](Demo%20Pics/IconName.png)
<br>
Once you have entered your name, a messaage box with your name will appear to notify you that you have beaten the game and the time taken to beat the game.

![](Demo%20Pics/IconWin.png)

<br>
Remember, you can always return to the main page by clicking on the big "Fun Ways to Approach MENTAL WELLNESS" button on the top of the window.

---
<br>

# **Creating the Frames**

<br>

---



<br>

# **Guess the Horoscope**

**Guess the Horoscope** is a game where it challenges the users' memorising skills, and determines if the user has good memory or not.

![Alt text](markdown%20imgs/horoscopeSS.png)

<br>

*Guess the Horoscope GUI*

<br>

---

<br>

## **Creating the Frames**
<br>

We will need to create the first frame, which is for the 3x4 grid.

```
inguessframe = Frame(guessframe)
inguessframe.grid(row=1, column=0)

imageFrame = Frame(guessframe)
imageFrame.grid(row=0, column=1)

inputrow = 6    
inputcolumn = 4

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

startbtn = Button(inguessframe3, text="START GAME", font=('Arial', 20), bg='yellow', command=startgame)
startbtn.grid(row=0, column=2)

resetbtn = Button(inguessframe3, text="RESET GAME", font=('Arial', 20), bg='pink', command=restartgame)
resetbtn.grid(row=1, column=2)

scorename = Label(inguessframe3, text="Score", font=('Arial', 25)) 
scorename.grid(row=2, column=2)

scoreresults = Label(inguessframe3, text=str(score), font=('Arial', 20))
scoreresults.grid(row=3, column=2)

youwin = Label(inguessframe3, text="Press Reset Game to Reset", font=('Arial', 12))
youwin.grid(row=4, column=2)
youwin.grid_forget()

```

After the frames have been created, we will start to create the buttons in the 3x4 grid. 

```
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

<br>

---

<br>

# **What's Your Luck?**

**What's Your Luck?** is a game where it .......

![Alt text](markdown%20imgs/luckSS.png)

*What's Your Luck? GUI*

## **Creating the Calendar Dropdown Menu**
<br>

We will first need to create an array of the months in a year.

```
options = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
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

Here, we set the title to 'What's Your Luck?'. You can change the title to your preference.

```
lucktitle = Label(luckframe, text="What's Your Luck?", font=('Arial', 30))
lucktitle.grid(row=0, columnspan=4)
```

To create the calendar dropdown buttons:

```
frame0 = Frame(luckframe)
frame0.grid(row=1, columnspan=3)
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










<br>

---

<br>

# **Test Your Concentration**

**Test Your Concentration** is a game where it challenges the users' ability to focus and select the correct answer within the given time limit. The game is called 'ICONcentrate', in which it has 4 stages, with the difficulty increasing each round. The program will randomly generate icons for each round, prompting the player to guess the correct icon shown on the polarizer panel.

![Alt text](markdown%20imgs/iconSS.png)

<br>

*Test Your Concentration GUI*

<br>

---

<br>

## **Code**

<br>

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





<br>

---

<br>

In order to view the values from the terminal, you will need to change the directory to the folder of the file. After changing the directory, you will need to enter `python3 filename.py` to print the output.


1. Open the terminal on Raspberry Pi.
2. In the terminal, type the following commands under this format: 
```
cd /Directory
```

Example:

```
cd /home/pi/Documents/EGL314/
```
3. Once inside the directory folder of your file, type in the following:

```
python3 main.py
```

<font size = "4">Output</font>

![](images/sendimage_outcome.png)
<br>


*The values printed are based on the sequence pattern.*





