from tkinter import *

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

#Start Game
startbtn = Button(main, text="Start Game", font=('Arial', 10))
startbtn.grid(row=2, column=2)

#Answer btn
frame1 = Frame(main)
frame1.grid(row=3, columnspan=4)

icons = ['Facebook', 'Instagram', 'Twitter', 'Youtube', 'Tiktok', 'Netflix']
btn = [i for i in range(6)]  #defining the number of buttons

for i in range (1, 6):  #Assigning array values into btn 
    btn[i] = Button(frame1, text=icons[i])
    btn[i].grid(row=0, column=i-1)







main.mainloop()