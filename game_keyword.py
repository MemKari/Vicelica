from words_generator import your_word_is

'''
Если играете вдвоем, укажите слово для отгадывания ниже в кавычках.
Если вы играете один, оставьте keyword пустым.
'''
key_word = ''


def check_keyword():
    return key_word or your_word_is
