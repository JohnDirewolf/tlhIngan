#Database
#This program stores the klingon reference in a dictionary saved to a JSON file
#This is set as as seperate module in case in future we want to actually implmement a full database interface.

import json
from constants import *

#{ENGLISH: "", KLINGON: ""}
#{ENGLISH: "", KLINGON: "", TYPE: ""}

_klingon_dict = {
    VERBS: [
        {ENGLISH: "run", KLINGON: "qet"},
        {ENGLISH: "walk", KLINGON: "yIt"},
        {ENGLISH: "jump", KLINGON: "Sup"},
        {ENGLISH: "eat", KLINGON: "Sop"},
        {ENGLISH: "breathe", KLINGON: "tlhuH"},
        {ENGLISH: "kill", KLINGON: "HoH"},
        {ENGLISH: "trust", KLINGON: "voq"},
        {ENGLISH: "drink", KLINGON: "tlhutlh"},
        {ENGLISH: "fight", KLINGON: "Suv"},
        {ENGLISH: "die", KLINGON: "Hegh"},
        {ENGLISH: "cooperate", KLINGON: "jIj"},
        {ENGLISH: "sleep", KLINGON: "Qong"},
        {ENGLISH: "defend", KLINGON: "Hub"},
        {ENGLISH: "love", KLINGON: "MuSHa'"},
        {ENGLISH: "shoot", KLINGON: "bach"},
        {ENGLISH: "fire (torpedo, rocket, missile)", KLINGON: "baH"}
    ],
    NOUNS: [
        {ENGLISH: "knife", KLINGON: "taj"},
        {ENGLISH: "scalpel", KLINGON: "Haqtaj"},
        {ENGLISH: "rock", KLINGON: "nagh"},
        {ENGLISH: "torpedo", KLINGON: "peng"},
        {ENGLISH: "torpedoes", KLINGON: "cha"},
        {ENGLISH: "computer", KLINGON: "De'wI'"},
        {ENGLISH: "ship, vessel", KLINGON: "Duj"},
        {ENGLISH: "device", KLINGON: "jan"},
        {ENGLISH: "explosive", KLINGON: "jorwI'"},
        {ENGLISH: "tricorder", KLINGON: "Hoqra'"},
        {ENGLISH: "communicator", KLINGON: "QumwI'"},
        {ENGLISH: "phaser", KLINGON: "pu'"},
        {ENGLISH: "disruptor", KLINGON: "nISwI'"},
        {ENGLISH: "love", KLINGON: "MuSHa'"}
    ],
    PEOPLE: [
        {ENGLISH: "man", KLINGON: "loD"},
        {ENGLISH: "woman", KLINGON: "be'"},
        {ENGLISH: "child", KLINGON: "puq"},
        {ENGLISH: "mother", KLINGON: "SoS"},
        {ENGLISH: "father", KLINGON: "vav"},
        {ENGLISH: "wife", KLINGON: "be'nal"},
        {ENGLISH: "husband", KLINGON: "loDnI"},
        {ENGLISH: "sister", KLINGON: "be'nI'"},
        {ENGLISH: "brother", KLINGON: "loD'nI'"},
        {ENGLISH: "aunt (mother's sister)", KLINGON: "me'"},
        {ENGLISH: "aunt (father's sister)", KLINGON: "'e'mam"},
        {ENGLISH: "uncle (mother's brother)", KLINGON: "'IrneH"},
        {ENGLISH: "uncle (father's brother)", KLINGON: "tennuS"},
        {ENGLISH: "friend", KLINGON: "jup"},
        {ENGLISH: "close friend", KLINGON: "yIr'ach"},
        {ENGLISH: "close female friend of female", KLINGON: "chaj"},
        {ENGLISH: "close male friend of a male", KLINGON: "maqoch"},
        {ENGLISH: "uncle", KLINGON: ""},
        {ENGLISH: "enemy", KLINGON: ""},
        {ENGLISH: "loved one", KLINGON: "bang"},
        {ENGLISH: "romantic partner", KLINGON: "parmaqqay"}
    ],
    ADJECTIVES: [
        {ENGLISH: "sharp", KLINGON: "jej"},
        {ENGLISH: "dull, blunt", KLINGON: "jejHa'"},
        {ENGLISH: "shiny", KLINGON: "boch"},
        {ENGLISH: "big", KLINGON: "tIn"},
        {ENGLISH: "small", KLINGON: "mach"},
        {ENGLISH: "tired", KLINGON: "Doy'"},
        {ENGLISH: "trivial, unimportant", KLINGON: "ram"},
        {ENGLISH: "pleased", KLINGON: "bel"},
        {ENGLISH: "flat", KLINGON: "beQ"},
        {ENGLISH: "irritable", KLINGON: "bergh"},
        {ENGLISH: "unusual", KLINGON: "motlhbe'"}
    ],
    ADVERBS: [
        {ENGLISH: "honor", KLINGON: "batlh"},
        {ENGLISH: "accidentally", KLINGON: "bong"},
        {ENGLISH: "perhaps", KLINGON: "chaq"},
        {ENGLISH: "on purpose", KLINGON: "chIch"},
        {ENGLISH: "now", KLINGON: "DaH"},
        {ENGLISH: "luckily", KLINGON: "Do'"},
        {ENGLISH: "slightly, a little bit", KLINGON: "loQ"},
        {ENGLISH: "fast, quickly", KLINGON: "nom"},
        {ENGLISH: "never", KLINGON: "not"},
        {ENGLISH: "suddenly", KLINGON: "pay'"},
        {ENGLISH: "often", KLINGON: "pIj"},
        {ENGLISH: "slowly", KLINGON: "QIt"},
        {ENGLISH: "always", KLINGON: "always"},
        {ENGLISH: "sometimes", KLINGON: "rut"},
        {ENGLISH: "soon", KLINGON: "tugh"},
        {ENGLISH: "thus, in that case, so, accordingly, then", KLINGON: "vaj"},
        {ENGLISH: "not yet", KLINGON: "wej"}
    ],
    VERB_BASIC_PREFIXES: [
        {ENGLISH: "I-none", KLINGON: "jI-"},
        {ENGLISH: "I-me", KLINGON: "---"},
        {ENGLISH: "I-you", KLINGON: "qa-"},
        {ENGLISH: "I-him/her/it", KLINGON: "vI-"},
        {ENGLISH: "I-us", KLINGON: "==="},
        {ENGLISH: "I-you(plural)", KLINGON: "Sa-"},
        {ENGLISH: "I-them", KLINGON: "vI-"},
        {ENGLISH: "you-none", KLINGON: "bI-"},
        {ENGLISH: "you-me", KLINGON: "cho-"},
        {ENGLISH: "you-you", KLINGON: "---"},
        {ENGLISH: "you-him/her/it", KLINGON: "Da-"},
        {ENGLISH: "you-us", KLINGON: "ju-"},
        {ENGLISH: "you-you(plural)", KLINGON: "---"},
        {ENGLISH: "you-them", KLINGON: "Da-"},
        {ENGLISH: "he/she/it-none", KLINGON: "0"},
        {ENGLISH: "he/she/it-me", KLINGON: "mu-"},
        {ENGLISH: "he/she/it-you", KLINGON: "Du-"},
        {ENGLISH: "he/she/it-him/her/it", KLINGON: "0"},
        {ENGLISH: "he/she/it-us", KLINGON: "nu-"},
        {ENGLISH: "he/she/it-you(plural)", KLINGON: "lI-"},
        {ENGLISH: "he/she/it-them", KLINGON: "0"},
        {ENGLISH: "we-none", KLINGON: "ma-"},
        {ENGLISH: "we-me", KLINGON: "---"},
        {ENGLISH: "we-you", KLINGON: "pI-"},
        {ENGLISH: "we-him/her/it", KLINGON: "wI-"},
        {ENGLISH: "we-us", KLINGON: "---"},
        {ENGLISH: "we-you(plural)", KLINGON: "re-"},
        {ENGLISH: "we-them", KLINGON: "DI-"},
        {ENGLISH: "you(plural)-none", KLINGON: "Su-"},
        {ENGLISH: "you(plural)-me", KLINGON: "tu-"},
        {ENGLISH: "you(plural)-you", KLINGON: "---"},
        {ENGLISH: "you(plural)-him/her/it", KLINGON: "bo-"},
        {ENGLISH: "you(plural)-us", KLINGON: "che-"},
        {ENGLISH: "you(plural)-you(plural)", KLINGON: "---"},
        {ENGLISH: "you(plural)-them", KLINGON: "bo-"},
        {ENGLISH: "they-none", KLINGON: "0"},
        {ENGLISH: "they-me", KLINGON: "mu-"},
        {ENGLISH: "they-you", KLINGON: "nI-"},
        {ENGLISH: "they-him/her/it", KLINGON: "lu-"},
        {ENGLISH: "they-us", KLINGON: "nu-"},
        {ENGLISH: "they-you(plural)", KLINGON: "lI-"},
        {ENGLISH: "they-them", KLINGON: "0"}
    ],
    VERB_IMPERATIVES_PREFIXES: [
        {ENGLISH: "you-none", KLINGON: "yI-"}, 
        {ENGLISH: "you-me", KLINGON: "HI-"},
        {ENGLISH: "you-him/her/it", KLINGON: "yI-"}, 
        {ENGLISH: "you-us", KLINGON: "gho-"},
        {ENGLISH: "you-them", KLINGON: "tI-"},
        {ENGLISH: "you(plural)-none", KLINGON: "pe-"},
        {ENGLISH: "you(plural)-me", KLINGON: "HI-"},
        {ENGLISH: "you(plural)-him/her/it", KLINGON: "yI-"},
        {ENGLISH: "you(plural)-us", KLINGON: "gho-"},
        {ENGLISH: "you(plural)-them", KLINGON: "tI-"}
    ],
    PRONOUNS: [
        {ENGLISH: "I, me", KLINGON: "jIH"},
        {ENGLISH: "you", KLINGON: "soH"},
        {ENGLISH: "he/she, him/her", KLINGON: "ghaH"},
        {ENGLISH: "'oH", KLINGON: "it"},
        {ENGLISH: "'e'", KLINGON: "that"},
        {ENGLISH: "net", KLINGON: "that"},
        {ENGLISH: "we, us", KLINGON: "maH"},
        {ENGLISH: "you(plural)", KLINGON: "tlhIH"},
        {ENGLISH: "they, them", KLINGON: "chaH"},
        {ENGLISH: "they, them", KLINGON: "bIH"}
    ],
    NUMBERS: [
        {ENGLISH: "0, zero", KLINGON: "pagh"},
        {ENGLISH: "1, one", KLINGON: "wa'"},
        {ENGLISH: "2, two", KLINGON: "cha'"},
        {ENGLISH: "3, three", KLINGON: "wej"},
        {ENGLISH: "4, four", KLINGON: "loS"},
        {ENGLISH: "5, five", KLINGON: "vagh"},
        {ENGLISH: "6, six", KLINGON: "jav"},
        {ENGLISH: "7, seven", KLINGON: "Soch"},
        {ENGLISH: "8, eight", KLINGON: "chorgh"},
        {ENGLISH: "9, nine", KLINGON: "Hut"},
        {ENGLISH: "10, ten", KLINGON: "wa'maH"}
    ],
    BODY_PARTS: [
        {ENGLISH: "head", KLINGON: "nach"},
        {ENGLISH: "hair", KLINGON: "jIb"},
        {ENGLISH: "face", KLINGON: "qab"},
        {ENGLISH: "eye", KLINGON: "mIn"},
        {ENGLISH: "nose", KLINGON: "ghIch"},
        {ENGLISH: "ear", KLINGON: "qogh"},
        {ENGLISH: "mouth", KLINGON: "nuj"},
        {ENGLISH: "neck", KLINGON: "mong"},
        {ENGLISH: "chest", KLINGON: "logh'ob"},
        {ENGLISH: "stomach", KLINGON: "burgh"},
        {ENGLISH: "hip", KLINGON: "'IvtIH"},
        {ENGLISH: "back", KLINGON: "Dub"},
        {ENGLISH: "butt", KLINGON: "Sa'Hut"},
        {ENGLISH: "arm", KLINGON: "DeS"},
        {ENGLISH: "elbow", KLINGON: "DeSqIv"},
        {ENGLISH: "hand", KLINGON: "ghop"},
        {ENGLISH: "thumb (adult)", KLINGON: "SenwI'"},
        {ENGLISH: "finger", KLINGON: "nItlh"}, 
        {ENGLISH: "leg", KLINGON: "'uS"},
        {ENGLISH: "knee", KLINGON: "qIv"},
        {ENGLISH: "foot", KLINGON: "qam"},
        {ENGLISH: "toe", KLINGON: "yaD"}
    ],
    REL_LOCATIONS: [
        {ENGLISH: "here", KLINGON: "naDev"}, 
        {ENGLISH: "there", KLINGON: "pa'"},
        {ENGLISH: "front", KLINGON: "tlhop"},
        {ENGLISH: "between", KLINGON: "joj"},
        {ENGLISH: "beside", KLINGON: "retlh"},
        {ENGLISH: "behind", KLINGON: "'em"},
        {ENGLISH: "above", KLINGON: "Dung"},
        {ENGLISH: "below", KLINGON: "bIng"},
        {ENGLISH: "under", KLINGON: "bIng"}
    ]
}

