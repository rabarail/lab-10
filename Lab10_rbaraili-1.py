
""" The program's name:Word Count 
Your name: Rajani Baraili
The purpose of the program: displays menu of 4 file, lets user choose one and reads and analyze that file and count the frequency of every
word selected file and prints alphabetical report.
Any info about starter code: none
Date: 03/29/2026 """

import pathlib


class WordAnalyzer:

    def __init__(self, filepath):
        self.__pathlibrary = pathlib.Path(filepath) 
        self.__frequencies = {}    
         



