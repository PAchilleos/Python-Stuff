from tkinter import *
import time


x=80;
y=120; #ball starting position
root = Tk()
canv = Canvas(root, highlightthickness=0)
canv.pack(fill='both', expand=True)
top = canv.create_line(0, 0, 640, 0, fill='green', tags=('top'))
left = canv.create_line(0, 0, 0, 480, fill='green', tags=('left'))
right = canv.create_line(639, 0, 639, 480, fill='green', tags=('right'))
bottom = canv.create_line(0, 478, 640, 478, fill='red', tags=('bottom'))

rect = canv.create_rectangle(270, 468, 365, 478, outline='black', fill='gray40', tags=('rect'))
ball = canv.create_oval(0, 10, 10, 0, outline='black', fill='black', tags=('ball'))
canv.move(ball, x,y)
canv.focus_set()

def key(event):
    
    if event.char == 'w' :
        canv.move(ball, 0,-3);
    elif event.char == 'a' :
        canv.move(ball,-3,0);
    elif event.char == 's' :
        canv.move(ball,0,3)
    elif event.char == 'd' :
        canv.move(ball,3,0) 
    


canv.bind("<Key>", key)
canv.pack()