def save_dict():
    #Converts the klingon_dict to JSON format and saves to file.
    #Really only used in development, once in place we only read the file to get the klingon dictionary so we can use it.
    if SAVE:
        with open('dictionary/dictionary.json', 'w') as outfile:
            json.dump(_klingon_dict, outfile)
            
def load_dict():
    global _klingon_dict
    with open('dictionary/dictionary.json', 'r') as openfile:
        _klingon_dict = json.load(openfile)

def get_dict():
    return _klingon_dict.copy()

def get_dict_type(dict_type):
    return _klingon_dict[dict_type].copy()

def get_t_verb_prefixes():
    return [
        ["OBJECT", "none", "me", "you", "him/\nher/\nit", "us", "you\nplural", "them"],
        ["SUBJECT", "I", "you", "he/she/it", "we", "you(plural)", "they"],
        [
        ["jI-", "---", "qa-", "vI-", "---", "Sa-", "vI-"],
        ["bI-", "cho-", "---", "Da-", "ju-", "---", "Da-"],
        ["0", "mu-", "Du-", "0", "nu-", "lI-", "0"],        
        ["ma-", "---", "pI-", "wI-", "---", "re-", "DI-"],        
        ["Su-", "tu-", "---", "bo-", "che-", "---", "bo-"],        
        ["0", "mu-", "nI-", "lu-", "nu-", "lI-", "0"]
        ]
    ]