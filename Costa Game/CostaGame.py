from tkinter import *
from random import randint
import time


x=50;
y=0;
z=10;
s=10;
class Controls(): # sets user controls
    def __init__(self):
        self.pressed = {}
        self._create_ui()
        
       
    def start(self):
        self._animate()       
        self.root.mainloop()

    def _create_ui(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry("200x200")
        app=Frame(self.root)
        app.grid()
        label = Label(app, text="Click This Window to Play")
        label.grid()
        
        #self.root.withdraw()
        self._set_bindings()

        
    def _animate(self): #intructions for controls
        
        global x
        global y
        global z
        global s
        global c
        global cx
        global cy
        global OV

        width= frame.winfo_width();
        co_x=frame.winfo_rootx()-408;
        co_x=co_x+width/2;
        co_y= frame.winfo_rooty()-81;
        co_y = co_y +width/2;
            
        if self.pressed["w"]:            
            if 0 < frame.winfo_rooty()-81:
                y-=3
                frame.place(x=x,y=y)                
            else:
                
                frame.place(x=x,y=y)
                
            
        if self.pressed["s"]:
            if frame.winfo_rooty()-81 + width <550:
                y+=3
                frame.place(x=x,y=y)                             
            else:                
                frame.place(x=x,y=y)
            
        if self.pressed["a"]:
            if 50< frame.winfo_rootx()-408:
                x-=3
                frame.place(x=x,y=y)                
            else:                
                frame.place(x=x,y=y)
                
        if self.pressed["d"]:
            if frame.winfo_rootx()-408 +width <850:
                x+=3
                frame.place(x=x,y=y)                
            else:                
                frame.place(x=x,y=y)

        if (cx-(width/2)<co_x<cx+(width/2)) and (cy-(width/2)<co_y<cy+(width/2)):
            z=z+1
            zm(z,s)
            cx=0;
            cy=0;
            canv.delete(OV)
            rndx=randint(60,840)
            rndy=randint(10,540)
            OV=canv.create_oval(rndx, rndy, rndx+10, rndy+10, width=2, fill='blue');
            c=canv.coords(OV);
            cx=mean([c[0],c[2]])
            cy=mean([c[1],c[3]])                  

        #print(frame.winfo_rootx()-408)  #408 is the x offset
        #print(frame.winfo_rooty()-81)    #81 is the y offset

                   
            
        self.root.after(10, self._animate)
        
    def _set_bindings(self):
        for char in ["w","s","a", "d"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = False

    def _pressed(self, event):
        self.pressed[event.char] = True

    def _released(self, event):
        self.pressed[event.char] = False

    
#Create Game   
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


OV=canv.create_oval(100, 110, 110, 120, width=2, fill='blue');
c=canv.coords(OV);
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

cx=mean([c[0],c[2]])
cy=mean([c[1],c[3]])
print(cx)
print(cy)


         

frame = Frame(root)
#canvas.grid(row = 0, column = 0)
photo = PhotoImage(file = './Costa.png')
photo = photo.subsample(4)

label= Label(frame, image=photo)
label.pack()
frame.place(x=x,y=y)
#print(frame.winfo_rootx())  #gets frame geometry
#print(frame.winfo_rooty())
#print(frame.winfo_width())
#print(frame.winfo_height())  USE THESE


def printcoords(event):
    #outputting x and y coords to console
    print (event.x,event.y)
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)


def zm(a,b): #Makes Costa Bigger
    global frame
    global photo
    frame.destroy()
    frame = Frame(root)
    photo = PhotoImage(file = './Costa.png') #Reload image to prevent loss of picture quality
    photo = photo.subsample(4)
    photo = photo.zoom(a)
    photo = photo.subsample(b)
    label= Label(frame, image=photo)
    label.pack()
    frame.place(x=x,y=y)

#Next to add, start with simple squares and when Costa hovers over them, he gets bigger, use the zm(a,b) function above
    #make square disappear after Costa has passed over it
    #need a counter to show how many squares have been 'eaten' (n), then the size of Costa is achieved by zm(a,b) where a=n+b
    #b in the function is basically the scale rate (Sets the rate at which Costa grows). Change accordingly
    #squares to be randomly placed on window, try frames first so they're easy to remove. If this causes problems need an alternative approach

game = Controls()
game.start()  





