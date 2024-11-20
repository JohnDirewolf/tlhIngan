from gui import *
from constants import *

#----------- APP CLASS - INHERITS WINDOW CLASS AND ADDS THE LEARNING OPTIONS -----------
class App(Window):
    def __init__(self, title, height, width):
        super().__init__(title, height, width)
        self.setup_ui()  # Set up the specific UI elements

    def setup_ui(self):
        self.AddLabel("Klingon Hol Teacher's Aid", 0, 0)
        self.AddButton("Verb Prefix Table", self.show_verb_prefix_table, 2, 0)

    def show_verb_prefix_table(self):
        win_verb_prefix_test = VerbPrefixTable("Verb Prefix Test!", 400, 600, self.root)
        win_verb_prefix_test.show_modal()
    pass

#---------- TEST WINDOW CLASSES ----------
class VerbPrefixTable(Window):
    def __init__(self, title, height, width, master):
        super().__init__(title, height, width, master)
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
        ENTRY_WIDTH=3 #This sets the width of all all the entry windows.

        # Column Names
        self.col_labels[0] = self.AddLabel("OBJECT", 0, 0)
        self.col_labels[1] = self.AddLabel("none", 0, 1)
        self.col_labels[2] = self.AddLabel("me", 0, 2)
        self.col_labels[3] = self.AddLabel("you", 0, 3)
        self.col_labels[4] = self.AddLabel("him/her/it", 0, 4)
        self.col_labels[5] = self.AddLabel("us", 0, 5)
        self.col_labels[6] = self.AddLabel("you (plural)", 0, 6)
        self.col_labels[7]= self.AddLabel("them", 0, 7)
        #Set colors and other attributes if needed
        for i in range(self.cols + 1):
            self.col_labels[i]["fg"] = VP_C_H_BG
            self.col_labels[i]["bg"] = VP_C_H_FG

        # Rows Names
        self.row_labels[0] = self.AddLabel("SUBJECT", 1, 0)
        self.row_labels[1] = self.AddLabel("I", 2, 0)
        self.row_labels[2] = self.AddLabel("you", 3, 0)
        self.row_labels[3] = self.AddLabel("he/she/it", 4, 0)
        self.row_labels[4] = self.AddLabel("we", 5, 0)
        self.row_labels[5] = self.AddLabel("you(plural)", 6, 0)
        self.row_labels[6] = self.AddLabel("they", 7, 0)
        for j in range(self.rows + 1):
            self.row_labels[j]["fg"] = VP_R_H_FG
            self.row_labels[j]["bg"] = VP_R_H_BG

        #Set up all our entries
        for i in range(0, self.rows):
            for j in range (0, self.cols):
                self.entry_box[i][j] = self.AddEntry(i+2, j+1, width=ENTRY_WIDTH)
    
        #Add Buttons to show answers for study and referenece, a clear button, and a submit test button.
        self.btn_show_key = self.AddButton("moHaq yIcha': Show prefixes!", self.show_key, 8, 0, col_span=4)
        self.btn_clear = self.AddButton("wa'chaw yIteq: Clear table!", self.clear, 8, 4, col_span=4)
        self.btn_score_test = self.AddButton("'el: Submit!", self.score_test, 9, 0, col_span=8)


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
                    self.entry_box[i][j]["bg"] = VP_CELL_BG_REF
                    self.entry_box[i][j].config(state="disabled") #Disabled so the user cannot change these, kept as boxes, not labels as that is simply cleaner.   

    # Button functions
    def score_test(self):
        qapla = True

        for i in range(0, 6):
            for j in range (0, 7):
                #We do check the invalid combinations as they are disabled and cannot change.
                if self.entry_box[i][j].get() == self.answer_key[i][j]:
                    self.entry_box[i][j]["bg"] = VP_CELL_BG_CORRECT
                else:
                    self.entry_box[i][j]["bg"] = VP_CELL_BG_WRONG
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
                    self.entry_box[i][j]["bg"] = VP_CELL_BG_REF #Shows this is for reference.

    def clear(self):
         self.btn_score_test.config(state="active") #We enable the button to submit as the table is cleared.
         for i in range(0, 6):
            for j in range (0, 7):
                #We do not clear the invalid combination boxes.
                if self.entry_box[i][j].get() != "---":
                    self.entry_box[i][j].delete(0, END) #Clear existing information, if any.
                    self.entry_box[i][j]["bg"] = VP_CELL_BG_ENTRY #Clear the background if the user ran a test.