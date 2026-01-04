# Boot.dev course project: Bookbot
from stats import get_words_count

def main():
    with open("./books/frankenstein.txt") as f:
        print(f"Found {get_words_count(f)} total words")

main()
