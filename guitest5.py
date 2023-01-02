#Import the required library
from tkinter import*
from datetime import *
from PIL import Image, ImageTk
import os
import random

#Create an instance of tkinter frame
main= Tk()

#Define geometry of the window
main.geometry("1300x750")
#main.title("Gallery")

#Define a Function to change to Image
def change_img():
    testAQs = date(2020, 1, 20)
    testAQe = date(2020, 2, 18)
    testPs = date(2020, 2, 19)
    testPe = date(2020, 3, 20)
    testAs = date(2020, 3, 21)
    testAe = date(2020, 4, 19)
    testTs = date(2020, 4, 20)
    testTe = date(2020, 5, 20)
    testGs = date(2020, 5, 21)
    testGe = date(2020, 6, 20)
    testCNs = date(2020, 6, 21)
    testCNe = date(2020, 7, 22)
    testLOs = date(2020, 7, 23)
    testLOe = date(2020, 8, 22)
    testVs = date(2020, 8, 23)
    testVe = date(2020, 9, 22)
    testLBs = date(2020, 9, 23)
    testLBe = date(2020, 10, 22)
    testSCs = date(2020, 10, 23)
    testSCe = date(2020, 11, 21)
    testSGs = date(2020, 11, 22)
    testSGe = date(2020, 12, 21)
    testCPs = date(2020, 12, 22)
    testCPe = date(2020, 1, 19)
    #test = str(test.strftime('%d/%m'))
    #test2 = datetime.now()
    #test2 = str(test2.strftime('%d/%m'))
    for i in range(len(options)) :
        if options[i] == clicked.get():
            i = i+1
            if i == 2 and clickeds.get() > 29:
                test3 = False   
            elif clickeds.get() > 30:
                if i == 4 or i == 6 or i == 9 or i == 11:
                    test3 = False
                else: 
                    test3 = True
                    test2 = date(2020, i, clickeds.get())
            else:
            #test2 = str(clickeds.get()) + "/" + i
            #test2 = datetime.date(2019, clickeds.get(), i)
                test3 = True
                test2 = date(2020, i, clickeds.get())
            #test2 = date.strftime(str(clickeds.get()), '%d/%m', str(i))
    if test3 == True:
        randomno = random.randint(1, 5)
        if randomno == 1:
            path = os.path.abspath('images') +'\\1.jpg'
            files = path.replace('\\','/')
            #send pic here to servo
            label2.config(text='')
            frame1.grid_forget()
        elif randomno == 2:
            path = os.path.abspath('images') +'\\2.jpg'
            files = path.replace('\\','/')
            #send pic here to servo
            label2.config(text='')
            frame1.grid_forget()
        elif randomno == 3:
            path = os.path.abspath('images') +'\\3.jpg'
            files = path.replace('\\','/')
            #send pic here to servo
            label2.config(text='')
            frame1.grid_forget()
        elif randomno == 4:
            path = os.path.abspath('images') +'\\4.jpg'
            files = path.replace('\\','/')
            label2.config(text='Would you like to play a game with me?')
            frame1.grid(row=3, column=1)
            #send pic here to servo
        else:
            path = os.path.abspath('images') +'\\5.jpg'
            files = path.replace('\\','/')
            label2.config(text='Would you like to play a game with me?')
            frame1.grid(row=3, column=1)
            #send pic here to servo

        """ if test2 >= testGs and test2 <= testGe:
            #label.config(text = clicked.get() + " " + str(clickeds.get()) + " Gemini")
            #label.config(text = "gemini")
            o = "gemini"
            label2.config(text='21 May to 20 June' + str(randomno))
            print(test2)
            print(testGs)
            print(testGs)
        elif test2 >= testTs and test2 <= testTe:
            #label.config(text = "taurus")
            label2.config(text='20 April to 20 May' + str(randomno))
            o = "taurus"
            print(test2)
            print(testTs)
            print(testTe)
        elif test2 >= testAs and test2 <= testAe:
            #label.config(text = "aries")
            label2.config(text='21 March to 21 April' + str(randomno))
            o = "aries"
            print(test2)
            print(testAs)
            print(testAe)
        elif test2 >= testPs and test2 <= testPe:
            #label.config(text = "pisces")
            label2.config(text='19 Febuary to 20 March' + str(randomno))
            o = "pisces"
            print(test2)
            print(testPs)
            print(testPe)
        elif test2 >= testAQs and test2 <= testAQe:
            #label.config(text = "aquarius")
            label2.config(text='20 January to 18 Febuary'+ str(randomno))
            o = "aquarius"
            print(test2)
            print(testAQs)
            print(testAQe)
        elif test2 >= testCNs and test2 <= testCNe:
            #label.config(text = "cancer")
            label2.config(text='21 June to 22 July'+ str(randomno))
            o = "cancer"
            print(test2)
            print(testCNs)
            print(testCNe)
        elif test2 >= testLOs and test2 <= testLOe:
            #label.config(text = "leo")
            label2.config(text='23 July to 22 Augest'+ str(randomno))
            o = "leo"
            print(test2)
            print(testLOs)
            print(testLOe)
        elif test2 >= testVs and test2 <= testVe:
            #label.config(text = "virgo")
            label2.config(text='23 Augest to 22 September'+ str(randomno))
            o = "virgo"
            print(test2)
            print(testVs)
            print(testVe)
        elif test2 >= testLBs and test2 <= testLBe:
            #label.config(text = "libra")
            label2.config(text='23 September to 22 October'+ str(randomno))
            o = "libra"
            print(test2)
            print(testLBs)
            print(testLBe)
        elif test2 >= testSCs and test2 <= testSCe:
            #label.config(text = "scorpio")
            label2.config(text='23 October to 21 November'+ str(randomno))
            o = "scorpio"
            print(test2)
            print(testSCs)
            print(testSCe)
        elif test2 >= testSGs and test2 <= testSGe:
            #label.config(text = "sagittarius")
            label2.config(text='22 November to 21 December'+ str(randomno))
            o = "sagittarius"
            print(test2)
            print(testSGs)
            print(testSGe)
        else:
            #label.config(text = "capricorn")
            label2.config(text='22 December to 19 January'+ str(randomno))
            o = "capricorn"
            print(test2)
            print(testCPs)
            print(testCPe)

        path = os.path.abspath('images') +'\\' + o + '.jpg'
        files = path.replace('\\','/')
        img2=ImageTk.PhotoImage(Image.open(files))
        label.configure(image=img2, width=900, height=500)
        label.image=img2 """
    else:
        label.configure(text = "Please input a valid DoB", image='', font=('50px'))
        label2.config(text='')

