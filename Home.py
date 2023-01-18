from tkinter import *
import os

main = Tk()
main.title("Welcome")
main.geometry('500x400')

def run_programhoro():
    os.system('python3 luck.py')

btn = Button(main, text="Horoscope", font = ("Arial", 15), width=10, height=5, bg='white', fg='black', command=run_programhoro)
btn.pack()

main.mainloop()