from tkinter import *
from datetime import datetime
import random
import cartoon
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

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
        #ADD IN ANOTHER MSGBOX TO SHOW TIMER IS UP
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
            icons = ['KFC', 'Jollibee', 'Macs', 'Pizza Hut', 'Mos Burger', 'Texas']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 2:
            icons = ['Puma', 'A&W', '', '', '', '']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 3:
            icons = ['Hawkeye', 'Hulk', 'Subway', 'Rolls Royce', '', '']
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
            if counter > 10:
                Stop(10)
           
    # Triggering the start of the counter.
    count()

main = Tk()
main.title('ICONCENTRATE')

#Define geometry of the window
#main.geometry("1000x300")     

numberxlist = []
Lno = 0
storetime = 0

#Header for the game
headername = Label(text="ICONcentrate", font=('Arial', 30), fg='#96DED1') 
headername.grid(row=0, column=0)

#Instructions
instrubtn = Button(main, text='Instruction', font=('Arial', 15), bg = '#b0c8ed', fg='white', command=getinstruction)
instrubtn.grid(row=1, column=0)

middleframe = Frame(main)
middleframe.grid(row=2, columnspan=6)

#Level
level = Label(middleframe, text='Level '+ str(Lno), font=('Arial', 15), justify=S)
level.grid(row=0, column=0)

#Timer
timer = Label(middleframe, text='Welcome', font=('Arial', 15))
timer.grid(row=0, column=1)

start = Button(middleframe, text='Start', font=('Arial', 15), command=lambda:Start(timer))
start.grid(row=0, column=2, ipadx=50)


#Answer btn
frame1 = Frame(main)
frame1.grid(row=3, column=0)

icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']  #Level 0
btn = [i for i in range(len(icons))]  #defining the number of buttons

for i in range (0, 6):  #Assigning array values into btn 
    btn[i] = Button(frame1, text=icons[i], state='disabled', width=10, height=2, font=("Courier", 15), command=lambda m=i:Stop(m))
    btn[i].grid(row=0, column=i)


main.mainloop()