def game(no):
    randomx = random.randint(1,3)
    if randomx == 1:
        #send rock pic 
        path = os.path.abspath('images') +'\\rock.jpg'
        files = path.replace('\\','/')
    elif randomx == 2:
        path = os.path.abspath('images') +'\\sci.jpg'
        files = path.replace('\\','/')
        #send sci pic
    else:
        path = os.path.abspath('images') +'\\paper.jpg'
        files = path.replace('\\','/')
        #send paper pic
   
# Dropdown menu options
options = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
optionss = []
d = 32
for x in range (1, d):
    optionss.append(x)

# datatype of menu text
clicked = StringVar()
clickeds = IntVar()

# initial menu text
#clicked.set("January")
#clickeds.set(1)
who = date.today()
whos = options[who.month-1]
clicked.set(whos)
clickeds.set(who.day)

# Create Dropdown menu
drop = OptionMenu(main , clicked , *options )
drop.grid(row=0, column=0, padx=30, pady=55, ipady=15)
drop.config(bg="#ffe4f2", fg="BLACK", height="6" , width="20" , activebackground="#e54ed0", activeforeground="WHITE")
drop["menu"].config(bg="#e54ed0", fg="WHITE", activebackground="#ffe4f2", activeforeground="BLACK")

# Create Dropdown menu
drops = OptionMenu(main , clickeds , *optionss )
drops.grid(row=1, column=0, padx=30, pady=55, ipady=15)
drops.config(bg="#9f45b0", fg="WHITE", height="4" , width="20", activebackground="#44008b", activeforeground="WHITE")
drops["menu"].config(bg="#44008b", fg="WHITE", activebackground="#9f45b0", activeforeground="WHITE")

#paths = change_img()
#Convert To PhotoImage
""" paths = os.path.abspath('images') +'\\' + 'capricorn' + '.jpg'
file = paths.replace('\\','/')
img1= ImageTk.PhotoImage(Image.open(file)) """

#Create a Label widget
label= Label(main, image='', text="Kindly, Input your DoB and Press the 'Enter' button", font=('100px'), bg='white')
label.grid(row=0, column=1)

#Create a Button to handle the update Image event
button= Button(main, text= "Enter", font= ('Helvetica 13 bold'), command= change_img,  bg="#00076f", fg="WHITE")
button.grid(row=1, column=1)

label2 = Label(main, text = " ", font='20px')
label2.grid(row=2, column=1)

frame1 = Frame(main)
frame1.grid(row=3, column=1)
frame1.grid_forget()

label3 = Button(frame1, text = "ROCK", font='20px', command=game(1))
label3.grid(row=0, column=0)

label4 = Button(frame1, text = "SCISSORS", font='20px', command=game(2))
label4.grid(row=0, column=1)

label5 = Button(frame1, text = "PAPER", font='20px', command=game(3))
label5.grid(row=0, column=2)

label6 = Label(frame1, text = "", font='20px')
label6.grid(row=0, column=3)

#result = Label(main , text = "Press Enter", font='30px', bg='black', fg='white')
#result.grid(row=3, column=0, pady=20)
main.bind("<Return>", change_img)
main.mainloop()