from tkinter import *
import winsound

#pre defined

def callback():
    print ("click!")
            
class Application(Frame):
    """ App """

    def __init__(self,master):
        """Initialise the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks=0 #count the number of button clicks for button 1
        self.create_widgets()

    def create_widgets(self):
        self.button1=Button(self, text="Button 1 Total Clicks: 0")
        self.button1["command"] =self.update_count
        self.button1.grid()        

        self.button2=Button(self,command=self.soundclip)
        self.button2.grid()
        #can add text after you've defined the button
        self.button2.configure(text="Wolf Howl")

        self.button3=Button(self, command=self.callback)
        self.button3.grid()
        #alternative method to add text to button
        self.button3["text"]= "Button 3"

    def update_count(self): #button1
        """Updates count on button 1"""
        self.button_clicks += 1
        self.button1["text"] = "Button 1 Total Clicks: " +str(self.button_clicks)

    def soundclip(self): #button2
        winsound.PlaySound('C:\\Users\\Procopis\\Desktop\\Projects\\Python Stuff\\Examples\\wolf.wav', winsound.SND_FILENAME)

    def callback(self): #button3
        print ("clicked!")

root=Tk()
root.title("Another GUI")
root.geometry("400x100")

app=Application(root)

root.mainloop()
    
       


    
     


