from tkinter import *

root=Tk()
root.resizable(width=False, height=False)

root.geometry("900x600+400+50")
canv = Canvas(root, highlightthickness=0)
canv.pack(fill='both', expand=True) 
top = canv.create_line(50, 0, 850, 0, fill='red', tags=('top'))
left = canv.create_line(50,0 , 50, 550, fill='blue', tags=('left'))
right = canv.create_line(850, 0, 850, 550, fill='yellow', tags=('right'))
bottom = canv.create_line(50, 550, 850, 550, fill='green', tags=('bottom'))

def printcoords(event):
    #outputting x and y coords to console
    print (event.x,event.y)
    #mouseclick event
canv.bind("<Button 1>",printcoords)
