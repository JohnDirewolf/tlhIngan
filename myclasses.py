from tkinter import *
from constants import *
import database

#__all__ = ["DevWin", "App", "VerbPrefixTable"]

#----------- UTILITY CLASS -------------
#This just creates a window used in development
class DevWin():
    def __init__(self, master):
        self.root = Toplevel(master)
        self.root.title("Development Tests")
        self.height = 400
        self.width = 1000
        self.root.geometry(f"{self.width}x{self.height}")
        self.output = ""
        self.setup_ui()

    def setup_ui(self):
        self.output = Text(self.root, height=10, width=120)
        self.output.grid(row=0, column=0, columnspan=3)

        btn_local = Button(self.root, text="Show Local Python Dictionary", command=self.print_python_dict)
        btn_local.grid(row=1, column=0, columnspan=1)
        btn_loaded = Button(self.root, text="Show Loaded Python Dictionary", command=self.print_loaded_dict)
        btn_loaded.grid(row=1, column=1, columnspan=1)        
        btn_clear = Button(self.root, text="Clear Output", command=self.clear_output)
        btn_clear.grid(row=1, column=3, columnspan=1)
        btn_save = Button(self.root, text="Save Dictionary", command=database.save_dict)
        btn_save.grid(row=2, column=0, columnspan=1)

        btn_load = Button(self.root, text="Load Dictionary", command=database.load_dict)
        btn_load.grid(row=2, column=1, columnspan=1)

    def print_python_dict(self):
        self.clear_output()
        self.output.insert(END, database.get_dict())

    def print_loaded_dict(self):
        self.clear_output()
        self.output.insert(END, database.get_dict())

    def clear_output(self):
        self.output.delete("1.0", END)

#This is a window used in learning GUI formatting and layout
class LayoutWin():
    def __init__(self, master):
        "Layout Window", 500, 500, 
        self.root = Toplevel(master)
        self.root.title("Layout Window")
        self.height = 500
        self.width = 500
        self.root.geometry(f"{self.width}x{self.height}")
        self.frame = ""
        self.rows = 5
        self.cols = 3
        self.subframes = [["" for j in range(self.cols)] for i in range(self.rows)]
        self.setup_ui()

    def setup_ui(self):
        self.frame = Frame(master=self.root, relief=RAISED, height=500, width=500, borderwidth=4)
        self.frame.grid(row=0, column=0, padx=5, pady=5)
        self.frame["bg"] = "blue"
        self.frame.grid_propagate(False)
        for i in range(self.rows):
            for j in range(self.cols):
                self.subframes[i][j] = Frame(master=self.frame, relief=SUNKEN, height=50, width=50, borderwidth=2)
                self.subframes[i][j].grid(row=i, column=j, padx=5, pady=5)
                self.subframes[i][j]["bg"] = "red"
                text = Label(self.subframes[i][j], text=f"Col: {j}, Row: {i}", height=2, width=2)
                text["bg"] = "white"
                text.grid(row=0, column=0, sticky="nsew")
                #text.config(font =("Courier", 8))


