"""
Translator module allows to change natural language to mathematical notation.
"""
from verbcalc.core.translator.symbols import Symbols
from verbcalc.core.translator.numbers import Numbers

DEFAULT_SYMBOLS = Symbols()
NUMBERS = Numbers()

def translate(sentence: str, symbols: Symbols = DEFAULT_SYMBOLS, numbers: Numbers = NUMBERS) -> str:
    """
      Translates maths related words into their symbols.

      Args:
          sentence: Sentence to be converted.
          symbols: Instance of symbols to match the words from.
          numbers : Instance of literal numbers to match the numbers from.

      Returns:
          Converted sentence.
    """
    result = sentence.lower()

    # translate the symbols in the initial sentence
    for key in symbols.symbol_dictionary.keys():
        for phrase in symbols.symbol_dictionary[key]:
            result = result.replace(phrase, key)


    # split the sentence based on whitespace
    # i.e. ['abs', 'four', 'hundred', '-', 'eight', '+', 'five']
    splitted = result.split(" ")

    # create a dictionnary and initialize it
    # i.e. {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    temp_dict = {}
    for i in range(2*len(splitted)):
        temp_dict[i] = []

    # add all splitted elements to the dictionnary (splitting them on operators)
    # i.e. {0: ['abs'], 1: ['four', 'hundred'], 2: ['-'], 3: ['eight'], 4: ['+'], 5: ['five'], 6: []}
    index = 0
    for item in splitted:
        if item not in symbols.symbol_dictionary.keys():
            temp_dict[index].append(item)
        else:
            index += 1
            temp_dict[index].append(item)
            index += 1

    # clean up the dictionnary by removing any entry having empty value
    # i.e. {0: ['abs'], 1: ['four', 'hundred'], 2: ['-'], 3: ['eight'], 4: ['+'], 5: ['five']}
    temp_dict = {key: val for key, val in temp_dict.items() if len(val) > 0}

    # translate every "non-symbol" entry (= written number) into its actual integer
    # i.e. {0: ['abs'], 1: '400', 2: ['-'], 3: '8', 4: ['+'], 5: '5'}
    for i, item in temp_dict.items():
        if item[0] not in symbols.symbol_dictionary.keys() and not numbers.is_string_an_integer(item[0]):
            temp_dict[i] = numbers.text_to_int(" ".join(item))

    # parse every entry to string
    # i.e. {0: 'abs', 1: '4', 2: '-', 3: '8', 4: '+', 5: '5'}
    for key, val in temp_dict.items():
        if isinstance(val, list):
            temp_dict[key] = val[0]
        else:
            temp_dict[key] = str(val)

    # parse the dictionnary into a single string
    # i.e. "abs 4 - 8 + 5"
    result = " ".join(temp_dict.values())

    return result
