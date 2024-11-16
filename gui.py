from tkinter import *
#import tkinter as tk

class Window:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        
        pass

    def AddLabel(self, label_text):
        #w=Label(master, option=value)
        #master is the parameter used to represent the parent window.
        #It is possible we don't need to declare the variable if we use grid.
        #We cannot use grid AND pack.

        Label(self.root, text=label_text, bg="lightgreen").grid(row=0)
        #lbl.pack()
        #Label can have a background color
        #We can add all the options at the start and not declare a variable or declare one and add the different aspects seperately.
        pass

    def AddMessage(self):
        #This is for creating a multiline non-editable text, like Label.
        '''
        from tkinter import *
        main = Tk()
        ourMessage = 'This is our Message'
        messageVar = Message(main, text=ourMessage)
        messageVar.config(bg='lightgreen')
        messageVar.pack()
        main.mainloop()
        '''
    def AddText(self):
        #This also creates multiline text, like Message.
        '''
        root = Tk()
        T = Text(root, height=2, width=30)
        T.pack()
        T.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')
        mainloop()
        '''

    def AddButton(self, button_text, width, command):
        #w=Button(master, option=value)
        #command does not do anything yet.
        Button(self.root, text=button_text, width=width, command=self.root.destroy).grid(row=1)
        #btn.pack()
        pass

    def AddEntry(self):
        #SpinBox is also a type of entry for a selection of numbers.
        '''
        So we can create labels in the grid and then add the entry boxes in the next column
        master = Tk()
        Label(master, text='First Name').grid(row=0)
        Label(master, text='Last Name').grid(row=1)
        e1 = Entry(master)
        e2 = Entry(master)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        '''

        Entry(self.root).grid(row=1, column=1)
        pass

    def AddCheckBox():
        '''
        Look into sticky
        master = Tk()
        var1 = IntVar()
        Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
        var2 = IntVar()
        Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
        mainloop()
        '''
        pass

    def AddRadioButton():
        '''
        Need to see how to do these with a grid, possibly sticky?
        root = Tk()
        v = IntVar()
        Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
        Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
        mainloop()
        '''
        pass

    def AddListBox():
        '''
        from tkinter import *
        top = Tk()
        Lb = Listbox(top)
        Lb.insert(1, 'Python')
        Lb.insert(2, 'Java')
        Lb.insert(3, 'C++')
        Lb.insert(4, 'Any other')
        Lb.pack()
        top.mainloop()
        '''
        pass

    def AddScrollBar():
        # Most likely this will need to be called by AddListBox or other object that needs a scrollbar
        '''
        root = Tk()
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        mylist = Listbox(root, yscrollcommand=scrollbar.set)

        for line in range(100):
            mylist.insert(END, 'This is line number' + str(line))
    
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)
        mainloop()
        '''
        pass

    def AddMenu():
        #This creates a menu bar and menu bar options.
        #Also see the Menubutton widget.
        '''
        root = Tk()
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')
        mainloop()
        '''
        pass

    def Run(self):
        self.root.mainloop()
        pass

'''
Combox box
Scale
TopLevel
Progress bar
Canvas - if we want to draw graphics, see our mazesolver project.
PannedWindow - Possibly something usefule like Grid

There are three geometry manager classes
pack() Works in blocks vertically, kind of like HTML block level elements
    # Create three buttons
    button1 = tk.Button(root, text="Button 1")
    button2 = tk.Button(root, text="Button 2")
    button3 = tk.Button(root, text="Button 3")

    # Pack the buttons vertically
    button1.pack()
    button2.pack()
    button3.pack()

grid() Works in a table, so very much like working in Excel.
    # Create three labels
    label1 = tk.Label(root, text="Label 1")
    label2 = tk.Label(root, text="Label 2")
    label3 = tk.Label(root, text="Label 3")

    # Grid the labels in a 2x2 grid
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=1, column=0, columnspan=2)

place() Works like CSS top, left placement. 
    # Create a label
    label = tk.Label(root, text="Label")

    # Place the label at specific coordinates
    label.place(x=50, y=50)
'''