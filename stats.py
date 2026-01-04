def get_book_text(filepath):
    return filepath.read()

def get_words_count(filepath):
    word_list = get_book_text(filepath).split() 
    return len(word_list)