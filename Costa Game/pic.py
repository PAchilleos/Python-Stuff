import tkinter
from tkinter import *

d=2
dx=10
dy=2
#def key(event):
 #   co=canvas.coords(ball)
  #  co= [co[0]-d,co[1]-d,co[2]+d,co[3]+d]
    #canvas.coords(ball,co)
    #canvas.move(ball,dx,0)
    #print ("pressed", repr(event.char))  



root = Tk()
root.geometry("800x400")
frame = Frame(root)
#canvas.grid(row = 0, column = 0)
photo = PhotoImage(file = './Costa.png')
photo = photo.subsample(4)

label= Label(frame, image=photo)
label.pack()
frame.place(x=0,y=0)
#pic=canvas.create_image(100,100, image=photo)
#ball=canvas.create_oval(10, 20, 20, 10, outline='black', fill='black', tags=('ball'))
#ball2=canvas.create_oval(10, 20, 20, 10, outline='red', fill='red', tags=('ball'))
#root.bind("<z>", key)


    
    







