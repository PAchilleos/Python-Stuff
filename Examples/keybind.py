from tkinter import *

root = Tk()
root.withdraw()

print ("Ready");

def key(event):
    print ("pressed", repr(event.char))  

root.bind("<Key>", key)

root.mainloop()
