import string

from conditions import conditions

'''
     |-----------
     |          |
     |          |
     |          O
     |          |
     |         /|\
     |          |
     |         /\
     |
________________
'''


class Viselica:
    field_condition = ""

    def __init__(self, word):
        self.word = word
        self.word_condition = len(word) * '_'
        self.wrong_letters = set()
        self.flag = True

    def input_letter(self) -> str:
        letter = input('Введите букву - ')
        if len(letter) != 1 or letter in string.punctuation or letter == ' ':
            print('Введите только одну букву')
            letter = self.input_letter()
        if letter.isdigit():
            print('Значение не должно быть числом')
        return letter

    def check_letter(self, letter) -> bool:
        return letter in self.word and self.word.count(letter) > self.word_condition.count(letter)

    def check_winner(self) -> bool:
        return self.word == self.word_condition

    def update_word_condition(self, letter) -> None:
        word_condition_splitted = list(self.word_condition)
        for no, i in enumerate(self.word):
            if i == letter:
                word_condition_splitted[no] = letter
        self.word_condition = ''.join(word_condition_splitted)

    def play(self) -> None:
        print(f'Слово состоит из {len(self.word)} букв.')
        while self.flag:
            self.make_turn()

    def make_turn(self) -> None:
        print(self.field_condition)
        print('Буквы, которых нет в слове: ', self.wrong_letters if self.wrong_letters else "[ ]")
        print(self.word_condition)
        print()

        new_letter = self.input_letter()
        if self.check_letter(new_letter):
            self.update_word_condition(new_letter)
        else:
            self.wrong_letters.add(new_letter)
            if len(self.wrong_letters) <= len(conditions):
                self.field_condition = conditions[len(self.wrong_letters)]
            else:
                print('Вы Дашка! поправьте трусы')
                print(f'А слово было {self.word}')
                self.flag = False
                return
        if self.check_winner():
            print('Вы победитель! Поздравляю! ')
            print(self.word)
            self.flag = False


game = Viselica("слово")

game.play()

