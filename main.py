# from graphics import Window #Line, Point, MyLine, Cell, Maze
import classes
import database

# from tkinter import *
# import tkinter as tk
#from tkinter import ttk

def main():
    #Load the database
    database.load_dict()
    #Create our main app window
    app = classes.App()
    # Start the GUI event loop
    app.Run()

if __name__ == "__main__":  
    main()