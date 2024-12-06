from tkinter import *
from constants import *
import random
import database

#__all__ = ["DevWin", "App", "VerbPrefixTable"]

#----------- UTILITY CLASSES -------------
def SubFrame(parent, row, column, height, width, columnspan=1):
    frm = Frame(parent, relief=FLAT, height=height, width=width, borderwidth=0)
    frm.grid(row=row, column=column, columnspan=columnspan, padx=0, pady=0)
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_propagate(False)
    return frm

#----------- APP CLASS - INHERITS WINDOW CLASS AND ADDS THE LEARNING OPTIONS -----------
class App():
    def __init__(self):
        self.app = Tk()
        self.app.title("tlhIngan Hol ghojmoHwI' boQ")
        self.height = 360
        self.width = 930
        self.app.geometry(f"{self.width}x{self.height}")
        #Master Frame, is the master frame of the window, gives a nice border.
        self.frm_master = None
        # Widgets are a list of a sub frame that positions it and the widget itself. 
        # This allows things like text widgets to just resize around the text but prevents positioning oddities with text sizes.
        # Labels
        self.title = [None, None]
        self.tables = [None, None]
        self.flash_cards = [None, None]
        self.disclaimer = [None, None]
        #Buttons
        self.t_verb_prefix = [None, None]
        self.t_body = [None, None]
        self.t_rlocation = [None, None]
        self.fc_verb_prefix = [None, None]
        self.fc_body = [None, None]
        self.fc_rlocation = [None, None]
        #Radio
        #radio_button1 = tk.Radiobutton(window, text="Option 1", variable=selected_value, value="option1")
        self.fc_prime_lang = StringVar(value=KLINGON)
        self.rdo = None
        self.rdo_english = [None, None]
        self.rdo_klingon = [None, None]

        self.setup_ui()  # Set up the specific UI elements

    def Close(self):
        self.app.destroy()

    def Run(self):
        self.app.mainloop()

    def setup_ui(self):
        self.app.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer raised boarder.
        self.frm_master = Frame(self.app, relief=RIDGE, height=400, width=900, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)
        #self.frm_master["bg"] = "red"
        
        self.title[0] = SubFrame(self.frm_master, 0, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL*3, columnspan=3)
        #self.title[0]["bg"] = "purple"
        self.title[1] = Label(self.title[0], text="Klingon Hol Teacher's Aid")
        self.title[1].grid(sticky="")
        self.title[1].config(font=(APP_TITLE_FONT, APP_TITLE_SIZE, "bold"))
        self.title[1]["fg"] = APP_FG

        #Consider sub frames around the entire tables and flash cards columns to be pretty
        self.tables[0] = SubFrame(self.frm_master, 1, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.tables[0]["bg"] = "yellow"
        self.tables[1] = Label(self.tables[0], text="Tables")
        self.tables[1].grid(sticky="")
        self.tables[1].config(font=(APP_HEADER_FONT, APP_HEADER_SIZE, "bold"))
        self.tables[1]["fg"] = APP_FG

        #Blank frame, all it does is fill the middle cell of the row, this allows this row to define the columns nicely
        SubFrame(self.frm_master, 1, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        
        self.flash_cards[0] = SubFrame(self.frm_master, 1, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.flash_cards[0]["bg"] = "yellow"
        self.flash_cards[1] = Label(self.flash_cards[0], text="Flash Cards")
        self.flash_cards[1].grid(sticky="")
        self.flash_cards[1].config(font=(APP_HEADER_FONT, APP_HEADER_SIZE, "bold"))
        self.flash_cards[1]["fg"] = APP_FG

        #So the buttons line up nicely with the flash cards that have the extra option of primary language, there is a blank two column in row 2
        #SubFrame(self.frm_master, 2, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL*2, columnspan=2)

        self.rdo = SubFrame(self.frm_master, 2, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.rdo["bg"] = "green"
        self.rdo_english[0] = SubFrame(self.rdo, 0, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL/2)
        #self.rdo_english[0]["bg"] = "purple"
        self.rdo_english[1] = Radiobutton(self.rdo_english[0], text="English", variable=self.fc_prime_lang, value=ENGLISH)
        self.rdo_english[1].grid(sticky="")
        self.rdo_klingon[0] = SubFrame(self.rdo, 0, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL/2)
        #self.rdo_klingon[0]["bg"] = "blue"
        self.rdo_klingon[1] = Radiobutton(self.rdo_klingon[0], text="Klingon", variable=self.fc_prime_lang, value=KLINGON)
        self.rdo_klingon[1].grid(sticky="")

        self.t_verb_prefix[0] = SubFrame(self.frm_master, 3, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.t_verb_prefix[0]["bg"] = "green"
        self.t_verb_prefix[1] = Button(self.t_verb_prefix[0], text="Verb Prefix", command=self.show_verb_prefix_table)
        self.t_verb_prefix[1].grid(sticky="")

        self.fc_verb_prefix[0] = SubFrame(self.frm_master, 3, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.fc_verb_prefix[0]["bg"] = "green"
        self.fc_verb_prefix[1] = Button(self.fc_verb_prefix[0], text="Verb Prefix", command=self.show_verb_prefix_cards)
        self.fc_verb_prefix[1].grid(sticky="")

        self.t_body[0] = SubFrame(self.frm_master, 4, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.t_body[0]["bg"] = "orange"
        self.t_body[1] = Button(self.t_body[0], text="Body Parts", command=self.show_body_table)
        self.t_body[1].grid(sticky="")

        self.fc_body[0] = SubFrame(self.frm_master, 4, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.fc_body[0]["bg"] = "orange"
        self.fc_body[1] = Button(self.fc_body[0], text="Body Parts", command=self.show_body_cards)
        self.fc_body[1].grid(sticky="")

        self.t_rlocation[0] = SubFrame(self.frm_master, 5, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.t_rlocation[0]["bg"] = "purple"
        self.t_rlocation[1] = Button(self.t_rlocation[0], text="Relative Locations", command=self.show_rlocation_table)
        self.t_rlocation[1].grid(sticky="")

        self.fc_rlocation[0] = SubFrame(self.frm_master, 5, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        #self.fc_rlocation[0]["bg"] = "purple"
        self.fc_rlocation[1] = Button(self.fc_rlocation[0], text="Relative Locations", command=self.show_rlocation_cards)
        self.fc_rlocation[1].grid(sticky="")

        self.disclaimer[0] = SubFrame(self.frm_master, 6, 0, APP_MINSIZE_ROW*5, APP_MINSIZE_COL*3, columnspan=3)
        #self.disclaimer[0]["bg"] = "green"
        self.disclaimer[1] = Label(self.disclaimer[0], text="""The Klingon language reference used is 'The Klingon Dictionary' by Marc Okrand.\nThis app provides various practice drills to help memorize things like verb prefixes and locations.\nThis app does NOT provide information on pronounciation or grammar.\nAlso this app does not include new additions to the language outside of 'The Klingon Dictionary'.\nTo learn more about this beautiful langauge, see 'The Klingon Dictionary' and other books by Marc Okrand.""")
        self.disclaimer[1].grid(sticky="")
        self.disclaimer[1].config(font=(APP_DISCLAIMER_FONT, APP_DISCLAIMER_SIZE))
        self.disclaimer[1]["fg"] = APP_FG
        
    def show_verb_prefix_table(self):
        VerbPrefixTable(self.app)
    
    def show_body_table(self):
        print("Show Body Table")
        #BodyTable(self.app)

    def show_rlocation_table(self):
        print("Show Relative Location Table")
        #RLocationTable(self.app)

    def show_verb_prefix_cards(self):
        print(f"Prime Language Sent: {self.fc_prime_lang}")
        FlashCards(self.app, "Verb Pronoun Prefixes", VERB_PREFIXES, self.fc_prime_lang.get())
        
    def show_body_cards(self):
        print(f"Show Body Cards, Primary: {self.fc_prime_lang}")
        #FlashCards(self.app, "Body Parts", BODY_PARTS)

    def show_rlocation_cards(self):
        print(f"Show Relative Location Cards, Primary: {self.fc_prime_lang}")
        #FlashCards(self.app, "Relative Locations", REL_LOCATIONS)
    pass

#--------- FLASH CARD CLASS -----------
class FlashCards():
    def __init__(self, master, subtitle, fc_type, fc_prime_lang):
        #Setup of Window
        self.root = Toplevel(master)
        self.my_subtitle = subtitle
        self.my_type = fc_type
        self.my_prime_lang = fc_prime_lang
        self.height = 240
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

        self.klingon = self.fc_load_dict()
        #for word in self.klingon:
        #    print(f"item: {word}")
        self.setup_ui()  # Set up the specific UI elements at start

    def setup_ui(self):
        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer raised boarder.
        self.frm_master = Frame(self.root, relief=RAISED, height=500, width=500, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)

        # Labels and other text widgets will automatically resize for the text within. So we don't fight this, we just let them clamp perfectly on their text.
        # Each label/text Widget has a parent frame to create the cell and then the text Widget can be positioned more cleanly.
        # Weight is added to the sub-grid to enable sticky for postioning.

        self.subtitle[0] = SubFrame(self.frm_master, 0, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL*4, columnspan=4)
        self.my_subtitle = (self.my_subtitle + ": Klingon to English") if self.my_prime_lang == KLINGON else (self.my_subtitle + ": English to Klingon")
        self.subtitle[1] = Label(self.subtitle[0], text=self.my_subtitle)
        self.subtitle[1].grid(sticky="w")
        self.subtitle[1].config(font =(FC_TITLE_FONT, FC_TITLE_SIZE))
        self.subtitle[1]["fg"] = FC_FG
        #self.subtitle[1]["bg"] = FC_BG

        self.word[0] = SubFrame(self.frm_master, 1, 0, FC_MINSIZE_ROW*2, FC_MINSIZE_COL*4, columnspan=4)
        self.word[1] = Label(self.word[0], text="Qapla'!")
        self.word[1].grid(sticky="")
        self.word[1].config(font =(FC_WORD_FONT, FC_WORD_SIZE))
        self.word[1]["fg"] = FC_FG
        #self.word[1]["bg"] = FC_BG

        self.lbl_answer[0] = SubFrame(self.frm_master, 2, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        #This will need to know if we are translating English to Klingon or DIvI' mugh tlhIngan
        self.lbl_answer[1] = Label(self.lbl_answer[0], text="English:")
        self.lbl_answer[1].grid(sticky="")
        self.lbl_answer[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.lbl_answer[1]["fg"] = FC_FG
        #self.lbl_answer[1]["bg"] = FC_BG

        self.entry_answer[0] = SubFrame(self.frm_master, 2, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*3, columnspan=3)
        self.entry_answer[1] = Entry(self.entry_answer[0], relief=SUNKEN, borderwidth=3)
        self.entry_answer[1].grid(sticky="NSEW")
        self.entry_answer[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.entry_answer[1]["fg"] = FC_FG
        self.entry_answer[1]["bg"] = FC_BG

        self.lbl_type[0] = SubFrame(self.frm_master, 3, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        #This may or may not be shown if Type is important or not.
        self.lbl_type[1] = Label(self.lbl_type[0], text="Type:")
        self.lbl_type[1].grid(sticky="")
        self.lbl_type[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.lbl_type[1]["fg"] = FC_FG
        #self.lbl_type[1]["bg"] = FC_BG
        
        self.entry_type[0] = SubFrame(self.frm_master, 3, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*3, columnspan=3)
        self.entry_type[1] = Entry(self.entry_type[0], relief=SUNKEN, borderwidth=3)
        self.entry_type[1].grid(sticky="NSEW")
        self.entry_type[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.entry_type[1]["fg"] = FC_FG
        #self.entry_type[1]["bg"] = FC_BG

        self.prev[0] = SubFrame(self.frm_master, 4, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.prev[1] = Button(self.prev[0], text="< Prev", command=self.cmd_prev, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.prev[1].grid(sticky="")
        self.prev[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.prev[1]["fg"] = FC_FG
        self.prev[1]["bg"] = FC_BG

        self.submit[0] = SubFrame(self.frm_master, 4, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.submit[1] = Button(self.submit[0], text="Submit", command=self.cmd_submit, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.submit[1].grid(sticky="")
        self.submit[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.submit[1]["fg"] = FC_FG
        self.submit[1]["bg"] = FC_BG

        self.show[0] = SubFrame(self.frm_master, 4, 2, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.show[1] = Button(self.show[0], text="Show", command=self.cmd_show, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.show[1].grid(sticky="")
        self.show[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.show[1]["fg"] = FC_FG
        self.show[1]["bg"] = FC_BG

        self.next[0] = SubFrame(self.frm_master, 4, 3, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.next[1] = Button(self.next[0], text="Next >", command=self.cmd_next, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.next[1].grid(sticky="")
        self.next[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.next[1]["fg"] = FC_FG
        self.next[1]["bg"] = FC_BG

        self.close[0] = SubFrame(self.frm_master, 5, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*2, columnspan=2)
        self.close[1] = Button(self.close[0], text="Close", command=self.cmd_close, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.close[1].grid(sticky="")
        self.close[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.close[1]["fg"] = FC_FG
        self.close[1]["bg"] = FC_BG

    def fc_load_dict(self):
        print("Get Type from Dictionary")
        type_dict = database.get_dict_type(self.my_type)
        random.shuffle(type_dict) 
        return type_dict

    def cmd_submit(self):
        print(f"Submit. Answer: {self.entry_answer[1].get()}, Type: {self.entry_type[1].get()}")

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
        self.height = 330
        self.width = 570
        self.root.title("Verb Prefix Table!")
        self.root.geometry(f"{self.width}x{self.height}")
        self.frm_rows, self.frm_cols = (7, 8)
        self.entry_rows, self.entry_cols = (6, 7)
        self.frm_master = None
        #For header labels 0 is the label, 1 is the sub frame, 2 is the label widget 
        self.col_labels = [[None for j in range(self.frm_cols)] for i in range(3)]
        self.row_labels = [[None for j in range(self.frm_rows)] for i in range(3)]
        #entry boxes are an i, j grid of boxes, with h=0 is h=0 subframe, h=1 is the entry box widget
        self.entry_box = [[[None for j in range(self.entry_cols)] for i in range(self.entry_rows)] for h in range(2)]
        self.answer_key = [["" for j in range(self.entry_cols)] for i in range(self.entry_rows)]
        self.btn_show_key = [None, None]
        self.btn_clear = [None, None]
        self.btn_score_test = [None, None]
        self.setup_ui()  # Set up the specific UI elements
        self.set_answer_key()
        self.set_null() #I-me, you-you, I-us etc are NOT VALID for a prefix ("---"), this is NOT the same as 0 for the combination does not have a prefix.

    def setup_ui(self):
        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer ridge boarder.
        self.frm_master = Frame(self.root, relief=RIDGE, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)
        #self.frm_master["bg"] = "yellow"
    
        # Column Names
        self.col_labels[0][0] = "OBJECT"
        self.col_labels[0][1] = "none"
        self.col_labels[0][2] = "me"
        self.col_labels[0][3] = "you"
        self.col_labels[0][4] = "him/\nher/\nit"
        self.col_labels[0][5] = "us"
        self.col_labels[0][6] = "you\nplural"
        self.col_labels[0][7] = "them"
        #Set sub frames, colors and other attributes
        for i in range(self.frm_cols):
            if i == 0:
                self.col_labels[1][0] = SubFrame(self.frm_master, 0, 0, VP_MINSIZE_ROW_0, VP_MINSIZE_COL_0)
            else:
                self.col_labels[1][i] = SubFrame(self.frm_master, 0, i, VP_MINSIZE_ROW, VP_MINSIZE_COL)
            self.col_labels[1][i]["bg"] = VP_COL_HDR_BG
            self.col_labels[2][i] = Label(self.col_labels[1][i], text=self.col_labels[0][i])
            self.col_labels[2][i].grid(row=0, column=0)
            self.col_labels[2][i].config(font =(VP_ALL_HDR_FONT, VP_ALL_HDR_FONT_SIZE))
            self.col_labels[2][i]["fg"] = VP_COL_HDR_FG
            self.col_labels[2][i]["bg"] = VP_COL_HDR_BG

        # Rows Names
        self.row_labels[0][0] = "SUBJECT"
        self.row_labels[0][1] = "I"
        self.row_labels[0][2] = "you"
        self.row_labels[0][3] = "he/she/it"
        self.row_labels[0][4] = "we"
        self.row_labels[0][5] = "you(plural)"
        self.row_labels[0][6] = "they"
        for j in range(self.frm_rows):
            self.row_labels[1][j] = SubFrame(self.frm_master, j+1, 0, VP_MINSIZE_ROW, VP_MINSIZE_COL_0)
            self.row_labels[1][j]["bg"] = VP_COL_HDR_BG
            self.row_labels[2][j] = Label(self.row_labels[1][j], text=self.row_labels[0][j])
            self.row_labels[2][j].grid(row=0, column=0)
            self.row_labels[2][j].config(font =(VP_ALL_HDR_FONT, VP_ALL_HDR_FONT_SIZE))
            self.row_labels[2][j]["fg"] = VP_ROW_HDR_FG
            self.row_labels[2][j]["bg"] = VP_ROW_HDR_BG
        
        #Set up all our entries, there are two less rows and 1 less columns because of the headers.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                self.entry_box[0][i][j] = SubFrame(self.frm_master, i+2, j+1, VP_MINSIZE_ROW, VP_MINSIZE_COL)
                self.entry_box[1][i][j] = Entry(self.entry_box[0][i][j], relief="sunken", width=VP_ENTRY_WIDTH)
                self.entry_box[1][i][j].grid(sticky="")
                self.entry_box[1][i][j].config(font =(VP_FONT, VP_FONT_SIZE))

        #Add Buttons to show answers for study and referenece, a clear button, and a submit test button.
        self.btn_show_key[0] = SubFrame(self.frm_master, 8, 1, VP_MINSIZE_ROW, VP_MINSIZE_COL*3, columnspan=3)
        self.btn_show_key[1] = Button(self.btn_show_key[0], text="moHaq yIcha': Show prefixes!", command=self.show_key)
        self.btn_show_key[1].grid(sticky="")
        
        self.btn_clear[0] = SubFrame(self.frm_master, 8, 5, VP_MINSIZE_ROW, VP_MINSIZE_COL*3, columnspan=3)
        self.btn_clear[1] = Button(self.btn_clear[0], text="wa'chaw yIteq: Clear table!", command=self.clear)
        self.btn_clear[1].grid(sticky="")
        
        self.btn_score_test[0] = SubFrame(self.frm_master, 9, 1, VP_MINSIZE_ROW, VP_MINSIZE_COL, columnspan=7)
        self.btn_score_test[1] = Button(self.btn_score_test[0], text="'el: Submit!", command=self.score_test)
        self.btn_score_test[1].grid(sticky="")

    def set_answer_key(self):
        self.answer_key = database.get_t_verb_prefixes() 
        
    def set_null(self):    
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                if self.answer_key[i][j] == "---":
                    self.entry_box[1][i][j].delete(0, END) #Should not be needed, but just in case.
                    self.entry_box[1][i][j].insert(0, "---")
                    self.entry_box[1][i][j]["bg"] = VP_BG_REF
                    self.entry_box[1][i][j].config(state="disabled") #Disabled so the user cannot change these, kept as boxes, not labels as that is simply cleaner.   

    # Button functions
    def score_test(self):
        qapla = True
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do check the invalid combinations as they are disabled and cannot change.
                if self.entry_box[1][i][j].get() == self.answer_key[i][j]:
                    self.entry_box[1][i][j]["bg"] = VP_BG_CORRECT
                else:
                    self.entry_box[1][i][j]["bg"] = VP_BG_WRONG
                    qapla = False
        if qapla:
            print("Qapla'!")
        else:
            print("ghobe'")

    def show_key(self):
        self.clear() #Clear existing information if any.
        self.btn_score_test[1].config(state="disabled") #We disable the button to submit as this is for reference.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do not insert the invalid combinations, they are set at the window intialization and never changed.
                if self.entry_box[1][i][j].get() != "---":
                    self.entry_box[1][i][j].insert(0, self.answer_key[i][j]) #Enter the information from our answer key.
                    self.entry_box[1][i][j]["bg"] = VP_BG_REF #Shows this is for reference.

    def clear(self):
         self.btn_score_test[1].config(state="active") #We enable the button to submit as the table is cleared.
         for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do not clear the invalid combination boxes.
                if self.entry_box[1][i][j].get() != "---":
                    self.entry_box[1][i][j].delete(0, END) #Clear existing information, if any.
                    self.entry_box[1][i][j]["bg"] = VP_BG_ENTRY #Clear the background if the user ran a test.