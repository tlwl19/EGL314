from tkinter import *
from tkinter import ttk

# Function to choose colour
def choose_colour(m):
    global colour #value of the colour selected
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
  print(canvasdraw)


def allwht():
  for r in range (32):
    for c in range (32):
      button[r][c].config(bg='grey99')
      value[r][c] = 0
  #canvasdraw = [[0 for r in range(576)] for c in range(576)]

def allblk():
  for r in range (32):
    for c in range (32):
      button[r][c].config(bg='grey1')
      value[r][c] = 90
  #canvasdraw = [[90 for r in range(576)] for c in range(576)]
 

def get_x_and_y(event):
   global lasx, lasy
   lasx, lasy = event.x, event.y

def paint(event):
    global lasx, lasy, value
    if lasx >= 0 and lasx <= 575 and lasy >= 0 and lasy <= 575:
      if colour == 0: 
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey99',width=4)
          canvasdraw[lasx][lasy] = 0
      elif colour == 20:
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey88',width=4)
          canvasdraw[lasx][lasy] = 20
      elif colour == 30:
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey77',width=4)
          canvasdraw[lasx][lasy] = 30
      elif colour == 40: 
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey66',width=4)
          canvasdraw[lasx][lasy] = 40
      elif colour == 50:
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey44',width=4)
          canvasdraw[lasx][lasy] = 50
      elif colour == 60: 
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey33',width=4)
          canvasdraw[lasx][lasy] = 60
      elif colour == 70:
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey22',width=4)
          canvasdraw[lasx][lasy] = 70
      else: 
          canvas.create_line((lasx,lasy, event.x, event.y),fill='grey11',width=4)
          canvasdraw[lasx][lasy] = 90
      get_x_and_y(event)


def save_draw_colour(list):
  for r in range(32):
    for c in range(32):
      if list[r][c] == 0:
        button[c][r].config(bg='grey99')
      elif list[r][c] == 20: 
        button[c][r].config(bg='grey88')
      elif list[r][c] == 30:
        button[c][r].config(bg='grey77')
      elif list[r][c] == 40: 
        button[c][r].config(bg='grey66')
      elif list[r][c] == 50:
        button[c][r].config(bg='grey44')  
      elif list[r][c] == 60: 
        button[c][r].config(bg='grey33')
      elif list[r][c] == 70:
        button[c][r].config(bg='grey22')
      else: 
        button[c][r].config(bg='grey1')

def savecanvas():
  global list2, list1, value, list4
  list2 = []
  list1 = []
  list3 = []
  list4 = []
  #f0(18)
  for r in range(0, 576, 18):
    list3 = []
    for c in range(0 , 576, 18):
      #list3 = []
      #f0(t, i)
      getnumber = f0(r, c)
      #print(i, t)
      list3.append(getnumber)
    list4.append(list3)
    #list3.append(list1)
  save_draw_colour(list4)
  print(list4)
  
def f0(x, y): #get the starting x, y of a 18x18 and to return 1 value back to rep the 18x18, to scale down a 18x18 to a 1x1
  global list0, list1, list2
  list0 = []
  #num1 = 18*(x-1)
  #num2 = num1 + 18
  for r in range(x ,18+x):
    for c in range(y ,18+y):
      list0.append(canvasdraw[r][c])
  freq = min(set(list0), key = list0.count) #using min instead cause if max almost everytime will get 0,harder for the draw to show; once the 18x18 grid got 1 value change, then return that value
                                            #Link: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
  #list1.append(freq)
  return freq 



def clearbtn():
  allwht()
  for r in range(576):
    for c in range(576):
      canvasdraw[r][c] = 0
  canvas.delete('all')
  print(canvasdraw)
  
def tictactoe():
  frame2.destroy()
  frame3.destroy()
  frame4.destroy()


main = Tk()
main.title("still doing")

notebook = ttk.Notebook(main) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2
tab3 = Frame(notebook) #new frame for tab 3

