from data.dictionary_data import dictionary_data

def search_word(word):
    return dictionary_data.get(word.lower())

def search_keyword