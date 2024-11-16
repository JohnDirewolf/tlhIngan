from tkinter import *

class Window:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        
        pass

    def AddLabel(self, label_text):
        #w=Label(master, option=value)
        #master is the parameter used to represent the parent window.

        lbl = Label(self.root, text=label_text)
        lbl.pack()
        pass

    def Run(self):
        self.root.mainloop()