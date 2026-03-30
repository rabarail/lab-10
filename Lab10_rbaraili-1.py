
""" The program's name:Word Count 
Your name: Rajani Baraili
The purpose of the program: displays menu of 4 file, lets user choose one and reads and analyze that file and count the frequency of every
word selected file and prints alphabetical report.
Any info about starter code: none
Date: 03/29/2026 """

from importlib.resources import path
import pathlib
from secrets import choice
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

    base_path = pathlib.Path(__file__).parent
    book_path = base_path / "books"

    file_menu = {
    "1": ("Princess Mars",   book_path / "princess_mars.txt"),
    "2": ("Tarzan",          book_path / "Tarzan.txt"),
    "3": ("Treasure Island", book_path / "treasure_island.txt"),
    "4": ("Monte Cristo",    book_path / "monte_cristo.txt"),
}
    
    while True:
        print("---Word Analyzer---")
        print("Please select a file to analyze:")

        for key, (title, __path__) in __file__menu.items():
            print(f"{key}. {title}")
        print("5. Exit")    

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting...")
            break
        elif choice in file_menu:
             title, path = file_menu[choice]

        analyzer = WordAnalyzer(path)

        if analyzer.process_file():
            analyzer.print_report()

        else:
            print(f"Could not process {title}. File may not exist.")
            print("Press Enter to return to the menu... ")













        





