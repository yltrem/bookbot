# Boot.dev course project: Bookbot
from stats import get_book_text, get_words_count, get_chars_count

def main():
    chars = {}
    book = ""

    with open("./books/frankenstein.txt") as f:
        book = get_book_text(f)
    
    print(f"Found {get_words_count(book)} total words")
    print("Characters used:")
    chars = get_chars_count(book)
    print(chars)

    
                  

main()