#----------- APP CLASS - INHERITS WINDOW CLASS AND ADDS THE LEARNING OPTIONS -----------
class App():
    def __init__(self, title, height, width):
        self.app = Tk()
        self.app.title(title)
        self.app.geometry(f"{width}x{height}")
        #Labels
        self.lbl_title = None
        self.lbl_tables = None
        self.lbl_flash_cards = None
        self.lbl_disclaimer = None
        #Buttons
        self.btn_verb_prefix_table = None
        self.btn_verb_previx_flash_cards = None
        #Dev
        self.btn_dev = None
        self.btn_layout = None

        self.setup_ui()  # Set up the specific UI elements

    def Close(self):
        self.app.destroy()

    def Run(self):
        self.app.mainloop()

    def setup_ui(self):
        self.lbl_title = Label(self.app, text="Klingon Hol Teacher's Aid")
        self.lbl_title.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.lbl_tables = Label(self.app, text="Tables")
        self.lbl_tables.grid(row=1, column=0)
        self.lbl_flash_cards = Label(self.app, text="Flash Cards")
        self.lbl_flash_cards.grid(row=1, column=1)

        self.btn_verb_previx_flash_cards = Button(self.app, text="Verb Prefix Table", command=self.show_verb_prefix_table)
        self.btn_verb_previx_flash_cards.grid(row=2, column=0)
        self.btn_verb_previx_flash_cards = Button(self.app, text="Verb Prefix Flash Cards", command=self.show_verb_prefix_cards)
        self.btn_verb_previx_flash_cards.grid(row=2, column=1)
        
        self.lbl_disclaimer = Label(self.app, text="""Klingon language is taken from 'The Klingon Dictionary' by Marc Okrand.\n
                      This app provides various practice drills to help memorize things like verb prefixes and locations.\n
                      This app does NOT provide information on pronounciation or grammar.\n
                      Also this app does not include new additions to the language out side of 'The Klingon Dictionary'.\n
                      To learn more about this beautiful langauge, please see 'The Klingon Dictionary' and other books by Marc Okrand.""")
        self.lbl_disclaimer.grid(row=3, column=0, columnspan=2)

        if DEV:
            self.btn_dev = Button(self.app, text="Show Development Window", command=self.show_dev_window)
            self.btn_dev.grid(row=4, column=0)
            self.btn_layout = Button(self.app, text="Show Layout Window", command=self.show_layout_window)
            self.btn_layout.grid(row=4, column=1)

    def show_verb_prefix_table(self):
        VerbPrefixTable(self.app)
        
    def show_verb_prefix_cards(self):
        FlashCards(self.app, "Verb Pronoun Prefixes")
        
    #Development Windows
    def show_dev_window(self):
        DevWin(self.app)

    def show_layout_window(self):
        LayoutWin(self.app)
    pass

#--------- FLASH CARD CLASSES -----------
def FlashCardSubFrame(parent, row, column, height, width, columnspan=1):
    frm = Frame(parent, relief=FLAT, height=height, width=width, borderwidth=0)
    frm.grid(row=row, column=column, columnspan=columnspan, padx=0, pady=0)
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_propagate(False)
    return frm

