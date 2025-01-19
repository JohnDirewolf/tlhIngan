#Language
ENGLISH = "English"
KLINGON = "Klingon"
TYPE = "Type"

#Word Types
ADVERBS = ["adverbs", "Adverbs"]
ANIMALS = ["animals", "Animals"]
BODY_PARTS = ["body_parts", "Body Parts"]
CLOTHING = ["clothing", "Clothing"]
CONJUNCTIONS = ["conjunctions", "Conjunctions"]
EPITHETS = ["epithets", "Epithets"]
EXCLAMATIONS = ["exclamations", "Exclamations"]
FOOD_DRINK = ["food_drink", "Food & Drink"]
INVECTIVES = ["invectives", "Invectives"]
NOUNS = ["nouns", "Nouns"]
NUMBERS = ["numbers", "Numbers"]
PEOPLE = ["people", "People"]
PLACES = ["places", "Places"]
PLANETS_INHABITANTS = ["planets_inhabitants", "Planets & Inhabitants"]
PRONOUNS = ["pronouns", "Pronouns"]
QUESTIONS = ["questions", "Questions"]
REL_LOCATIONS = ["relative_locations", "Locatives"]
RELATIONSHIPS = ["relationships", "Relationships"]
TIME = ["time", "Time"]
VERB_BASIC_PREFIXES = ["verb_basic_prefixes", "Pronominal Prefixes"]
VERB_IMPERATIVES_PREFIXES = ["verb_imperatives_prefixes", "Imperatives Prefixes"]
VERB_TO_BE = ["verb_to_be", "To Be Verbs"]
VERBS = ["verbs", "Verbs"]
#Affixes
NOUN_SUFFIXES = "noun_suffixes"
PRONOMINAL_PREFIXES = "pronominal_prefixes"
VERB_SUFFIXES = "verb_suffixes"
NUMBER_SUFFIXES = "number_suffixes"
#Affix Types
N_AUGMENTATIVE_DIMINUTIVE = 1
N_NUMBER = 2
N_QUALIFICATION = 3
N_POSSESSION_SPECIFICATION = 4
N_SYNTACTIC = 5

V_BASIC = 0
V_IMPERATIVE = -1
V_ONESELF_ONE_ANOTHER = 1
V_VOLITION_PREDISPOSITION = 2
V_CHANGE = 3
V_CAUSE = 4
V_INDEFINITE_SUBJECT_ABILITY = 5
V_QUALIFICATION = 6
V_ASPECT = 7
V_HONORIFIC = 8
V_SYNTATIC = 9
V_ROVER = 0

NUM_SUFFIXES = 0

#App Constants
APP_MINSIZE_ROW = 30
APP_MINSIZE_COL = 200
APP_T_BTN_WIDTH = 15
APP_FC_BTN_WIDTH = 15
APP_RDO_SPACER = 30
APP_RDO_FUDGE = 15 # While the SPACER match is all technically correct the way that rdo buttons are generated need some fudge to feel correct
#App Colors
APP_FG = "black"
#App Fonts
APP_TITLE_FONT = "Arial"
APP_TITLE_SIZE = 12
APP_HEADER_FONT = "Times New Roman"
APP_HEADER_SIZE = 12
APP_DISCLAIMER_FONT = "Courier"
APP_DISCLAIMER_SIZE = 10

# Verb Prefix Table Constants
VP_ENTRY_WIDTH=4 #This sets the width of all all the entry windows.
#Set the Grid to be of consistent height and width.
VP_MINSIZE_COL_0 = 120
VP_MINSIZE_COL = 60
VP_MINSIZE_ROW_0 = 60
VP_MINSIZE_ROW = 30
#Verb Prefix Table Colors
VP_COL_HDR_FG="purple"
VP_COL_HDR_BG="grey"
VP_ROW_HDR_FG="blue"
VP_ROW_HDR_BG="grey"
VP_FG="black"
VP_BG_REF="lightgrey"
VP_BG_ENTRY="white"
#Verb Previx Table Fonts
VP_ALL_HDR_FONT = "Courier"
VP_ALL_HDR_FONT_SIZE = 12
VP_FONT = "Courier"
VP_FONT_SIZE = 12

#Verb Suffix Type Table Contants
VST_MINSIZE_COL = 30
VST_MINSIZE_ROW = 30 

# Imperative Prefix Table Constants
IP_ENTRY_WIDTH=4 #This sets the width of all all the entry windows.
#Set the Grid to be of consistent height and width.
IP_MINSIZE_COL_0 = 120
IP_MINSIZE_COL = 60
IP_MINSIZE_ROW_0 = 60
IP_MINSIZE_ROW = 30
#Verb Prefix Table Colors
IP_COL_HDR_FG="purple"
IP_COL_HDR_BG="grey"
IP_ROW_HDR_FG="blue"
IP_ROW_HDR_BG="grey"
IP_FG="black"
IP_BG_REF="lightgrey"
IP_BG_ENTRY="white"
#Imperative Previx Table Fonts
IP_ALL_HDR_FONT = "Courier"
IP_ALL_HDR_FONT_SIZE = 12
IP_FONT = "Courier"
IP_FONT_SIZE = 12

# Conjunction Table Constants
C_ENTRY_WIDTH=5 #This sets the width of all all the entry windows.
#Set the Grid to be of consistent height and width.
C_MINSIZE_COL = 120
C_MINSIZE_ROW = 30
#Verb Prefix Table Colors
C_COL_HDR_FG="purple"
C_COL_HDR_BG="grey"
C_ROW_HDR_FG="blue"
C_ROW_HDR_BG="grey"
C_FG="black"
C_BG_REF="lightgrey"
C_BG_ENTRY="white"
#Imperative Previx Table Fonts
C_ALL_HDR_FONT = "Courier"
C_ALL_HDR_FONT_SIZE = 12
C_FONT = "Courier"
C_FONT_SIZE = 12

#General Table Constants
T_BG_CORRECT = "lightgreen"
T_BG_WRONG = "pink"

#Flash Card Constants.
#Set the Grid to be of consistent height and width.
FC_MINSIZE_COL = 120
FC_MINSIZE_ROW = 30
#Flash Card Colors
FC_FG = "black"
FC_BG = "grey"
#Flash Card Font
FC_WORD_FONT = "Times New Roman"
FC_WORD_SIZE = 28
FC_TITLE_FONT = "Courier"
FC_TITLE_SIZE = 10
FC_ENTRY_FONT = "Times New Roman"
FC_ENTRY_SIZE = 10
FC_BTN_FONT = "Courier"
FC_BTN_SIZE = 10