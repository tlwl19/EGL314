from tkinter import *
import time

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
    
            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)
    
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1

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
timer = Label(main, text="timer", font=('Arial', 10))
timer.grid(row=2, column=1)

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")
  
# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=20)
  
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)


#Start Game
startbtn = Button(main, text="Start Game", font=('Arial', 10))
startbtn.grid(row=2, column=2)

#Answer btn
frame1 = Frame(main)
frame1.grid(row=3, columnspan=4)

icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']
btn = [i for i in range(len(icons))]  #defining the number of buttons

for i in range (0, 6):  #Assigning array values into btn 
    btn[i] = Button(frame1, text=icons[i])
    btn[i].grid(row=0, column=i)







main.mainloop()