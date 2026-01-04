# Boot.dev course project: Bookbot
from stats import get_book_text, get_words_count, get_chars_count, get_sorted_dict

def main():
    chars = {}
    sorted_list = []
    book = ""
    
    print("=========== BOOKBOT ===========")

    with open("books/frankenstein.txt") as f:
        book = get_book_text(f)
        print(f"Analyzing book found at {f.name}")

    print("----------- Word Count -----------")
    print(f"Found {get_words_count(book)} total words")
    print("--------- Character Count --------- ")
    chars = get_chars_count(book)
    sorted_list = get_sorted_dict(chars)
    for i in range(0, len(sorted_list)):
        if sorted_list[i]["name"].isalpha():
                print(f"{sorted_list[i]["name"]}: {sorted_list[i]["num"]}")

main()
