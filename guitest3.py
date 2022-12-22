from tkinter import *
from tkcalendar import Calendar
from datetime import *
from PIL import Image, ImageTk
import os

global img, o
#global label, files, bg, bgs
def import_photo():
    global o, img
    #global label, files, bg, myImage
    print("Importing Photo...")

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
        if test2 >= testGs and test2 <= testGe:
            #label.config(text = clicked.get() + " " + str(clickeds.get()) + " Gemini")
            label.config(text = "gemini")
            o = "gemini"
            print(test2)
            print(testGs)
            print(testGs)
        elif test2 >= testTs and test2 <= testTe:
            label.config(text = "taurus")
            o = "taurus"
            print(test2)
            print(testTs)
            print(testTe)
        elif test2 >= testAs and test2 <= testAe:
            label.config(text = "aries")
            o = "aries"
            print(test2)
            print(testAs)
            print(testAe)
        elif test2 >= testPs and test2 <= testPe:
            label.config(text = "pisces")
            o = "pisces"
            print(test2)
            print(testPs)
            print(testPe)
        elif test2 >= testAQs and test2 <= testAQe:
            label.config(text = "aquarius")
            o = "aquarius"
            print(test2)
            print(testAQs)
            print(testAQe)
        elif test2 >= testCNs and test2 <= testCNe:
            label.config(text = "cancer")
            o = "cancer"
            print(test2)
            print(testCNs)
            print(testCNe)
        elif test2 >= testLOs and test2 <= testLOe:
            label.config(text = "leo")
            o = "leo"
            print(test2)
            print(testLOs)
            print(testLOe)
        elif test2 >= testVs and test2 <= testVe:
            label.config(text = "virgo")
            o = "virgo"
            print(test2)
            print(testVs)
            print(testVe)
        elif test2 >= testLBs and test2 <= testLBe:
            label.config(text = "libra")
            o = "libra"
            print(test2)
            print(testLBs)
            print(testLBe)
        elif test2 >= testSCs and test2 <= testSCe:
            label.config(text = "scorpio")
            o = "scorpio"
            print(test2)
            print(testSCs)
            print(testSCe)
        elif test2 >= testSGs and test2 <= testSGe:
            label.config(text = "sagittarius")
            o = "sagittarius"
            print(test2)
            print(testSGs)
            print(testSGe)
        else:
            label.config(text = "capricorn")
            o = "capricorn"
            print(test2)
            print(testCPs)
            print(testCPe)
        choice = label.cget("text")
        print(choice)

        path = os.path.abspath('images') +'\\' + choice + '.jpg'
        files = path.replace('\\','/')
        print("file path is {}".format(files))
        ##image1 = Image.open(files)
        ##test = PhotoImage(image1)
        ##label1.config(image=test)
        #bgs = PhotoImage(files)
        #bg = label1.config(image = str(files))
        return files
        myImage = Image.open(files)
        myImage.show()
    else:
        label.config(text = "Please input a valid DoB")

# Main GUI Windows
main = Tk()
main.title('Tutorial 3 Sample')
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
  
main.geometry("1100x450")

""" #label1 = Label(main, image = "")
label1 = Label(image="")
label1.place(x = 0, y = 0) """

# Create Dropdown menu
drop = OptionMenu(main , clicked , *options )
drop.grid(row=0, column=0)
drop.config(bg="#ffe4f2", fg="BLACK", height="6" , width="20" , activebackground="#e54ed0", activeforeground="WHITE")
drop["menu"].config(bg="#e54ed0", fg="WHITE", activebackground="#ffe4f2", activeforeground="BLACK")

# Create Dropdown menu
drops = OptionMenu(main , clickeds , *optionss )
drops.grid(row=1, column=0)
drops.config(bg="#9f45b0", fg="WHITE", height="4" , width="20", activebackground="#44008b", activeforeground="WHITE")
drops["menu"].config(bg="#44008b", fg="WHITE", activebackground="#9f45b0", activeforeground="WHITE")

# Create button, it will change label text
button = Button(main , text = "Enter" , command = import_photo , bg="#00076f", fg="WHITE", height="2" , width="20",  activebackground="WHITE", activeforeground="BLACK")
button.grid(row=2, column=0)

# Create Label
label = Label(main , text = "")
label.grid(row=3, column=0)

path = import_photo()
print(path)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(path))

# Create a Label Widget to display the text or Image
photo = Label(main, image = img)
photo.grid(row=0, column=1, rowspan=4)

""" # Add Calendar
cal = Calendar(main, selectmode = 'day', month = 5, day = 22)
 
cal.pack(pady = 20)
 
def grad_date():
    test = cal.get_date()
    if (test > '05/21' and test < '06/21') :
        date.config(text = cal.get_date() + ' is gemini ')
        date.config(text = test)
    else:
        date.config(text = cal.get_date() + ' is others ')
        date.config(text = test)
 
# Add Button and Label
Button(main, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(main, text = "")
date.pack(pady = 20) """


main.mainloop()