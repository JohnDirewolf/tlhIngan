from gui import *
from subwindows import *

#----------- APP CLASS - INHERITS WINDOW CLASS AND ADDS THE LEARNING OPTIONS -----------
class App(Window):
    def __init__(self, title, height, width):
        super().__init__(title, height, width)
        self.setup_ui()  # Set up the specific UI elements

    def setup_ui(self):
        self.AddLabel("Klingon Hol Teacher's Aid", 0, 0)
        self.AddButton("Verb Prefix Table", self.show_verb_prefix_table_ref, 1, 0)
        self.AddButton("Verb Prefix Table Test!", self.show_verb_prefix_table_test, 2, 0)

    ## Various learning option functions
    def show_verb_prefix_table_ref(self):
        win_verb_prefix_ref = Window("Verb Prefix Table", 400, 600, self.root)
        verb_prefix_table_ref(win_verb_prefix_ref)
        win_verb_prefix_ref.show_modal()

    def show_verb_prefix_table_test(self):
        win_verb_prefix_test = VerbPrefixTableTest("Verb Prefix Test!", 400, 600, self.root)
        win_verb_prefix_test.show_modal()
    pass

#---------- TEST WINDOW CLASSES ----------
class VerbPrefixTableTest(Window):
    def __init__(self, title, height, width, master):
        super().__init__(title, height, width, master)
        self.rows, self.cols = (6, 7)
        self.entry_box = [["" for j in range(self.cols)] for i in range(self.rows)]
        #self.answers = [["" for j in range(self.cols)] for i in range(self.rows)]
        self.answer_key = [["" for j in range(self.cols)] for i in range(self.rows)]
        self.setup_ui()  # Set up the specific UI elements
        self.set_answer_key()

    def setup_ui(self):
        C_H_BG_COLOR="green"
        C_H_FG_COLOR="red"
        R_H_BG_COLOR="grey"
        R_H_FG_COLOR="blue"
        #BG and FG for the entry boxes is not currently used.
        #ENTRY_BG_COLOR="lightgrey"
        #ENTRY_FG_COLOR="black"
        ENTRY_WIDTH=3 #This sets the width of all all the entry windows.

        # Column Names
        lbl_col_title = self.AddLabel("OBJECT", 0, 0)
        lbl_col_title["fg"] = C_H_BG_COLOR
        lbl_col_title["bg"] = C_H_FG_COLOR
        lbl_col_none = self.AddLabel("none", 0, 1)
        lbl_col_none["fg"] = C_H_BG_COLOR
        lbl_col_none["bg"] = C_H_FG_COLOR
        lbl_col_me = self.AddLabel("me", 0, 2)
        lbl_col_me["fg"] = C_H_BG_COLOR
        lbl_col_me["bg"] = C_H_FG_COLOR
        lbl_col_you = self.AddLabel("you", 0, 3)
        lbl_col_you["fg"] = C_H_BG_COLOR
        lbl_col_you["bg"] = C_H_FG_COLOR
        lbl_col_hhi = self.AddLabel("him/her/it", 0, 4)
        lbl_col_hhi["fg"] = C_H_BG_COLOR
        lbl_col_hhi["bg"] = C_H_FG_COLOR
        lbl_col_us = self.AddLabel("us", 0, 5)
        lbl_col_us["fg"] = C_H_BG_COLOR
        lbl_col_us["bg"] = C_H_FG_COLOR
        lbl_col_youp = self.AddLabel("you (plural)", 0, 6)
        lbl_col_youp["fg"] = C_H_BG_COLOR
        lbl_col_youp["bg"] = C_H_FG_COLOR
        lbl_col_them = self.AddLabel("them", 0, 7)
        lbl_col_them["fg"] = C_H_BG_COLOR
        lbl_col_them["bg"] = C_H_FG_COLOR

        # Rows Names
        lbl_row_title = self.AddLabel("SUBJECT", 1, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR
        lbl_row_title = self.AddLabel("I", 2, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR
        lbl_row_title = self.AddLabel("you", 3, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR
        lbl_row_title = self.AddLabel("he/she/it", 4, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR
        lbl_row_title = self.AddLabel("we", 5, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR
        lbl_row_title = self.AddLabel("you(plural)", 6, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR
        lbl_row_title = self.AddLabel("they", 7, 0)
        lbl_row_title["fg"]=R_H_FG_COLOR
        lbl_row_title["bg"]=R_H_BG_COLOR

        #Set up all our entries
        for i in range(0, 6):
            for j in range (0, 7):
                self.entry_box[i][j] = self.AddEntry(i+2, j+1, width=ENTRY_WIDTH)
    
        #Add Button to submit the test.
        submit_test = self.AddButton("'el: Submit!", self.score_test, 8, 0, col_span=8) 

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
        self.answer_key[4][4] = "cho-"
        self.answer_key[4][5] = "---"
        self.answer_key[4][6] = "bo-"
        self.answer_key[5][0] = "0"
        self.answer_key[5][1] = "mu-"
        self.answer_key[5][2] = "nI-"
        self.answer_key[5][3] = "lu-"
        self.answer_key[5][4] = "nu-"
        self.answer_key[5][5] = "lI-"
        self.answer_key[5][6] = "0"

    # Button functions in sub windows.
    def score_test(self):
        qapla = True

        for i in range(0, 6):
            for j in range (0, 7):
                print(f"self.entry_box[][].get(): {self.entry_box[i][j].get()} , self.answer_key[][]: {self.answer_key[i][j]} ")
                if self.entry_box[i][j].get() == self.answer_key[i][j]:
                    self.entry_box[i][j]["bg"] = "green"
                else:
                    self.entry_box[i][j]["bg"] = "red"
                    qapla = False
 
        if qapla:
            print("Qapla'!")
        else:
            print("ghobe'")


    