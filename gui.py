from tkinter import *
#import tkinter as tk

#----------- WINDOW CLASS -----------
class Window:
    def __init__(self, title, height, width, master=None):
        self.master = master
        self.root = Tk() if master is None else Toplevel(master)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

    def AddButton(self, text, command, row, column, col_span=1):
        #command does not do anything yet.
        btn = Button(self.root, text=text, command=command)
        btn.grid(row=row, column=column, columnspan=col_span)
        return btn
    
    def AddEntry(self, row, column, col_span=1, width=10):
        etr = Entry(self.root, relief="sunken", width=width)
        etr.grid(row=row, column=column, columnspan=col_span)
        return etr
    
    def AddFrame(self, row, column, col_span=1):
        frm = Frame(self.root)
        frm.grid(row=row, column=column, columnspan=col_span)
        return frm

    def AddLabel(self, text, row, column, col_span=1):
        #This creates a label in the window in a particular grid location. The various aspects are then set in the Label
        lbl = Label(self.root, text=text)
        lbl.grid(row=row, column=column, columnspan=col_span)
        return lbl 
    
    def AddTextBox(self, height, width, row, column, col_span=1):
        txt_box = Text(self.root, width=width, height=height)
        txt_box.grid(row=row, column=column, columnspan=col_span)
        return txt_box
    
    def show_modal(self):
        #Does not work, but through all research no one actually knows how to make this work.
        self.root.grab_set()  # Make the window modal
        self.master.wait_window(self.root)  # Block interaction with the master until this window is closed
    
    def Run(self):
        self.root.mainloop()
