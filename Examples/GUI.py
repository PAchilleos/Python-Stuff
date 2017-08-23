from tkinter import *   ## notice lowercase 't' in tkinter here for python 3
import time
t = time.time()
#create window
root=Tk()

#window properties
root.title("My GUI")
root.geometry("200x200")


#creates a frame to add widgets
app=Frame(root)
app.grid() # puts the widget on the gui
label = Label(app, text="Label")
label.grid()

app2=Frame(root) #add buttons
app2.grid()
button1=Button(app2, text= "Button")
button1.grid()

button2= Button(app2, text="Another Button")
button2.grid()
elapsed = time.time() - t

#kick off the event loop
root.mainloop()


