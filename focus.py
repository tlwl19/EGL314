from tkinter import *

from datetime import datetime

counter = 66000
running = False
def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==66000:            
                display="Starting..."
            else:
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
   
    # Triggering the start of the counter.
    count() 

# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
   
    # If rest is pressed after pressing stop.
    if running==False:      
        reset['state']='disabled'
        label['text']='Welcome!'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'
   

main = Tk()

#Define geometry of the window
main.geometry("1000x300")     

#Header for the game
headername = Label(text="ICONcentrate", font=('Arial', 30)) 
headername.grid(row=0, columnspan=3)

#Instructions
instruction = Label(main, text="1. Press on start game etc...", font=('Arial', 15), bg='pink')
instruction.grid(row=1, columnspan=4)

#Timer
timer = Label(main, text='Timer', font=('Arial', 10))
timer.grid(row=2, column=1)

start = Button(main, text='Start', font=('Arial', 10), width=6, command=lambda:Start(timer))
start.grid(row=2, column=2)
stop = Button(main, text='Stop',width=6,state='disabled', command=Stop)
reset = Button(main, text='Reset',width=6, state='disabled', command=lambda:Reset(timer))

#Answer btn
frame1 = Frame(main)
frame1.grid(row=3, columnspan=4)

icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']
btn = [i for i in range(len(icons))]  #defining the number of buttons

for i in range (0, 6):  #Assigning array values into btn 
    btn[i] = Button(frame1, text=icons[i])
    btn[i].grid(row=0, column=i)







main.mainloop()