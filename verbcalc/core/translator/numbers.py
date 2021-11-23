"""
    Handles literal numbers
"""

class Numbers:
    """

    """

    def __init__(self):
        self.units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]
        self.word_int_map = self.create_dict()


    def create_dict(self):
        """

        Returns: a dictionnary mapping every literals to their corresponding integer

        i.e. {"five" : (a, b)} where a is the scale of the literal (1 in this case)
                                     b is the corresponding int (5 in this case)
        """
        res = {}

        for index, word in enumerate(self.units):
            res[word] = (1, index)

        for index, word in enumerate(self.tens):
            res[word] = (1, index * 10)

        for index, word in enumerate(self.scales):
            res[word] = (10 ** (index * 3 or 2), 0)

        res["and"] = (1, 0)

        return res


    def text_to_int(self, txt):
        """

        Args:
            txt: the literal number to convert

        Returns: an integer translation of txt

        """
        current = result = 0

        txt = txt.replace('-', ' ')

        for word in txt.split():
            if word not in self.word_int_map:
                raise Exception("Word not handled: " + word)

            scale, num = self.word_int_map[word]
            current = current * scale + num
            if scale > 100:
                result += current
                current = 0

        return result + current
