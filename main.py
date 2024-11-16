# from graphics import Window #Line, Point, MyLine, Cell, Maze
from gui import Window
from tkinter import *
# import tkinter as tk
#from tkinter import ttk

def main():    
    '''
    print("tlhIngan Hol ghojmoHwI' boQ")
    print("Klingon Hol Teacher's Aid")
    print("This program provides some teaching aids for learning Klingon")

    win = Window("tlhIngan Hol ghojmoHwI' boQ")
    
    win.AddLabel("nuq DaneH qo'!")
    win.AddButton("Quit", 30, "destroy")
    win.AddEntry()

    # Start the GUI event loop
    win.Run()
    '''

    #Test of color options
    root = Tk()
    root.title("Color Options in Tkinter")

    # Create a button with active background and foreground colors
    button = Button(root, text="Click Me", activebackground="blue", activeforeground="white")
    button.pack()

    #Create a label with background and foreground colors
    label = Label(root, text="Hello, Tkinter!", bg="lightgray", fg="red")
    label.pack()

    # Create an Entry widget with selection colors
    entry = Entry(root, selectbackground="lightblue", selectforeground="green")
    entry.pack()

    root.mainloop()

    pass
    
main()