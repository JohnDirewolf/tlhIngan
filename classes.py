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

def result_popup(parent, title, text):
        parent.protocol("WM_DELETE_WINDOW", lambda: None)
        popup = Toplevel(parent)
        popup.title(title)
        popup.transient(parent)
        frm_popup = Frame(popup, relief=GROOVE, height=180, width=180, borderwidth=5)
        frm_popup.grid(row=0, column=0, padx=10, pady=10)
        lbl_result = Label(frm_popup, text=text, font=("Courier", 24), padx=5, pady=5)
        lbl_result.grid(row=0, column=0, padx=10, pady=(10,5))
        btn_close = Button(frm_popup, text="Close", font=("Courier", 24), padx=5, pady=5, command=popup.destroy, borderwidth=5)
        btn_close.grid(row=1, column=0, padx=10, pady=(5, 10))
        popup.update()
        popup.grab_set_global()
        popup.focus_force()
        parent.wait_window(popup)
        parent.protocol("WM_DELETE_WINDOW", parent.destroy)

#----------- APP CLASS -----------
class App():
    def __init__(self):
        self.app = Tk()
        self.app.title("tlhIngan Hol ghojmoHwI' boQ")
        self.height = 420
        self.width = 1030
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
        self.t_imperative = [None, None]
        self.t_conjunction = [None, None]
        self.fc_verb_prefix = [None, None]
        self.fc_pronoun = [None, None]
        self.fc_body = [None, None]
        self.fc_rlocation = [None, None]
        self.fc_verb = [None, None]
        self.fc_adverb = [None, None]
        self.fc_adjective = [None, None]
        self.fc_people = [None, None]
        self.fc_noun= [None, None]

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
        
        self.title[0] = SubFrame(self.frm_master, 0, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL*5, columnspan=5)
        self.title[1] = Label(self.title[0], text="Klingon Hol Teacher's Aid")
        self.title[1].grid(sticky="")
        self.title[1].config(font=(APP_TITLE_FONT, APP_TITLE_SIZE, "bold"))
        self.title[1]["fg"] = APP_FG

        #Consider sub frames around the entire tables and flash cards columns to be pretty
        
        #TABLES
        self.tables[0] = SubFrame(self.frm_master, 1, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.tables[1] = Label(self.tables[0], text="Tables")
        self.tables[1].grid(sticky="")
        self.tables[1].config(font=(APP_HEADER_FONT, APP_HEADER_SIZE, "bold"))
        self.tables[1]["fg"] = APP_FG

        self.t_verb_prefix[0] = SubFrame(self.frm_master, 3, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.t_verb_prefix[1] = Button(self.t_verb_prefix[0], text="Verb Prefix", width=APP_T_BTN_WIDTH, command=self.show_verb_prefix_table)
        self.t_verb_prefix[1].grid(sticky="")

        self.t_imperative[0] = SubFrame(self.frm_master, 4, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.t_imperative[1] = Button(self.t_imperative[0], text="Imperative Prefix", width=APP_T_BTN_WIDTH, command=self.show_imperative_table)
        self.t_imperative[1].grid(sticky="")

        self.t_conjunction[0] = SubFrame(self.frm_master, 5, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.t_conjunction[1] = Button(self.t_conjunction[0], text="Conjunctions", width=APP_T_BTN_WIDTH, command=self.show_conjunction_table)
        self.t_conjunction[1].grid(sticky="")

        #Blank frame, all it does is fill the middle cell of the row, this allows this row to define the columns nicely
        #SubFrame(self.frm_master, 1, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        
        #FLASH CARDS
        self.flash_cards[0] = SubFrame(self.frm_master, 1, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL*4, columnspan=4)
        self.flash_cards[1] = Label(self.flash_cards[0], text="Flash Cards")
        self.flash_cards[1].grid(sticky="")
        self.flash_cards[1].config(font=(APP_HEADER_FONT, APP_HEADER_SIZE, "bold"))
        self.flash_cards[1]["fg"] = APP_FG

        #Flash Cards need to know if they should show Klingon or English so the user can review the opposite.
        self.rdo = SubFrame(self.frm_master, 2, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL*4, columnspan=4)
        # APP_MINSIZE_COL-(APP_RDO_SPACER/2)
        self.rdo_english[0] = SubFrame(self.rdo, 0, 0, APP_MINSIZE_ROW, APP_MINSIZE_COL*2 - APP_RDO_SPACER)
        self.rdo_english[1] = Radiobutton(self.rdo_english[0], text="English", variable=self.fc_prime_lang, value=ENGLISH)
        self.rdo_english[1].grid(sticky="e")
        SubFrame(self.rdo, 0, 1, APP_MINSIZE_ROW, APP_RDO_SPACER*2 - APP_RDO_FUDGE) #Spacer for the RDOs, it is doubled to make the rdo spaces easier
        self.rdo_klingon[0] = SubFrame(self.rdo, 0, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL*2 - APP_RDO_SPACER + APP_RDO_FUDGE)
        self.rdo_klingon[1] = Radiobutton(self.rdo_klingon[0], text="Klingon", variable=self.fc_prime_lang, value=KLINGON)
        self.rdo_klingon[1].grid(sticky="w")

        self.fc_adverb[0] = SubFrame(self.frm_master, 3, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=ADVERBS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(ADVERBS))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 4, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=ANIMALS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(ANIMALS))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 5, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=BODY_PARTS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(BODY_PARTS))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 6, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=CLOTHING[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(CLOTHING))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 7, 1, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=EPITHETS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(EPITHETS))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 3, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=EXCLAMATIONS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(EXCLAMATIONS))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 4, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=FOOD_DRINK[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(FOOD_DRINK))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 5, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=INVECTIVES[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(INVECTIVES))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 6, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=NOUNS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(NOUNS))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 7, 2, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=NUMBERS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(NUMBERS))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 3, 3, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=PEOPLE[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(PEOPLE))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 4, 3, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=PLACES[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(PLACES))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 5, 3, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=PLANETS_INHABITANTS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(PLANETS_INHABITANTS))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 6, 3, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=PRONOUNS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(PRONOUNS))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 7, 3, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=QUESTIONS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(QUESTIONS))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 3, 4, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=REL_LOCATIONS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(REL_LOCATIONS))
        self.fc_adverb[1].grid(sticky="")

        self.fc_adverb[0] = SubFrame(self.frm_master, 4, 4, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=RELATIONSHIPS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(RELATIONSHIPS))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 5, 4, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=TIME[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(TIME))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 6, 4, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=VERB_TO_BE[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(VERB_TO_BE))
        self.fc_adverb[1].grid(sticky="")  

        self.fc_adverb[0] = SubFrame(self.frm_master, 7, 4, APP_MINSIZE_ROW, APP_MINSIZE_COL)
        self.fc_adverb[1] = Button(self.fc_adverb[0], text=VERBS[1], width=APP_FC_BTN_WIDTH, command=lambda: self.show_cards(VERBS))
        self.fc_adverb[1].grid(sticky="")

        self.disclaimer[0] = SubFrame(self.frm_master, 8, 0, APP_MINSIZE_ROW*5, APP_MINSIZE_COL*5, columnspan=5)
        self.disclaimer[1] = Label(self.disclaimer[0], text="""The Klingon language reference used is 'The Klingon Dictionary' by Marc Okrand.\nThis app provides various practice drills to help memorize things like verb prefixes and locations.\nThis app does NOT provide information on pronounciation or grammar.\nAlso this app does not include new additions to the language outside of 'The Klingon Dictionary'.\nTo learn more about this beautiful langauge, see 'The Klingon Dictionary' and other books by Marc Okrand.""")
        self.disclaimer[1].grid(sticky="")
        self.disclaimer[1].config(font=(APP_DISCLAIMER_FONT, APP_DISCLAIMER_SIZE))
        self.disclaimer[1]["fg"] = APP_FG
        
    def show_verb_prefix_table(self):
        VerbPrefixTable(self.app)
    
    def show_imperative_table(self):
        ImperativePrefixTable(self.app)

    def show_conjunction_table(self):
        ConjunctionTable(self.app)

    def show_cards(self, card_type):
        FlashCards(self.app, card_type, self.fc_prime_lang.get())

