from tkinter import *   #import tkinter library

main = Tk()   #Create a main window
main.title("Guess the Horoscope") #Title will be shown on the GUI window

#First frame is created for the 3x4 grid
frame1 = Frame(main)
frame1.grid(row=0, column=0)

#Second frame is created for the button "GUESS!"
frame2 = Frame(main)
frame2.grid(row=0, column=1)

#Third frame is created for the 'START/RESET/SCORE' 
frame3 = Frame(main)
frame3.grid(row=0, column=2)

inputrow = 3
inputcolumn = 4

button = [[r for r in range(inputrow)] for c in range(inputcolumn)]
for r in range(inputrow):
    for c in range(inputcolumn):
        button[r][r] = Button(frame1, text="Gemini", font=('Arial',5))
        button[r][r].grid(row=r, column=c)

main.mainloop()  #for the window to stay