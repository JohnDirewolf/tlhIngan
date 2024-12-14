# thlIngan Hol ghojmoHwI' boQ
## Klingon Hol Teacher's Aide

## Description
Learning aide for the Klingon language, tlhIngan Hol
I started learning Klingon many years ago for fun and for use on online Star Trek games. 
I got interested originally because of PC Game Star Trek: Klingon which was a holodeck "immersion study" of the Klingon culture.
Later I got the book The Klingon Dictionary by the inventory of the langugage Marc Okrand. 
And more recently I have used the Duolingo Klingon language track.
During all this self learning I made a lot of flash cards and tests and games to help learn and remember the language.

Now I have used Python and the tkinter library to create an app to assist in learning Klingon with similar techniques I have been using over the years.

## Contents
main.py - the main file that creates the app window.
classes.py - contains the classes for the tables and flash cards
constants.py - all the color, height, width, fonts, and other formatting constants. Also constants for the JSON file keys.
database.py - loads the dictionaries and provides them to the app.
/dictionary
    dictionary.json - Contains the Klingon Lanuage in a dictionary of lists using the constants from constants.py as the list key and each list is dictionaries of the 
                      English, Klingon, and if needed Syntatic Type
    tables.json - Contains the columna and row headers as well as the correct Klingon for all the entry boxes. It is a dictionary of lists of arrays, using the constants 
                  from constants.py as the list key. Index 0 is the column headers, 1 is the row headers, and 3 is a list, 2-D or other format, for the table.  

## Requirements
Python 3.12.2 or better

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JohnDirewolf/tlhIngan
   cd tlhIngan
   ```

2. Install Python 3.12+ if needed.
   To install  on Ubuntu, run the following commands in your terminal:
    ```bash
    sudo apt update
    sudo apt install python3.12
    ```

3. Running the Application
   To run the application:
      ```bash
      python main.py
      ```

## Usage

The main UI will appear and give the various options.

On the left are Tables for different types of words and language. 
Tables have the ability to either show the Klingon, filling in the table, so can be used for reference.
Or you can instead fill in the table and then click Submit and the app will score your entries and tell you if you succeeded or failed.

Flash Cards are great for vocabulary building. Again there are Flash Cards for different types of words and parts of speech. 
Flash Cards can show either the English or the Klingon so you can practice in both directions. 
You do not fill out the Card, instead you simply make your guess and then click Show and see if you were correct. 
You can use the Prev and Next buttons to then move between the cards.
Each time you start a Flash Card, the app shuffles the words so they may appear in any order.

/dictionary/dictionary.json has the klingon langauge reference in a JSON format that could be useful for other apps by itself. Simply add
the file to your application directory and load the informtion using the Python JSON library. See the contents section for more on its structure.

## Contributing

If you run thlIngan Hol ghojmoHwI' boQ and would like to share feedback, please open an issue on GitHub: [tlhIngan Issues](https://github.com/JohnDirewolf/tlhIngan/issues)