from tkinter import *
from PIL import Image, ImageTk

def button(m):
    global choice
    choice = m
    print("Choice is", choice)
    show_Image(choice)

def show_Image(choice):
    global imageLabel

    path = "img/" + str(choice) + ".png"
    myImage = Image.open(path)
    myImage = myImage.resize((250, 250))
    loadImage = ImageTk.PhotoImage(myImage)
    imageLabel.image = loadImage
    imageLabel.config(image = loadImage, width = 250, height = 250)


main = Tk()

# Variable Declaration
choice = 0

# Frame Sectbion
buttonFrame = Frame(main)
imageFrame = Frame(main)

buttonFrame.grid(row=0, column=0)
imageFrame.grid(row=0, column=1)

# Button Section
btn0 = Button(buttonFrame, text = "Aquarius", font = ("Arial", 15), command=lambda m=0:button(m))
btn1 = Button(buttonFrame, text = "Aries", font = ("Arial", 15), command=lambda m=1:button(m))
btn2 = Button(buttonFrame, text = "Cancer", font = ("Arial", 15), command=lambda m=2:button(m))
btn3 = Button(buttonFrame, text = "Capricorn", font = ("Arial", 15), command=lambda m=3:button(m))
btn4 = Button(buttonFrame, text = "Gemini", font = ("Arial", 15), command=lambda m=4:button(m))
btn5 = Button(buttonFrame, text = "Leo", font = ("Arial", 15), command=lambda m=5:button(m))
btn6 = Button(buttonFrame, text = "Libra", font = ("Arial", 15), command=lambda m=6:button(m))
btn7 = Button(buttonFrame, text = "Pisces", font = ("Arial", 15), command=lambda m=7:button(m))
btn8 = Button(buttonFrame, text = "Sagittarius", font = ("Arial", 15), command=lambda m=8:button(m))
btn9 = Button(buttonFrame, text = "Scorpio", font = ("Arial", 15), command=lambda m=9:button(m))
btn10 = Button(buttonFrame, text = "Tarus", font = ("Arial", 15), command=lambda m=10:button(m))
btn11 = Button(buttonFrame, text = "Virgo", font = ("Arial", 15), command=lambda m=11:button(m))

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=1, column=3)
btn8.grid(row=2, column=0)
btn9.grid(row=2, column=1)
btn10.grid(row=2, column=2)
btn11.grid(row=2, column=3)

# Image Window
imageLabel = Label(imageFrame, bg = 'white', width = 30, height = 15)
imageLabel.grid(row=0, column=0)
imagePixel = Label (imageFrame, bg = 'grey', width = 30, height = 15)
imagePixel.grid(row=0, column=1)

main.mainloop()