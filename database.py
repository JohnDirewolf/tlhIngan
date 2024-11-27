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