class FlashCards():
    def __init__(self, master, subtitle):
        #Setup of Window
        self.root = Toplevel(master)
        self.mySubtitle = subtitle
        self.height = 510
        self.width = 510
        self.root.title("Flash Cards!")
        self.root.geometry(f"{self.width}x{self.height}")
        #Widget variables
        self.rows, self.cols = (6, 3)
        self.frm_master = None
        #Objects are a array of two variables, 0 is the frame, 1 is the widget.
        self.subtitle = [None, None]
        self.word = [None, None]
        self.lbl_answer = [None, None]
        self.entry_answer = [None, None]
        self.lbl_type = [None, None]
        self.entry_type = [None, None]
        self.submit = [None, None]
        self.show = [None, None]
        self.next = [None, None]
        self.prev = [None, None]
        self.close = [None, None]
        self.klingon = {}
        self.cmd_load_dict()
        self.setup_ui()  # Set up the specific UI elements at start

    def setup_ui(self):
        # Set up the Grid sizes
        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer raised boarder.
        self.frm_master = Frame(self.root, relief=RAISED, height=500, width=500, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)

        # Labels and other text widgets will automatically resize for the text within. So we don't fight this, we just let them clamp perfectly on their text.
        # Each label/text Widget has a parent frame to create the cell and then the text Widget can be positioned more cleanly.
        # Weight is added to the sub-grid to enable sticky for postioning.

        self.subtitle[0] = FlashCardSubFrame(self.frm_master, 0, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL*4, columnspan=4)
        self.subtitle[1] = Label(self.subtitle[0], text=self.mySubtitle)
        self.subtitle[1].grid(sticky="w")
        self.subtitle[1].config(font =(FC_TITLE_FONT, FC_TITLE_SIZE))
        self.subtitle[1]["fg"] = FC_FG
        #self.subtitle[1]["bg"] = FC_BG

        self.word[0] = FlashCardSubFrame(self.frm_master, 1, 0, FC_MINSIZE_ROW*2, FC_MINSIZE_COL*4, columnspan=4)
        self.word[1] = Label(self.word[0], text="Qapla'!")
        self.word[1].grid(sticky="")
        self.word[1].config(font =(FC_WORD_FONT, FC_WORD_SIZE))
        self.word[1]["fg"] = FC_FG
        #self.word[1]["bg"] = FC_BG

        self.lbl_answer[0] = FlashCardSubFrame(self.frm_master, 2, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        #self.lbl_answer[0]["bg"] = "orange"
        #This will need to know if we are translating English to Klingon or DIvI' mugh tlhIngan
        self.lbl_answer[1] = Label(self.lbl_answer[0], text="English:")
        self.lbl_answer[1].grid(sticky="")
        self.lbl_answer[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.lbl_answer[1]["fg"] = FC_FG
        #self.lbl_answer[1]["bg"] = FC_BG

        self.entry_answer[0] = FlashCardSubFrame(self.frm_master, 2, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*3, columnspan=3)
        #self.entry_answer[0]["bg"] = "yellow"
        self.entry_answer[1] = Entry(self.entry_answer[0], relief=SUNKEN, borderwidth=3)
        self.entry_answer[1].grid(sticky="NSEW")
        self.entry_answer[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.entry_answer[1]["fg"] = FC_FG
        self.entry_answer[1]["bg"] = FC_BG

        self.lbl_type[0] = FlashCardSubFrame(self.frm_master, 3, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        #self.lbl_type[0]["bg"] = "green"
        #This may or may not be shown if Type is important or not.
        self.lbl_type[1] = Label(self.lbl_type[0], text="Type:")
        self.lbl_type[1].grid(sticky="")
        self.lbl_type[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.lbl_type[1]["fg"] = FC_FG
        #self.lbl_type[1]["bg"] = FC_BG
        
        self.entry_type[0] = FlashCardSubFrame(self.frm_master, 3, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*3, columnspan=3)
        #self.entry_type[0]["bg"] = "lightblue"
        self.entry_type[1] = Entry(self.entry_type[0], relief=SUNKEN, borderwidth=3)
        self.entry_type[1].grid(sticky="NSEW")
        self.entry_type[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.entry_type[1]["fg"] = FC_FG
        #self.entry_type[1]["bg"] = FC_BG

        self.prev[0] = FlashCardSubFrame(self.frm_master, 4, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.prev[0]["bg"] = "purple"
        self.prev[1] = Button(self.prev[0], text="< Prev", command=self.cmd_prev, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.prev[1].grid(sticky="")
        self.prev[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.prev[1]["fg"] = FC_FG
        self.prev[1]["bg"] = FC_BG

        self.submit[0] = FlashCardSubFrame(self.frm_master, 4, 1, FC_MINSIZE_ROW, width=FC_MINSIZE_COL)
        self.submit[0]["bg"] = "red"
        self.submit[1] = Button(self.submit[0], text="Submit", command=self.cmd_submit, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.submit[1].grid(sticky="")
        self.submit[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.submit[1]["fg"] = FC_FG
        self.submit[1]["bg"] = FC_BG

        self.show[0] = FlashCardSubFrame(self.frm_master, 4, 2, FC_MINSIZE_ROW, width=FC_MINSIZE_COL)
        self.show[0]["bg"] = "orange"
        self.show[1] = Button(self.show[0], text="Show", command=self.cmd_show, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.show[1].grid(sticky="")
        self.show[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.show[1]["fg"] = FC_FG
        self.show[1]["bg"] = FC_BG

        self.next[0] = FlashCardSubFrame(self.frm_master, 4, 3, FC_MINSIZE_ROW, width=FC_MINSIZE_COL)
        self.next[0]["bg"] = "yellow"
        self.next[1] = Button(self.next[0], text="Next >", command=self.cmd_next, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.next[1].grid(sticky="")
        self.next[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.next[1]["fg"] = FC_FG
        self.next[1]["bg"] = FC_BG

        self.close[0] = FlashCardSubFrame(self.frm_master, 5, 1, FC_MINSIZE_ROW, width=FC_MINSIZE_COL*2, columnspan=2)
        self.close[0]["bg"] = "green"
        self.close[1] = Button(self.close[0], text="Close", command=self.cmd_close, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.close[1].grid(sticky="")
        self.close[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.close[1]["fg"] = FC_FG
        self.close[1]["bg"] = FC_BG

    def cmd_load_dict(self):
        print("Load Dictionary")

    def cmd_submit(self):
        print("Submit")

    def cmd_show(self):
        print("Show")
    
    def cmd_next(self):
        print("Next")

    def cmd_prev(self):
        print("Prev")

    def cmd_close(self):
        self.root.destroy()

#---------- TABLE TEST CLASSES ----------
class VerbPrefixTable():
    def __init__(self, master):
        self.root = Toplevel(master)
        self.height = 400
        self.width = 600
        self.root.title("Verb Prefix Table!")
        self.root.geometry(f"{self.width}x{self.height}")
        self.rows, self.cols = (6, 7)
        self.col_labels = [""]*(self.cols + 1)
        self.row_labels = [""]*(self.rows + 1)
        self.entry_box = [["" for j in range(self.cols)] for i in range(self.rows)]
        #self.answers = [["" for j in range(self.cols)] for i in range(self.rows)]
        self.answer_key = [["" for j in range(self.cols)] for i in range(self.rows)]
        self.btn_show_key = None
        self.btn_clear = None
        self.btn_score_test = None
        self.setup_ui()  # Set up the specific UI elements
        self.set_answer_key()
        self.set_null() #I-me, you-you, I-us etc are NOT VALID for a prefix ("---"), this is NOT the same as 0 for the combination does not have a prefix.

    def setup_ui(self):
        self.root.grid_columnconfigure([0], minsize=VP_MINSIZE_COL_0)
        self.root.grid_columnconfigure([1, 2, 3, 4, 5, 6, 7], minsize=VP_MINSIZE_COL)
        self.root.grid_rowconfigure(0, minsize=VP_MINSIZE_ROW_0)
        self.root.grid_rowconfigure([1, 2, 3, 4, 5, 6], minsize=VP_MINSIZE_ROW)

        # Column Names
        self.col_labels[0] = Label(self.root, text="OBJECT")
        self.col_labels[1] = Label(self.root, text="none")
        self.col_labels[2] = Label(self.root, text="me")
        self.col_labels[3] = Label(self.root, text="you")
        self.col_labels[4] = Label(self.root, text="him/\nher/\nit")
        self.col_labels[5] = Label(self.root, text="us")
        self.col_labels[6] = Label(self.root, text="you\nplural")
        self.col_labels[7] = Label(self.root, text="them")
        #Set colors and other attributes if needed
        for i in range(self.cols + 1):
            self.col_labels[i].grid(row=0, column=i)
            self.col_labels[i].config(font =(VP_ALL_HDR_FONT, VP_ALL_HDR_FONT_SIZE))
            self.col_labels[i]["fg"] = VP_COL_HDR_FG
            self.col_labels[i]["bg"] = VP_COL_HDR_BG

        # Rows Names
        self.row_labels[0] = Label(self.root, text="SUBJECT")
        self.row_labels[1] = Label(self.root, text="I")
        self.row_labels[2] = Label(self.root, text="you")
        self.row_labels[3] = Label(self.root, text="he/she/it")
        self.row_labels[4] = Label(self.root, text="we")
        self.row_labels[5] = Label(self.root, text="you(plural)")
        self.row_labels[6] = Label(self.root, text="they")
        for j in range(self.rows + 1):
            self.row_labels[j].grid(row=j, column=0)
            self.row_labels[j].config(font =(VP_ALL_HDR_FONT, VP_ALL_HDR_FONT_SIZE))
            self.row_labels[j]["fg"] = VP_ROW_HDR_FG
            self.row_labels[j]["bg"] = VP_ROW_HDR_BG

        #Set up all our entries
        for i in range(0, self.rows):
            for j in range (0, self.cols):
                self.entry_box[i][j] = Entry(self.root, relief="sunken", width=VP_ENTRY_WIDTH)
                self.entry_box[i][j].grid(row=i+2, column=j+1)
                self.entry_box[i][j].config(font =(VP_FONT, VP_FONT_SIZE))
    
        #Add Buttons to show answers for study and referenece, a clear button, and a submit test button.
        self.btn_show_key = Button(self.root, text="moHaq yIcha': Show prefixes!", command=self.show_key)
        self.btn_show_key.grid(row=8, column=0, columnspan=4)
        self.btn_clear = Button(self.root, text="wa'chaw yIteq: Clear table!", command=self.clear)
        self.btn_clear.grid(row=8, column=4, columnspan=4)
        self.btn_score_test = Button(self.root, text="'el: Submit!", command=self.score_test)
        self.btn_score_test.grid(row=9, column=0, columnspan=8)

    def set_answer_key(self):
        self.answer_key[0][0] = "jI-"
        self.answer_key[0][1] = "---"
        self.answer_key[0][2] = "qa-"
        self.answer_key[0][3] = "vI-"
        self.answer_key[0][4] = "---"
        self.answer_key[0][5] = "Sa-"
        self.answer_key[0][6] = "vI-"
        self.answer_key[1][0] = "bI-"
        self.answer_key[1][1] = "cho-"
        self.answer_key[1][2] = "---"
        self.answer_key[1][3] = "Da-"
        self.answer_key[1][4] = "ju-"
        self.answer_key[1][5] = "---"
        self.answer_key[1][6] = "Da-"
        self.answer_key[2][0] = "0"
        self.answer_key[2][1] = "mu-"
        self.answer_key[2][2] = "Du-"
        self.answer_key[2][3] = "0"
        self.answer_key[2][4] = "nu-"
        self.answer_key[2][5] = "lI-"
        self.answer_key[2][6] = "0"
        self.answer_key[3][0] = "ma-"
        self.answer_key[3][1] = "---"
        self.answer_key[3][2] = "pI-"
        self.answer_key[3][3] = "wI-"
        self.answer_key[3][4] = "---"
        self.answer_key[3][5] = "re-"
        self.answer_key[3][6] = "DI-"
        self.answer_key[4][0] = "Su-"
        self.answer_key[4][1] = "tu-"
        self.answer_key[4][2] = "---"
        self.answer_key[4][3] = "bo-"
        self.answer_key[4][4] = "che-"
        self.answer_key[4][5] = "---"
        self.answer_key[4][6] = "bo-"
        self.answer_key[5][0] = "0"
        self.answer_key[5][1] = "mu-"
        self.answer_key[5][2] = "nI-"
        self.answer_key[5][3] = "lu-"
        self.answer_key[5][4] = "nu-"
        self.answer_key[5][5] = "lI-"
        self.answer_key[5][6] = "0"

    def set_null(self):    
        for i in range(0, self.rows):
            for j in range (0, self.cols):
                if self.answer_key[i][j] == "---":
                    self.entry_box[i][j].delete(0, END) #Should not be needed, but just in case.
                    self.entry_box[i][j].insert(0, "---")
                    self.entry_box[i][j]["bg"] = VP_BG_REF
                    self.entry_box[i][j].config(state="disabled") #Disabled so the user cannot change these, kept as boxes, not labels as that is simply cleaner.   

    # Button functions
    def score_test(self):
        qapla = True

        for i in range(0, 6):
            for j in range (0, 7):
                #We do check the invalid combinations as they are disabled and cannot change.
                if self.entry_box[i][j].get() == self.answer_key[i][j]:
                    self.entry_box[i][j]["bg"] = VP_BG_CORRECT
                else:
                    self.entry_box[i][j]["bg"] = VP_BG_WRONG
                    qapla = False
        if qapla:
            print("Qapla'!")
        else:
            print("ghobe'")

    def show_key(self):
        self.clear() #Clear existing information if any.
        self.btn_score_test.config(state="disabled") #We disable the button to submit as this is for reference.
        for i in range(0, 6):
            for j in range (0, 7):
                #We do not insert the invalid combinations, they are set at the window intialization and never changed.
                if self.entry_box[i][j].get() != "---":
                    self.entry_box[i][j].insert(0, self.answer_key[i][j]) #Enter the information from our answer key.
                    self.entry_box[i][j]["bg"] = VP_BG_REF #Shows this is for reference.

    def clear(self):
         self.btn_score_test.config(state="active") #We enable the button to submit as the table is cleared.
         for i in range(0, 6):
            for j in range (0, 7):
                #We do not clear the invalid combination boxes.
                if self.entry_box[i][j].get() != "---":
                    self.entry_box[i][j].delete(0, END) #Clear existing information, if any.
                    self.entry_box[i][j]["bg"] = VP_BG_ENTRY #Clear the background if the user ran a test.
