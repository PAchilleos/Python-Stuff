from tkinter import *
import time


x=80;
y=120; #ball starting position
dx=3;
dy=3;
d=0.2;

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
        if self.pressed["w"]:            
            co=canv.coords(ball)             
            co= [co[0]-d,co[1]-d,co[2]+d,co[3]+d]
            canv.coords(ball,co)
            canv.move(ball, 0,-3)
        if self.pressed["s"]:              
            co=canv.coords(ball)
            co= [co[0]+d,co[1]+d,co[2]-d,co[3]-d]
            canv.coords(ball,co)
            canv.move(ball,0,3)
        if self.pressed["a"]:            
            co=canv.coords(ball)
            co= [co[0]+d,co[1]+d,co[2]-d,co[3]-d]
            canv.coords(ball,co)
            canv.move(ball,-3,0)
        if self.pressed["d"]:
            co=canv.coords(ball)
            co= [co[0]-d,co[1]-d,co[2]+d,co[3]+d]
            canv.coords(ball,co)
            canv.move(ball,3,0)            
            
        
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
top = canv.create_line(50, 0, 850, 0, fill='blue', tags=('top'))
left = canv.create_line(50,0 , 50, 550, fill='blue', tags=('left'))
right = canv.create_line(850, 0, 850, 550, fill='blue', tags=('right'))
bottom = canv.create_line(50, 550, 850, 550, fill='blue', tags=('bottom'))

#rect = canv.create_rectangle(270, 468, 365, 478, outline='black', fill='gray40', tags=('rect'))
ball = canv.create_oval(0, 10, 10, 0, outline='black', fill='black', tags=('ball'))
canv.move(ball, x,y)
canv.focus_set()


game = Controls()
game.start()  





