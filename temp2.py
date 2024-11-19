import tkinter as tk

class Window:
    def __init__(self, master=None):
        self.master = master
        self.window = tk.Tk() if master is None else tk.Toplevel(master)

    def add_label(self, text):
        label = tk.Label(self.window, text=text)
        label.pack()

    def show_modal(self):
        self.window.grab_set()  # Make the window modal
        self.master.wait_window(self.window)  # Block interaction with the master until this window is closed

class App(Window):
    def __init__(self):
        super().__init__()
        self.add_label("Main Window")

    def open_modal_dialog(self):
        dialog = Window(self.window)
        dialog.add_label("Modal Dialog")
        dialog.show_modal()

app = App()
# Adding a button to trigger the modal dialog
button = tk.Button(app.window, text="Open Modal", command=app.open_modal_dialog)
button.pack()

app.run()

