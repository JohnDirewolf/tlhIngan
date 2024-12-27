#Database
#This program stores the klingon reference in a dictionary saved to a JSON file
#This is set as as seperate module in case in future we want to actually implmement a full database interface.

import json
from constants import *

_klingon_dict = {} #{ENGLISH: "", KLINGON: ""}
_affixes_dict = {} #{ENGLISH: "", KLINGON: "", TYPE: #}
_tables_dict = {} #Custom for each table, generally list of lists, 0 - Column Headers, 1 - Row Headers, 2 - 2D list of data, answers

def load_dict():
    global _klingon_dict, _tables_dict
    with open('dictionary/dictionary.json', 'r') as openfile:
        _klingon_dict = json.load(openfile)
    with open('dictionary/affixes.json', 'r') as openfile:
        _affixes_dict = json.load(openfile)    
    with open('dictionary/tables.json', 'r') as openfile:
        _tables_dict = json.load(openfile)

def get_klingon_dict():
    return _klingon_dict.copy()

def get_affixes_dict():
    return _affixes_dict.copy()

def get_tables_dict():
    return _tables_dict.copy()

def get_klingon_type(dict_type):
    return _klingon_dict[dict_type].copy()

def get_affixes_type(dict_type):
    return _affixes_dict[dict_type].copy()

def get_tables_type(dict_type):
    return _tables_dict[dict_type].copy()