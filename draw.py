from tkinter import *
from tkinter import ttk
import cartoon


def choose_colour(m):
    global colour #Value of the colour selected
    colour = m


def colour_picker(r, c):
  global colour
  if colour == 0:
      button[r][c].config(bg='grey99') #to configure the background colour of the grid selected with the selected colour
      value[r][c] = colour #assign the grid's angle value based on the colour selected
  elif colour == 20:
      button[r][c].config(bg='grey88')
      value[r][c] = colour
  elif colour == 30:
      button[r][c].config(bg='grey77')
      value[r][c] = colour
  elif colour == 40:
      button[r][c].config(bg='grey66')
      value[r][c] = colour
  elif colour == 50:
      button[r][c].config(bg='grey44')
      value[r][c] = colour
  elif colour == 60:
      button[r][c].config(bg='grey33')
      value[r][c] = colour
  elif colour == 70:
      button[r][c].config(bg='grey11')
      value[r][c] = colour
  else:
      button[r][c].config(bg='grey1') 
      value[r][c] = colour


def sendbtn():
  global value
  print(value)
  #pubpic(value)


def allwht():
  for r in range (32):
    for c in range (32):
      button[r][c].config(bg='grey99')
      value[r][c] = 0  #This is the angle of grey99
  canvas.config(bg = 'white')
  for r in range(800):
    for c in range(800):
      canvasdraw[r][c] = 0    


def allblk():
  for r in range (32):
    for c in range (32):
      button[r][c].config(bg='grey1')
      value[r][c] = 90 #This is the angle of grey1
  canvas.config(bg = 'black')
  for r in range(800):
    for c in range(800):
      canvasdraw[r][c] = 90    
 

def get_x_and_y(event):
   global getx, gety
   getx, gety = event.x, event.y


def paint(event):   #creating line
    global getx, gety, value
    if getx >= 0 and getx <= 799 and gety >= 0 and gety <= 799:
      if colour == 0: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey99',width=4)  #event.x is the position of the mouse relative to the widget
          canvasdraw[getx][gety] = 0   #store position in canvasdraw
      elif colour == 20:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey88',width=4)
          canvasdraw[getx][gety] = 20
      elif colour == 30:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey77',width=4)
          canvasdraw[getx][gety] = 30
      elif colour == 40: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey66',width=4)
          canvasdraw[getx][gety] = 40
      elif colour == 50:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey44',width=4)
          canvasdraw[getx][gety] = 50
      elif colour == 60: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey33',width=4)
          canvasdraw[getx][gety] = 60
      elif colour == 70:
          canvas.create_line((getx,gety, event.x, event.y),fill='grey22',width=4)
          canvasdraw[getx][gety] = 70
      else: 
          canvas.create_line((getx,gety, event.x, event.y),fill='grey11',width=4)
          canvasdraw[getx][gety] = 90
      get_x_and_y(event)


def save_draw_colour(list):  #number convert to colour
  global value
  for r in range(32):    
    for c in range(32):
      if list[r][c] == 0: 
        button[c][r].config(bg='grey99')
        value[c][r] = 0
      elif list[r][c] == 20: 
        button[c][r].config(bg='grey88')
        value[c][r] = 20
      elif list[r][c] == 30:
        button[c][r].config(bg='grey77')
        value[c][r] = 30
      elif list[r][c] == 40: 
        button[c][r].config(bg='grey66')
        value[c][r] = 40
      elif list[r][c] == 50:
        button[c][r].config(bg='grey44')  
        value[c][r] = 50
      elif list[r][c] == 60: 
        button[c][r].config(bg='grey33')
        value[c][r] = 60
      elif list[r][c] == 70:
        button[c][r].config(bg='grey22')
        value[c][r] = 70
      else: 
        button[c][r].config(bg='grey1')
        value[c][r] = 90


def savecanvas():  #convert 800x800 to 32x32 grid
  global value, list4 
  list3 = []  #one row only (1x18)
  list4 = []  #final output of 32x32 array that will convert to grid
  for r in range(0, 800, 25):
    list3 = []   #it will be empty once it is done getting the value for list4, will keep repeating 
    for c in range(0 , 800, 25): #will only loop 32times that is 1x18
      getnumber = f0(r, c)    #returning only 1 value
      list3.append(getnumber) #store that 1 value for 32 times
    list4.append(list3)       #row will loop 32 times
  save_draw_colour(list4)
  print(list4)
  