#--------- FLASH CARD CLASS -----------
class FlashCards():
    def __init__(self, master, fc_type, fc_prime_lang):
        #Setup of Window
        self.root = Toplevel(master)
        self.my_type = fc_type[0]
        self.my_prime_lang = fc_prime_lang
        self.my_to_lang = KLINGON if self.my_prime_lang == ENGLISH else ENGLISH
        self.my_subtitle = fc_type[1] + ": " + self.my_prime_lang + " to " + self.my_to_lang
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
        self.word_text = StringVar(value="")
        self.lbl_answer = [None, None]
        self.answer = [None, None]
        self.answer_text = StringVar(value="")
        self.lbl_type = [None, None]
        self.type = [None, None]
        self.type_text = StringVar(value="")
        self.type_needed = False
        self.submit = [None, None]
        self.show = [None, None]
        self.next = [None, None]
        self.prev = [None, None]
        self.close = [None, None]

        self.klingon = ""
        self.cur_word = 0
        self.setup_ui()  # Set up the specific UI elements at start

    def setup_ui(self):
        self.klingon = database.get_klingon_type(self.my_type)
        random.shuffle(self.klingon)

        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer raised boarder.
        self.frm_master = Frame(self.root, relief=GROOVE, height=500, width=500, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)

        # Labels and other text widgets will automatically resize for the text within. So we don't fight this, we just let them clamp perfectly on their text.
        # Each label/text Widget has a parent frame to create the cell and then the text Widget can be positioned more cleanly.
        # Weight is added to the sub-grid to enable sticky for postioning.

        self.subtitle[0] = SubFrame(self.frm_master, 0, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL*4, columnspan=4)
        self.subtitle[1] = Label(self.subtitle[0], text=self.my_subtitle)
        self.subtitle[1].grid(sticky="w")
        self.subtitle[1].config(font =(FC_TITLE_FONT, FC_TITLE_SIZE))
        self.subtitle[1]["fg"] = FC_FG

        self.word[0] = SubFrame(self.frm_master, 1, 0, FC_MINSIZE_ROW*2, FC_MINSIZE_COL*4, columnspan=4)
        self.word[1] = Label(self.word[0], textvariable=self.word_text)
        self.word[1].grid(sticky="")
        self.word[1].config(font =(FC_WORD_FONT, FC_WORD_SIZE))
        self.word[1]["fg"] = FC_FG
        self.load_word()
        
        self.lbl_answer[0] = SubFrame(self.frm_master, 2, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.lbl_answer[1] = Label(self.lbl_answer[0], text=(self.my_to_lang + ":"))
        self.lbl_answer[1].grid(sticky="")
        self.lbl_answer[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.lbl_answer[1]["fg"] = FC_FG

        self.answer[0] = SubFrame(self.frm_master, 2, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*3, columnspan=3)
        self.answer[0].config(relief="sunken", borderwidth=3)
        self.answer[1] = Label(self.answer[0], textvariable=self.answer_text, borderwidth=3)
        self.answer[1].grid(sticky="W")
        self.answer[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.answer[1]["fg"] = FC_FG

        self.lbl_type[0] = SubFrame(self.frm_master, 3, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.lbl_type[1] = Label(self.lbl_type[0], text="Type:")
        #Type is invisible if not needed.
        if self.type_needed:
            self.lbl_type[1].grid(sticky="")
        else:
            self.lbl_type[1].grid_forget()
        self.lbl_type[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.lbl_type[1]["fg"] = FC_FG
        self.lbl_type[1]["bg"] = FC_BG

        self.type[0] = SubFrame(self.frm_master, 3, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*3, columnspan=3)
        self.type[1] = Label(self.type[0], textvariable=self.type_text, relief=SUNKEN, borderwidth=3)
        #Type is invisible if not needed
        if self.type_needed:
            self.type[1].grid(sticky="NSEW")
        else:
            self.type[1].grid_forget()
        self.type[1].config(font =(FC_ENTRY_FONT, FC_ENTRY_SIZE))
        self.type[1]["fg"] = FC_FG
        self.type[1]["bg"] = FC_BG
        self.clear_type()

        self.prev[0] = SubFrame(self.frm_master, 4, 0, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.prev[1] = Button(self.prev[0], text="< Prev", command=self.cmd_prev, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.prev[1].grid(sticky="")
        self.prev[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.prev[1]["fg"] = FC_FG
        
        self.show[0] = SubFrame(self.frm_master, 4, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*2, columnspan=2)
        self.show[1] = Button(self.show[0], text="Show", command=self.cmd_show, width=((FC_MINSIZE_COL*2)-20), height=FC_MINSIZE_ROW-10)
        self.show[1].grid(sticky="")
        self.show[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.show[1]["fg"] = FC_FG
        
        self.next[0] = SubFrame(self.frm_master, 4, 3, FC_MINSIZE_ROW, FC_MINSIZE_COL)
        self.next[1] = Button(self.next[0], text="Next >", command=self.cmd_next, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.next[1].grid(sticky="")
        self.next[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.next[1]["fg"] = FC_FG
        
        self.close[0] = SubFrame(self.frm_master, 5, 1, FC_MINSIZE_ROW, FC_MINSIZE_COL*2, columnspan=2)
        self.close[1] = Button(self.close[0], text="Close", command=self.cmd_close, width=FC_MINSIZE_COL-20, height=FC_MINSIZE_ROW-10)
        self.close[1].grid(sticky="")
        self.close[1].config(font =(FC_BTN_FONT, FC_BTN_SIZE))
        self.close[1]["fg"] = FC_FG
        
    def clear_answer(self):
        self.answer_text.set("")

    def clear_type(self):
        self.type_text.set("")

    def load_word(self):
        self.clear_answer()
        self.clear_type()
        self.word_text.set(self.klingon[self.cur_word][self.my_prime_lang])
    
    def load_answer(self):
        self.answer_text.set(self.klingon[self.cur_word][self.my_to_lang])

    def cmd_show(self):
        self.answer_text.set(self.klingon[self.cur_word][self.my_to_lang])
        if self.type_needed:
            self.type_text.set(self.klingon[self.cur_word][TYPE])
    
    def cmd_next(self):
        if self.cur_word == len(self.klingon) - 1:
            self.cur_word = 0
        else:
            self.cur_word += 1
        self.load_word()

    def cmd_prev(self):
        if self.cur_word == 0:
            self.cur_word = len(self.klingon) - 1
        else:
            self.cur_word -= 1
        self.load_word()

    def cmd_close(self):
        self.root.destroy()

#---------- TABLE TEST CLASSES ----------
class VerbPrefixTable():
    def __init__(self, master):
        self.root = Toplevel(master)
        self.height = (VP_MINSIZE_ROW_0 + (VP_MINSIZE_ROW*9) + 30)
        self.width = (VP_MINSIZE_COL_0 + (VP_MINSIZE_COL*7) + 30)
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
        #dict, 0 Col Headers, 1 Row Headers, 2 Answer Key
        self.dict = database.get_tables_type(VERB_BASIC_PREFIXES)
        self.setup_ui()  # Set up the specific UI elements
        self.set_answer_key()
        self.set_null() #I-me, you-you, I-us etc are NOT VALID for a prefix ("---"), this is NOT the same as 0 for combinations do not have a prefix.

    def setup_ui(self):
        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer ridge boarder.
        self.frm_master = Frame(self.root, relief=RIDGE, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)
    
        # Column Names
        self.col_labels[0] = self.dict[0] 
        #Set sub frames, colors and other attributes
        for i in range(self.frm_cols):
            if i == 0:
                self.col_labels[1][0] = SubFrame(self.frm_master, 0, 0, VP_MINSIZE_ROW_0, VP_MINSIZE_COL_0)
            else:
                self.col_labels[1][i] = SubFrame(self.frm_master, 0, i, VP_MINSIZE_ROW_0, VP_MINSIZE_COL)
            self.col_labels[1][i]["bg"] = VP_COL_HDR_BG
            self.col_labels[2][i] = Label(self.col_labels[1][i], text=self.col_labels[0][i])
            self.col_labels[2][i].grid(row=0, column=0)
            self.col_labels[2][i].config(font =(VP_ALL_HDR_FONT, VP_ALL_HDR_FONT_SIZE))
            self.col_labels[2][i]["fg"] = VP_COL_HDR_FG
            self.col_labels[2][i]["bg"] = VP_COL_HDR_BG

        # Rows Names
        self.row_labels[0] = self.dict[1] 
        for j in range(self.frm_rows):
            self.row_labels[1][j] = SubFrame(self.frm_master, j+1, 0, VP_MINSIZE_ROW, VP_MINSIZE_COL_0)
            self.row_labels[1][j]["bg"] = VP_COL_HDR_BG
            self.row_labels[2][j] = Label(self.row_labels[1][j], text=self.row_labels[0][j])
            self.row_labels[2][j].grid(row=0, column=0)
            self.row_labels[2][j].config(font =(VP_ALL_HDR_FONT, VP_ALL_HDR_FONT_SIZE))
            self.row_labels[2][j]["fg"] = VP_ROW_HDR_FG
            self.row_labels[2][j]["bg"] = VP_ROW_HDR_BG
        
        #Set up all our entries, grid position needs to take into account two row and 1 column difference.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                self.entry_box[0][i][j] = SubFrame(self.frm_master, i+2, j+1, VP_MINSIZE_ROW, VP_MINSIZE_COL)
                self.entry_box[1][i][j] = Entry(self.entry_box[0][i][j], relief="sunken", width=VP_ENTRY_WIDTH)
                self.entry_box[1][i][j].grid(sticky="")
                self.entry_box[1][i][j].config(font =(VP_FONT, VP_FONT_SIZE))

        #Add Buttons to show answers for study and referenece, a clear button, and a submit test button.
        self.btn_show_key[0] = SubFrame(self.frm_master, 8, 0, VP_MINSIZE_ROW, (VP_MINSIZE_COL_0 + (VP_MINSIZE_COL*2)), columnspan=3)
        self.btn_show_key[1] = Button(self.btn_show_key[0], text="yIcha': Show!", command=self.show_key)
        self.btn_show_key[1].grid(sticky="")
        
        self.btn_clear[0] = SubFrame(self.frm_master, 8, 4, VP_MINSIZE_ROW, VP_MINSIZE_COL*4, columnspan=4)
        self.btn_clear[1] = Button(self.btn_clear[0], text="yIteq: Clear!", command=self.clear)
        self.btn_clear[1].grid(sticky="")
        
        self.btn_score_test[0] = SubFrame(self.frm_master, 9, 2, VP_MINSIZE_ROW, VP_MINSIZE_COL*3, columnspan=3)
        self.btn_score_test[1] = Button(self.btn_score_test[0], text="'el: Submit!", command=self.score_test)
        self.btn_score_test[1].grid(sticky="")

    def set_answer_key(self):
        self.answer_key = self.dict[2] 
        
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
                    self.entry_box[1][i][j]["bg"] = T_BG_CORRECT
                else:
                    self.entry_box[1][i][j]["bg"] = T_BG_WRONG
                    qapla = False
        if qapla:
            result_popup(self.root, "Success", "Qapla'!")
        else:
            result_popup(self.root, "Failure", "ghobe'!")

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

class ImperativePrefixTable():
    def __init__(self, master):
        self.root = Toplevel(master)
        self.height = (IP_MINSIZE_ROW_0 + ((IP_MINSIZE_ROW*4) + 30))
        self.width = (IP_MINSIZE_COL_0 + ((IP_MINSIZE_COL*5) + 30))
        self.root.title("Verb Prefix Table!")
        self.root.geometry(f"{self.width}x{self.height}")
        self.frm_rows, self.frm_cols = (2, 6)
        self.entry_rows, self.entry_cols = (2, 5)
        self.frm_master = None
        #For header labels 0 is the label, 1 is the sub frame, 2 is the label widget 
        self.col_labels = [[None for j in range(self.frm_cols)] for i in range(3)]
        self.row_labels = [[None for j in range(self.frm_rows)] for i in range(3)]
        self.entry_box = [[[None for j in range(self.entry_cols)] for i in range(self.entry_rows)] for h in range(2)]
        self.answer_key = [["" for j in range(self.entry_cols)] for i in range(self.entry_rows)]
        self.btn_show_key = [None, None]
        self.btn_clear = [None, None]
        self.btn_score_test = [None, None]
        #dict, 0 Col Headers, 1 Row Headers, 2 Answer Key
        self.dict = database.get_tables_type(VERB_IMPERATIVES_PREFIXES)
        self.setup_ui()  # Set up the specific UI elements
        self.set_answer_key()

    def setup_ui(self):
        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer ridge boarder.
        self.frm_master = Frame(self.root, relief=RIDGE, borderwidth=5, width=(IP_MINSIZE_COL_0 + (IP_MINSIZE_COL*6)), height=(IP_MINSIZE_ROW_0 + (IP_MINSIZE_ROW*3)))
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)

        # Column Names
        self.col_labels[0] = self.dict[0] 
        #Set sub frames, colors and other attributes
        for i in range(self.frm_cols):
            if i == 0:
                self.col_labels[1][0] = SubFrame(self.frm_master, 0, 0, IP_MINSIZE_ROW_0, IP_MINSIZE_COL_0)
            else:
                self.col_labels[1][i] = SubFrame(self.frm_master, 0, i, IP_MINSIZE_ROW_0, IP_MINSIZE_COL)
            self.col_labels[1][i]["bg"] = IP_COL_HDR_BG
            self.col_labels[2][i] = Label(self.col_labels[1][i], text=self.col_labels[0][i])
            self.col_labels[2][i].grid(row=0, column=0)
            self.col_labels[2][i].config(font =(IP_ALL_HDR_FONT, IP_ALL_HDR_FONT_SIZE))
            self.col_labels[2][i]["fg"] = IP_COL_HDR_FG
            self.col_labels[2][i]["bg"] = IP_COL_HDR_BG

        # Rows Names
        self.row_labels[0] = self.dict[1] 
        for j in range(self.frm_rows):
            self.row_labels[1][j] = SubFrame(self.frm_master, j+1, 0, IP_MINSIZE_ROW, IP_MINSIZE_COL_0)
            self.row_labels[1][j]["bg"] = IP_COL_HDR_BG
            self.row_labels[2][j] = Label(self.row_labels[1][j], text=self.row_labels[0][j])
            self.row_labels[2][j].grid(row=0, column=0)
            self.row_labels[2][j].config(font =(IP_ALL_HDR_FONT, IP_ALL_HDR_FONT_SIZE))
            self.row_labels[2][j]["fg"] = IP_ROW_HDR_FG
            self.row_labels[2][j]["bg"] = IP_ROW_HDR_BG

        #Set up all our entries, there is a one row and one column offset.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                self.entry_box[0][i][j] = SubFrame(self.frm_master, i+1, j+1, IP_MINSIZE_ROW, IP_MINSIZE_COL)
                self.entry_box[1][i][j] = Entry(self.entry_box[0][i][j], relief="sunken", width=IP_ENTRY_WIDTH)
                self.entry_box[1][i][j].grid(sticky="")
                self.entry_box[1][i][j].config(font =(IP_FONT, IP_FONT_SIZE))

        #Add Buttons to show answers for study and referenece, a clear button, and a submit test button.
        self.btn_show_key[0] = SubFrame(self.frm_master, 4, 0, IP_MINSIZE_ROW, (IP_MINSIZE_COL_0 + IP_MINSIZE_COL), columnspan=2)
        self.btn_show_key[1] = Button(self.btn_show_key[0], text="yIcha': Show", command=self.show_key)
        self.btn_show_key[1].grid(sticky="")
        
        self.btn_clear[0] = SubFrame(self.frm_master, 4, 3, IP_MINSIZE_ROW, IP_MINSIZE_COL*3, columnspan=3)
        self.btn_clear[1] = Button(self.btn_clear[0], text="yIteq: Clear", command=self.clear)
        self.btn_clear[1].grid(sticky="")
        
        self.btn_score_test[0] = SubFrame(self.frm_master, 5, 1, IP_MINSIZE_ROW, IP_MINSIZE_COL*3, columnspan=3)
        self.btn_score_test[1] = Button(self.btn_score_test[0], text="'el: Submit", command=self.score_test)
        self.btn_score_test[1].grid(sticky="")
    
    def set_answer_key(self):
        self.answer_key = self.dict[2] 

    # Button functions
    def score_test(self):
        qapla = True
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do check the invalid combinations as they are disabled and cannot change.
                if self.entry_box[1][i][j].get() == self.answer_key[i][j]:
                    self.entry_box[1][i][j]["bg"] = T_BG_CORRECT
                else:
                    self.entry_box[1][i][j]["bg"] = T_BG_WRONG
                    qapla = False
        if qapla:
            result_popup(self.root, "Success", "Qapla'!")
        else:
            result_popup(self.root, "Failure", "ghobe'!")

    def show_key(self):
        self.clear() #Clear existing information if any.
        self.btn_score_test[1].config(state="disabled") #We disable the button to submit as this is for reference.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do not insert the invalid combinations, they are set at the window intialization and never changed.
                self.entry_box[1][i][j].insert(0, self.answer_key[i][j]) #Enter the information from our answer key.
                self.entry_box[1][i][j]["bg"] = IP_BG_REF #Shows this is for reference.

    def clear(self):
         self.btn_score_test[1].config(state="active") #We enable the button to submit as the table is cleared.
         for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                self.entry_box[1][i][j].delete(0, END) #Clear existing information, if any.
                self.entry_box[1][i][j]["bg"] = IP_BG_ENTRY #Clear the background if the user ran a test.

class ConjunctionTable():
    def __init__(self, master):
        self.root = Toplevel(master)
        self.height = (C_MINSIZE_ROW*8)
        self.width = (C_MINSIZE_COL*3 + 30)
        self.root.title("Conjunction Table!")
        self.root.geometry(f"{self.width}x{self.height}")
        self.frm_rows, self.frm_cols = (3, 3)
        self.entry_rows, self.entry_cols = (3, 2)
        self.frm_master = None
        #For header labels 0 is the label, 1 is the sub frame, 2 is the label widget 
        self.col_labels = [[None for j in range(self.frm_cols)] for i in range(3)]
        self.row_labels = [[None for j in range(self.frm_rows)] for i in range(3)]
        self.entry_box = [[[None for j in range(self.entry_cols)] for i in range(self.entry_rows)] for h in range(2)]
        self.answer_key = [["" for j in range(self.entry_cols)] for i in range(self.entry_rows)]
        self.btn_show_key = [None, None]
        self.btn_clear = [None, None]
        self.btn_score_test = [None, None]
        #dict, 0 Col Headers, 1 Row Headers, 2 Answer Key
        self.dict = database.get_tables_type(CONJUNCTIONS)
        self.setup_ui()  # Set up the specific UI elements
        self.set_answer_key()

    def setup_ui(self):   
        self.root.resizable(width=False, height=False)
        
        #Master Frame - gives a nice outer ridge boarder.
        self.frm_master = Frame(self.root, relief=RIDGE, borderwidth=5)
        self.frm_master.grid(row=0, column=0, padx=10, pady=10)
    
        # Column Names
        self.col_labels[0] = self.dict[0] 
        #Set sub frames, colors and other attributes
        for i in range(self.frm_cols):
            self.col_labels[1][i] = SubFrame(self.frm_master, 0, i, C_MINSIZE_ROW*2, C_MINSIZE_COL)
            self.col_labels[1][i]["bg"] = C_COL_HDR_BG
            self.col_labels[2][i] = Label(self.col_labels[1][i], text=self.col_labels[0][i])
            self.col_labels[2][i].grid(row=0, column=0)
            self.col_labels[2][i].config(font =(C_ALL_HDR_FONT, C_ALL_HDR_FONT_SIZE))
            self.col_labels[2][i]["fg"] = C_COL_HDR_FG
            self.col_labels[2][i]["bg"] = C_COL_HDR_BG

        # Rows Names
        self.row_labels[0] = self.dict[1] 
        for j in range(self.frm_rows):
            self.row_labels[1][j] = SubFrame(self.frm_master, j+1, 2, C_MINSIZE_ROW, C_MINSIZE_COL)
            self.row_labels[1][j]["bg"] = C_COL_HDR_BG
            self.row_labels[2][j] = Label(self.row_labels[1][j], text=self.row_labels[0][j])
            self.row_labels[2][j].grid(row=0, column=0, sticky="w")
            self.row_labels[2][j].config(font =(C_ALL_HDR_FONT, C_ALL_HDR_FONT_SIZE))
            self.row_labels[2][j]["fg"] = C_ROW_HDR_FG
            self.row_labels[2][j]["bg"] = C_ROW_HDR_BG
        
        #Set up all our entries, grid position needs to take into account two row and 1 column difference.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                self.entry_box[0][i][j] = SubFrame(self.frm_master, i+1, j, C_MINSIZE_ROW, C_MINSIZE_COL)
                self.entry_box[1][i][j] = Entry(self.entry_box[0][i][j], relief="sunken", width=C_ENTRY_WIDTH)
                self.entry_box[1][i][j].grid(sticky="")
                self.entry_box[1][i][j].config(font =(C_FONT, C_FONT_SIZE))

        #Add Buttons to show answers for study and referenece, a clear button, and a submit test button.
        self.btn_show_key[0] = SubFrame(self.frm_master, 4, 0, C_MINSIZE_ROW, C_MINSIZE_COL)
        self.btn_show_key[1] = Button(self.btn_show_key[0], text="yIcha': Show!", command=self.show_key)
        self.btn_show_key[1].grid(sticky="")
        
        self.btn_clear[0] = SubFrame(self.frm_master, 4, 2, C_MINSIZE_ROW, C_MINSIZE_COL)
        self.btn_clear[1] = Button(self.btn_clear[0], text="yIteq: Clear!", command=self.clear)
        self.btn_clear[1].grid(sticky="")
        
        self.btn_score_test[0] = SubFrame(self.frm_master, 5, 1, C_MINSIZE_ROW, C_MINSIZE_COL)
        self.btn_score_test[1] = Button(self.btn_score_test[0], text="'el: Submit!", command=self.score_test)
        self.btn_score_test[1].grid(sticky="")

    def set_answer_key(self):
        self.answer_key = self.dict[2] 

    # Button functions
    def score_test(self):
        qapla = True
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do check the invalid combinations as they are disabled and cannot change.
                if self.entry_box[1][i][j].get() == self.answer_key[i][j]:
                    self.entry_box[1][i][j]["bg"] = T_BG_CORRECT
                else:
                    self.entry_box[1][i][j]["bg"] = T_BG_WRONG
                    qapla = False
        if qapla:
            result_popup(self.root, "Success", "Qapla'!")
        else:
            result_popup(self.root, "Failure", "ghobe'!")

    def show_key(self):
        self.clear() #Clear existing information if any.
        self.btn_score_test[1].config(state="disabled") #We disable the button to submit as this is for reference.
        for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                #We do not insert the invalid combinations, they are set at the window intialization and never changed.
                self.entry_box[1][i][j].insert(0, self.answer_key[i][j]) #Enter the information from our answer key.
                self.entry_box[1][i][j]["bg"] = C_BG_REF #Shows this is for reference.

    def clear(self):
         self.btn_score_test[1].config(state="active") #We enable the button to submit as the table is cleared.
         for i in range(0, self.entry_rows):
            for j in range (0, self.entry_cols):
                self.entry_box[1][i][j].delete(0, END) #Clear existing information, if any.
                self.entry_box[1][i][j]["bg"] = C_BG_ENTRY #Clear the background if the user ran a test.
