""" The program's name: Word Count
Your name: Rajani Baraili
The purpose of the program: displays menu of 4 files, lets user choose one,
reads and analyzes that file, counts the frequency of every word in the
selected file, and prints an alphabetical report.
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
            if not self.__pathlibrary.exists():
                raise FileNotFoundError

            translation_table = str.maketrans('', '', string.punctuation)

            with self.__pathlibrary.open('r', encoding='utf-8', errors='ignore') as file:


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
            print(f"{word:<15} :: {self.__frequencies[word]}")


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
        print("--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key, (title, path) in file_menu.items():
            print(f"{key}. {title}")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        elif choice in file_menu:
            title, path = file_menu[choice]
            print(f"Processing '{path.name}'...\n")
            analyzer = WordAnalyzer(path)
            if analyzer.process_file():
                analyzer.print_report()
            else:
                print(f"Could not process {title}. File may not exist.")
            input("Press Enter to return to the menu... ")

        else:
            print("Invalid choice. Please select from 1-5.")
            input("Press Enter to return to the menu... ")


if __name__ == "__main__":
    main()
