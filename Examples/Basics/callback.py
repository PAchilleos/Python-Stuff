from tkinter import *

root=Tk()

def callback(event):
    root.focus_set()
    print ("clicked at", event.x, event.y)
    
root.bind("<Button-1>", callback)
