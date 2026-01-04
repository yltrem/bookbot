def get_book_text(filepath):
    return filepath.read()

def get_words_count(book):
    word_list = book.split() 
    return len(word_list)

def get_chars_count(book):
    book = book.lower()
    chars = {}

    for c in book:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1

    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_dict(dict):
    temp_list = []

    for i in dict:
        #print(f"{i}: {dict[i]}")
        temp_list.append({"name" : i, "num": dict[i]})
    
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list


