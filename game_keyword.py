from words_generator import your_word_is

'''
If you are playing together, specify the word to guess below in quotation marks.
If you are playing alone, leave the key_word blank.
'''
key_word = ''


def check_keyword() -> str:
    return key_word or your_word_is
