import string

from conditions import conditions
from game_keyword import check_keyword

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
    """A class to represent a Hangman game in Russian."""

    field_condition = ""
    """A string representing the current visual state of the game."""

    def __init__(self, word):
        self.word = word
        self.word_condition = len(word) * '_'
        self.wrong_letters = set()
        self.flag = True

    def input_letter(self) -> str:
        """
        Prompt the player to input a letter and validates the input. Ensure the input is a single,
        unused, non-numeric character.
        """
        letter = input('Введите букву - ').lower().strip()
        if letter in self.wrong_letters:
            print('Эта буква уже была')
            letter = self.input_letter()
        if len(letter) != 1 or letter in string.punctuation:
            print('Введите только одну букву')
            letter = self.input_letter()
        if letter in self.word_condition:
            print('Эта буква уже есть в слове')
            letter = self.input_letter()
        if letter.isdigit():
            print('Значение не должно быть числом')
            letter = self.input_letter()
        return letter

    def check_letter(self, letter) -> bool:
        """Check if the input letter is in the word and if it has not been guessed already."""
        return letter in self.word and self.word.count(letter) > self.word_condition.count(letter)

    def check_winner(self) -> bool:
        """Check if the word is guessed correctly"""
        return self.word == self.word_condition

    def update_word_condition(self, letter) -> None:
        """Update the word_condition with the correctly guessed letter."""
        word_condition_splitted = list(self.word_condition)
        for no, i in enumerate(self.word):
            if i == letter:
                word_condition_splitted[no] = letter
        self.word_condition = ''.join(word_condition_splitted)

    def play(self) -> None:
        """Start the game and continues until the game is won or lost."""
        print(f'Слово состоит из {len(self.word)} букв.')
        while self.flag:
            self.make_turn()

    def make_turn(self) -> None:
        """
        Handle the logic for each turn of the game. Prompt for a letter, check the letter,
        update the game state, and determine if the game is won or lost.
        """
        print(self.field_condition)
        print('Буквы, которых нет в слове: ', self.wrong_letters if self.wrong_letters else "[ ]")
        print(self.word_condition)
        print()

        new_letter = self.input_letter()
        if self.check_letter(new_letter):
            self.update_word_condition(new_letter)
        else:
            self.wrong_letters.add(new_letter)
            self.field_condition = conditions[len(self.wrong_letters)]
            if len(self.wrong_letters) == len(conditions) - 1:
                print(self.field_condition)
                print('Вы проиграли эту битву!')
                print(f'А слово было {self.word}')
                self.flag = False
                return
        if self.check_winner():
            print('Вы победитель! Поздравляю! ')
            print(self.word)
            self.flag = False


word = check_keyword()
game = Viselica(word)

game.play()