notebook.add(tab1,text="Grid")
notebook.add(tab2,text="Draw")
# notebook.add(tab3, text="tictactoe")
notebook.grid(row=0, column = 0)

frame1 = Frame(tab1, width=800, height=800) #3x3 btn
frame1.grid(row=0, column=0)
# frame1.grid(ipadx='64px', ipady='64px')

frame2 = Frame(main) #shades btn
frame2.grid(row=0, column=1)

frame3 = Frame(main)
frame3.grid(row=1, columnspan=2) #colour btns 

frame4 = Frame(main)
frame4.grid(row=2, columnspan=2) #send btn

frame5 = Frame(tab2) # draw canvas 
frame5.grid(row=0, column=0) 


canvas = Canvas(tab2, width=576, height=576, bg='white')  
canvas.grid(row=0, column=0)

canvas.bind('<Button-1>', get_x_and_y)
canvas.bind('<B1-Motion>',paint)
canvas.bind('<Enter>', get_x_and_y)

#this variable to store the colour choice 
colour = 0
canvasdraw = [[0 for r in range(576)] for c in range(576)]  # save eventxy into an array 
#print(canvasdraw)


# 32x32 grid
button = [[r for r in range(32)] for c in range(32)]

value = [[0 for r in range(32)] for c in range(32)]
# print("Value is {}".format(value))

for r in range (32):
  for c in range (32):
    button[r][c] = Button(frame1, font=("Calibri, 5"), width=1, height=1, bg='white', command=lambda x=r, y=c:colour_picker(x, y))
    button[r][c].grid(row=r, column=c)


#shades button
white = Button(frame2, text="White", font=("Calibri, 10"), bg='grey99', width=13, height=2, command=lambda m=0:choose_colour(m))
white.grid(row=1, column=0)
grey1 = Button(frame2, text="Grey1", font=("Calibri, 10"), bg='grey88', width=13, height=2, command=lambda m=20:choose_colour(m))
grey1.grid(row=2, column=0)
grey2 = Button(frame2, text="Grey2", font=("Calibri, 10"), bg='grey77', width=13, height=2, command=lambda m=30:choose_colour(m))
grey2.grid(row=3, column=0)
grey3 = Button(frame2, text="Grey3", font=("Calibri, 10"), bg='grey66', width=13, height=2, command=lambda m=40:choose_colour(m))
grey3.grid(row=4, column=0)
grey4 = Button(frame2, text="Grey4", font=("Calibri, 10"), bg='grey44', width=13, height=2, command=lambda m=50:choose_colour(m))
grey4.grid(row=5, column=0)
grey5 = Button(frame2, text="Grey5", font=("Calibri, 10"), bg='grey33', fg='white', width=13, height=2, command=lambda m=60:choose_colour(m))
grey5.grid(row=6, column=0)
grey6 = Button(frame2, text="Grey6", font=("Calibri, 10"), bg='grey11', fg='white', width=13, height=2, command=lambda m=70:choose_colour(m))
grey6.grid(row=7, column=0)
black = Button(frame2, text="Black", font=("Calibri, 10"), bg='grey1', fg='white', width=13, height=2, command=lambda m=90:choose_colour(m))
black.grid(row=8, column=0)

#save button
savebtn = Button(frame2, text="Save", font=("Calibri, 10"), bg='light blue', fg='black', width=13, height=2, command=savecanvas)
savebtn.grid(row=9, column=0)

#colour button
allwhite = Button(frame3, text="All White",font=("Calibri, 12"), bg='white', width=13, height=2, command=allwht)
allwhite.grid(row=0, column=0)

allblack = Button(frame3, text="All Black",font=("Calibri, 12"), bg='black', fg='white', width=13, height=2, command=allblk)
allblack.grid(row=0, column=1)

clear = Button(frame3, text="Clear",font=("Calibri, 12"), bg='gold', width=13, height=2, command=clearbtn)
clear.grid(row=0, column=2)


#send btn
send = Button(frame4, text="Send Image!", font=("Calibri, 12"), width=13, height=2, command=lambda :sendbtn())
send.grid(row=0, column=0)

main.mainloop()
