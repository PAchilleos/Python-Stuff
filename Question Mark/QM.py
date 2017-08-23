from tkinter import *   ## notice lowercase 't' in tkinter here for python 3
import time
import random
import sys
t = time.time()

c=0;
lim=10; #limit of how may dummy buttons there can be for c==6
g=[0]*lim;# pre allocate g
x=1 # starting value of x to create one dummy button
def rngp(): #Generates button positions on the widget    
    win_w=root.winfo_width()
    win_h= root.winfo_height()
    w=button.winfo_width()    
    h=button.winfo_height()
    w1=button1.winfo_width()    
    h1=button1.winfo_height()    
    rngp.n_x=random.uniform(0, win_w-w1-w)
    rngp.n_y=random.uniform(h, win_h-h1)
    
    
    
def callback():
    global c
    rngp()    
    button1.place(y=rngp.n_y, x=rngp.n_x)
    
    if c == 0:
        button1.configure(text="Once More?")        
    elif 0< c < 5:
        button1.configure(text="Once again?")        
    elif c==5: # needs to be fixed
        button1.configure(text="Catch Me!!")  
        i=1
        while i<11:  
            rngp()
            button1.place(y=rngp.n_y, x=rngp.n_x)
            print (i)
            #time.sleep(1), #Disabled until this level is fixed
            i+=1
            
        #trying to make the button change position while you try to click it, however
        #the button only shows its last position in the loop
            
    elif c==6: #needs to be tweaked
        button1.configure(text="is this the button?")
        global x
               
               
        for i in range(0,x):
            makeframe()
            g[i]=makeframe.app
            button2=Button(g[i], text= "is this the button!",command=dup) 
            button2.grid()
            #! instead of ? to distinguish the dummy buttons, change when completed

        #NEED TO MAKE SURE FRAMES DO NOT OVERLAP SO BUTTONS CAN BE CLEARLY PRESSED!!
 
        
               
    else:        
        for i in range(0,x):
            g[i].destroy()
        
        button1.configure(text="Done for now")
        button1['state'] = 'disabled'

    c=counter(c) 
        
def des():
    root.destroy()
    sys.exit()
    
       
    #print(c)

def makeframe():
    #x=1;
    rngp()
    w1=button1.winfo_width()    
    h1=button1.winfo_height()
    makeframe.app=Frame(root, height=h1, width=w1)
    makeframe.app.place(y=rngp.n_y, x=rngp.n_x)


def dup():    
    global x   
   
    for i in range(0,x):
        g[i].destroy()

    x+=1

    if x>lim: #x=10 is the limit for now, once x>10, program closes
        button1.configure(text="You Lose!")
        button1['state'] = 'disabled'

    else:
        print(x) #remove when level c==6 is completed
        rngp()
        button1.place(y=rngp.n_y, x=rngp.n_x)
        for i in range(0,x):
            makeframe()
            g[i]=makeframe.app
            button2=Button(g[i], text= "is this the button!",command=dup)
            button2.grid()

          
root=Tk()
root.title("My GUI")
root.geometry("400x200")

button1=Button(root, text= "Hello, Click me!",command=callback)
button1.place(y=100, x=200)

button=Button(root, text="End",command=des)
button.place(rely=0, relx=1.0, x=0, y=0, anchor=NE)

def counter(c):
    c+=1
    return c



elapsed= time.time()-t




