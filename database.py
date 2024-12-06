#Database
#This program stores the klingon reference in a dictionary saved to a JSON file
#This is set as as seperate module in case in future we want to actually implmement a full database interface.

import json
import constants

_klingon_dict = {
    constants.VERB_PREFIXES: [{"english": "I-none", "klingon": "jI-"}, {"english": "I-you", "klingon": "qa-"},{"english": "I-him/her/it", "klingon": "vI-"}],
    constants.BODY_PARTS: [{"english": "arm", "klingon": "Des"}, {"english": "leg", "klingon": "'uS"},{"english": "head", "klingon": "nach"}],
    constants.REL_LOCATIONS: [{"english": "here", "naDev": "jI-"}, {"english": "there", "klingon": "pa'"},{"english": "in front of", "klingon": "tlhop"}]
}

def save_dict():
    #Converts the klingon_dict to JSON format and saves to file.
    #Really only used in development, once in place we only read the file to get the klingon dictionary so we can use it.
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