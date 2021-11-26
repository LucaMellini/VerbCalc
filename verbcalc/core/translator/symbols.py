"""
   Handles symbol storage.
"""


class Symbols:
    """
    Hint:
        You can edit lists like additions, subtractions etc. to make a library's
        translation to other language (human language, not programming language)
        or implement any other custom behaviour you desire.

    Stores lists with words corresponding to given symbols.

    Attributes:
        symbol_dictionary:
            Stores all the symbol keys and their corresponding values.
    """

    def __init__(self):
        self._additions = ['plus']
        self._subtractions = ['minus']
        self._multiplications = ['times', 'multiplied by']
        self._divisions = ['divided by']
        self._exponentiations = ['to the power of']
        self._absolutes = ['absolute of', 'absolute value of']
        self._modulo = ['mod', 'modulo']
        self._roots = ['root of']
        self._questions = ['what is the result of', 'what is', 'calculate',
                           'result of', 'how do you', 'find',' how much',
                           'how much is', 'which number is result of', 'what']
        self.symbol_dictionary = {
            '+': self._additions,
            '-': self._subtractions,
            '*': self._multiplications,
            '/': self._divisions,
            '**': self._exponentiations,
            'abs': self._absolutes,
            '%': self._modulo,
            'root': self._roots,
            '': self._questions
        }

    @property
    def additions(self) -> list:
        return self._additions

    @property
    def subtractions(self) -> list:
        return self._subtractions

    @property
    def multiplications(self) -> list:
        return self._multiplications

    @property
    def divisions(self) -> list:
        return self._divisions

    @property
    def exponentiations(self) -> list:
        return self._exponentiations

    @property
    def absolutes(self) -> list:
        return self._absolutes

    @property
    def modulo(self) -> list:
        return self._modulo

    @property
    def roots(self) -> list:
        return self._roots

    @property
    def questions(self) -> list:
        return self._questions

    @additions.setter
    def additions(self, value) -> None:
        self._additions = value
        self.symbol_dictionary.update({'+': self._additions})

    @subtractions.setter
    def subtractions(self, value) -> None:
        self._subtractions = value
        self.symbol_dictionary.update({'-': self._subtractions})

    @multiplications.setter
    def multiplications(self, value) -> None:
        self._multiplications = value
        self.symbol_dictionary.update({'*': self._multiplications})

    @divisions.setter
    def divisions(self, value) -> None:
        self._divisions = value
        self.symbol_dictionary.update({'/': self._divisions})

    @exponentiations.setter
    def exponentiations(self, value) -> None:
        self._exponentiations = value
        self.symbol_dictionary.update({'**': self._exponentiations})

    @absolutes.setter
    def absolutes(self, value) -> None:
        self._absolutes = value
        self.symbol_dictionary.update({'abs': self._absolutes})

    @modulo.setter
    def modulo(self, value) -> None:
        self._modulo = value
        self.symbol_dictionary.update({'%': self._modulo})

    @roots.setter
    def roots(self, value) -> None:
        self._roots = value
        self.symbol_dictionary.update({'root': self._roots})

    @questions.setter
    def questions(self, value) -> None:
        self._questions = value
        self.symbol_dictionary.update({'': self._questions})
