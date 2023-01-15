from tkinter import *
from datetime import datetime
import random
import cartoon
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog

counter = 0
running = False

def show_Image(choice):
    global icons
    path2 = "icons/" + str(icons[choice]) + ".png"
    myImage = Image.open(path2)

    #sending to cartoon.py
    #first path refers to input for img
    #path2 refers to variable
    cartoon.pixelised(path = path2)
    myImage = Image.open("cartoon.png")

def click():
    global numberxlist
    numberx = random.randint(0,5) #generate a random no.
    if len(numberxlist) >= 1:
        while numberx == numberxlist[0]:
            numberx = random.randint(0,5)
        else:
            numberxlist[0] = numberx
            print(numberx)
    else:
        numberxlist = [numberx]
        print(numberxlist[0])
    show_Image(numberx) #send to polariser the number

def getname():
    name = simpledialog.askstring("Test", "What's your Name?:")
    return name

def correctbox():
    name = getname()
    messagebox.showinfo("Congrats {}".format(name)+" !","You're 100% focus!")

def wrongbox():
    messagebox.showinfo("Try Again!", "You need to improve on your focus!")

# start function of the stopwatch
def Start(label):
    global running, Lno
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    for i in range (0, 6): 
        btn[i]['state']='normal'
    click()
   
# Stop function of the stopwatch
def Stop(m):
    global running, numberxlist, Lno
    start['state']='disabled'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    print('stop')
    for i in range (0, 6): 
        btn[i]['state']='disabled'
    if m == numberxlist[0]:
        Lno = Lno+1
        if Lno > 3:
            correctbox()
            Lno = 0
    elif m == 10:
        Lno = 0
    else:
        Lno = 0
        wrongbox()
        print('wrong')

# Reset function of the stopwatch
def Reset(label):
    global counter, Lno, icons
    counter=0
   
    # If rest is pressed after pressing stop.
    if running==False:
        start['state']='normal'      
        reset['state']='disabled'
        label['text']='Welcome!'
        level['text']='Level '+ str(Lno)
        if Lno == 1:
            icons = ['Netflix', 'Tiktok', 'Youtube', 'Twitter', 'Instagram', 'Facebook']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        elif Lno == 2:
            icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
        else:
            icons = ['Netflix', 'Tiktok', 'Youtube', 'Twitter', 'Instagram', 'Facebook']
            for i in range (0, 6):
                btn[i]['text']=icons[i]
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'

def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            """ if counter==0:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("00:00:%S")
                display=string """
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

#Define geometry of the window
main.geometry("1000x300")     

numberxlist = []
Lno = 0

#Header for the game
headername = Label(text="ICONcentrate", font=('Arial', 30)) 
headername.grid(row=0, columnspan=4)

#Instructions
instruction = Label(main, text="1. Press on start game etc...", font=('Arial', 15), bg='pink')
instruction.grid(row=1, columnspan=4)

level = Label(main, text='Level '+ str(Lno), font=('Arial', 10))
level.grid(row=2, column=0)

#Timer
timer = Label(main, text='Timer', font=('Arial', 10))
timer.grid(row=2, column=1)

start = Button(main, text='Start', font=('Arial', 10), width=6, command=lambda:Start(timer))
start.grid(row=2, column=2)
stop = Button(main, text='Stop',width=6,state='disabled', command=Stop)
reset = Button(main, text='Reset',width=6, state='disabled', command=lambda:Reset(timer))
reset.grid(row=2, column=3)

#Answer btn
frame1 = Frame(main)
frame1.grid(row=3, columnspan=4)

icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']
btn = [i for i in range(len(icons))]  #defining the number of buttons

for i in range (0, 6):  #Assigning array values into btn 
    btn[i] = Button(frame1, text=icons[i], state='disabled', command=lambda m=i:Stop(m))
    btn[i].grid(row=0, column=i)




main.mainloop()