def f0(x, y): #get the starting x, y of a 18x18 and to return 1 value back to rep the 18x18, to scale down a 18x18 to a 1x1
  global list0
  list0 = []  #To store the value of 18x18 to store in 1 array,
  for r in range(x ,25+x):
    for c in range(y ,25+y):
      list0.append(canvasdraw[r][c])
  freq = min(set(list0), key = list0.count) #using min instead cause if max almost everytime will get 0,harder for the draw to show; once the 18x18 grid got 1 value change, then return that value
  return freq  #Returning min value 


def clearbtn():
  allwht()
  for r in range(800):
    for c in range(800):
      canvasdraw[r][c] = 0
  canvas.delete('all')
  print(canvasdraw)


main = Tk()
main.title("Draw")

master = ttk.Notebook(main) #widget that manages a collection of windows/displays

tabgrid = Frame(master) #new frame for tab grid
tabdraw = Frame(master) #new frame for tab draw

#Placement is at the top left corner
master.add(tabgrid,text="Grid")
master.add(tabdraw,text="Draw")
master.grid(row=0, column = 0)

gridframe = Frame(tabgrid, width=800, height=800) #32x32 btn
gridframe.grid(row=0, column=0)

shadeframe = Frame(main) #shades btn
shadeframe.grid(row=0, column=1)

colourframe = Frame(main)
colourframe.grid(row=1, column=0) #all white/black btns and send btn 


#Set canvas background colour to white
canvas = Canvas(tabdraw, width=800, height=800, bg='white')  
canvas.grid(row=0, column=0)

canvas.bind('<Button-1>', get_x_and_y)
canvas.bind('<B1-Motion>',paint)
canvas.bind('<Enter>', get_x_and_y)

#This variable to store the colour choice 
colour = 0
canvasdraw = [[0 for r in range(800)] for c in range(800)]  # save eventxy into an array 

# 32x32 grid
button = [[r for r in range(32)] for c in range(32)]
value = [[0 for r in range(32)] for c in range(32)]  #angle

for r in range (32):
  for c in range (32):
    button[r][c] = Button(gridframe, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda x=r, y=c:colour_picker(x, y))
    button[r][c].grid(row=r, column=c)

#shades button
white = Button(shadeframe, text="White", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=lambda m=0:choose_colour(m))
white.grid(row=1, column=0)
grey1 = Button(shadeframe, text="Grey1", font=("Calibri, 10"), bg='grey88', width=13, height=2, command=lambda m=20:choose_colour(m))
grey1.grid(row=2, column=0)
grey2 = Button(shadeframe, text="Grey2", font=("Calibri, 10"), bg='grey77', width=13, height=2, command=lambda m=30:choose_colour(m))
grey2.grid(row=3, column=0)
grey3 = Button(shadeframe, text="Grey3", font=("Calibri, 10"), bg='grey66', width=13, height=2, command=lambda m=40:choose_colour(m))
grey3.grid(row=4, column=0)
grey4 = Button(shadeframe, text="Grey4", font=("Calibri, 10"), bg='grey44', width=13, height=2, command=lambda m=50:choose_colour(m))
grey4.grid(row=5, column=0)
grey5 = Button(shadeframe, text="Grey5", font=("Calibri, 10"), bg='grey33', fg='white', width=13, height=2, command=lambda m=60:choose_colour(m))
grey5.grid(row=6, column=0)
grey6 = Button(shadeframe, text="Grey6", font=("Calibri, 10"), bg='grey11', fg='white', width=13, height=2, command=lambda m=70:choose_colour(m))
grey6.grid(row=7, column=0)
black = Button(shadeframe, text="Black", font=("Calibri, 10"), bg='grey1', fg='white', width=13, height=2, command=lambda m=90:choose_colour(m))
black.grid(row=8, column=0)

#save button
savebtn = Button(shadeframe, text="Save", font=("Calibri, 10"), bg='light blue', fg='black', width=13, height=2, command=savecanvas)
savebtn.grid(row=9, column=0)

#colour button
allwhite = Button(colourframe, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(colourframe, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

clear = Button(colourframe, text="Clear",font=("Calibri, 12"), bg='gold', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=2)

#send btn
send = Button(colourframe, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=3)



main.mainloop()
