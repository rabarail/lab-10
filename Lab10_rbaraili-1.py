
""" The program's name:Word Count 
Your name: Rajani Baraili
The purpose of the program: displays menu of 4 file, lets user choose one and reads and analyze that file and count the frequency of every
word selected file and prints alphabetical report.
Any info about starter code: none
Date: 03/29/2026 """

import pathlib
import string


class WordAnalyzer:

    def __init__(self, filepath):
        self.__pathlibrary = pathlib.Path(filepath) 
        self.__frequencies = {}    

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError(f"File '{self.__filepath}' does not exist.")
            
            translation_table = str.maketrans('', '', string.punctuation)
            
            with self.__filepath.open('r') as file:
                for line in file:

                    line = line.translate(translation_table).lower()
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True
        except FileNotFoundError:
            return False
        
    def print_report(self):

        sorted_words = sorted(self.__frequencies.keys())
        
        for word in sorted_words:
            print(f"{word}: {self.__frequencies[word]}")

def main():

    book_menu = pathlib.Path("books")

    file_menu = {
    "1": ("Princess Mars",   book_menu / "princess_mars.txt"),
    "2": ("Tarzan",          book_menu / "Tarzan.txt"),
    "3": ("Treasure Island", book_menu / "treasure_island.txt"),
    "4": ("Monte Cristo",    book_menu / "monte_cristo.txt"),
}
    










        





