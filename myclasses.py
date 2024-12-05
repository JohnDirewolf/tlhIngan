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
        for word in self.klingon:
            print(f"item: {word}")
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

        self.subtitle[0] = SubFrame(self.frm_master, 0, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL*4, columnspan=4)
        print(f"Pre-Check: {self.my_subtitle}")
        self.my_subtitle = (self.my_subtitle + ": Klingon to English") if self.my_prime_lang == KLINGON else (self.my_subtitle + ": English to Klingon")
        print(f"Post-Check: {self.my_subtitle}")   
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

        self.submit[0] = SubFrame(self.frm_master, 4, 1, FC_MINSIZE_ROW, width=FC_MINSIZE_COL)
        self.submit[1] = Button(self.submit[0], text="Submit", command=self.cmd_submit, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.submit[1].grid(sticky="")
        self.submit[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.submit[1]["fg"] = FC_FG
        self.submit[1]["bg"] = FC_BG

        self.show[0] = SubFrame(self.frm_master, 4, 2, FC_MINSIZE_ROW, width=FC_MINSIZE_COL)
        self.show[1] = Button(self.show[0], text="Show", command=self.cmd_show, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.show[1].grid(sticky="")
        self.show[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.show[1]["fg"] = FC_FG
        self.show[1]["bg"] = FC_BG

        self.next[0] = SubFrame(self.frm_master, 4, 3, FC_MINSIZE_ROW, width=FC_MINSIZE_COL)
        self.next[1] = Button(self.next[0], text="Next >", command=self.cmd_next, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.next[1].grid(sticky="")
        self.next[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.next[1]["fg"] = FC_FG
        self.next[1]["bg"] = FC_BG

        self.close[0] = SubFrame(self.frm_master, 5, 1, FC_MINSIZE_ROW, width=FC_MINSIZE_COL*2, columnspan=2)
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
