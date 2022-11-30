from tkinter import *
from tkcalendar import Calendar
from datetime import *
from PIL import Image
import os

def import_photo():
    global var
    print("Importing Photo...")
    
    choice = var.get()

    # if user did not input any text
    if len(choice) == 0:
        path = os.path.abspath('images') + '\\' + 'cat.png'
        file = path.replace('\\','/')
        myImage = Image.open(file)
        myImage.show()
    # if user input ball, cat or dog
    else:
        path = os.path.abspath('images') +'\\' + var.get() + '.png'
        file = path.replace('\\','/')
        print("file path is {}".format(file))
        myImage = Image.open(file)
        myImage.show()


# Main GUI Windows
main = Tk()
main.title('Tutorial 3 Sample')

# Change the label text
def show():
    testAQs = date(2019, 1, 20)
    testAQe = date(2019, 2, 18)
    testPs = date(2019, 2, 19)
    testPe = date(2019, 3, 20)
    testAs = date(2019, 3, 21)
    testAe = date(2019, 4, 19)
    testTs = date(2019, 4, 20)
    testTe = date(2019, 5, 20)
    testGs = date(2019, 5, 21)
    testGe = date(2019, 6, 20)
    testCNs = date(2019, 6, 21)
    testCNe = date(2019, 7, 22)
    testLOs = date(2019, 7, 23)
    testLOe = date(2019, 8, 22)
    testVs = date(2019, 8, 23)
    testVe = date(2019, 9, 22)
    testLBs = date(2019, 9, 23)
    testLBe = date(2019, 10, 22)
    testSCs = date(2019, 10, 23)
    testSCe = date(2019, 11, 21)
    testSGs = date(2019, 11, 22)
    testSGe = date(2019, 12, 21)
    testCPs = date(2019, 12, 22)
    testCPe = date(2019, 1, 19)
    #test = str(test.strftime('%d/%m'))
    #test2 = datetime.now()
    #test2 = str(test2.strftime('%d/%m'))
    for i in range(len(options)) :
        if options[i] == clicked.get():
            i = i+1
            #test2 = str(clickeds.get()) + "/" + i
            #test2 = datetime.date(2019, clickeds.get(), i)
            test2 = date(2019, i, clickeds.get())
            #test2 = date.strftime(str(clickeds.get()), '%d/%m', str(i))
    if test2 >= testGs and test2 <= testGe:
        #label.config(text = clicked.get() + " " + str(clickeds.get()) + " Gemini")
        label.config(text = "Gemini")
        print(test2)
        print(testGs)
        print(testGs)
    elif test2 >= testTs and test2 <= testTe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testTs)
        print(testTe)
    elif test2 >= testAs and test2 <= testAe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testAs)
        print(testAe)
    elif test2 >= testPs and test2 <= testPe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testPs)
        print(testPe)
    elif test2 >= testAQs and test2 <= testAQe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testAQs)
        print(testAQe)
    elif test2 >= testCNs and test2 <= testCNe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testCNs)
        print(testCNe)
    elif test2 >= testLOs and test2 <= testLOe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testLOs)
        print(testLOe)
    elif test2 >= testVs and test2 <= testVe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testVs)
        print(testVe)
    elif test2 >= testLBs and test2 <= testLBe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testLBs)
        print(testLBe)
    elif test2 >= testSCs and test2 <= testSCe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testSCs)
        print(testSCe)
    elif test2 >= testSGs and test2 <= testSGe:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testSGs)
        print(testSGe)
    else:
        label.config( text = clicked.get() + " " + str(clickeds.get()))
        print(test2)
        print(testCPs)
        print(testCPe)

  
# Dropdown menu options
options = [ "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
optionss = []
i = 32
for x in range (1, i): 
    optionss.append(x)

# datatype of menu text
clicked = StringVar()
clickeds = IntVar()

# initial menu text
#clicked.set("January")
#clickeds.set(1)
who = date.today()
whos = options[who.month]
clicked.set(whos)
clickeds.set(who.day)
  
# Create Dropdown menu
drop = OptionMenu(main , clicked , *options )
drop.pack()

# Create Dropdown menu
drops = OptionMenu(main , clickeds , *optionss )
drops.pack()
  
# Create button, it will change label text
button = Button(main , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label(main , text = " " )
label.pack()

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