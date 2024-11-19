# from graphics import Window #Line, Point, MyLine, Cell, Maze
from gui import *
from myclasses import *

# from tkinter import *
# import tkinter as tk
#from tkinter import ttk



def main():    
    # print("tlhIngan Hol ghojmoHwI' boQ")
    # print("Klingon Hol Teacher's Aid")
    # print("This program provides some teaching aids for learning Klingon")

    #Create our main app window
    app = App("tlhIngan Hol ghojmoHwI' boQ", 400, 400)
    # Start the GUI event loop
    app.Run()
    pass

if __name__ == "__main__":  
    main()