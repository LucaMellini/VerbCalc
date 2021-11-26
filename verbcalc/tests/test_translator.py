"""
Tests translator module.
"""
import unittest
import verbcalc


class TestTranslator(unittest.TestCase):
    """
    Tests how translator works.
    """

    def setUp(self):
        self._custom_symbols = verbcalc.Symbols()
        self._custom_symbols.additions = ['foo']
        self._custom_symbols.subtractions = ['bar']
        self._custom_symbols.multiplications = ['boo']
        self._custom_symbols.divisions = ['far']
        self.expected = ['2 + 2', '2 - 2', '2 * 2', '2 / 2', '2 ** 2',
                         'abs 2', '2 % 2']

    def test_translation(self):
        values = [verbcalc.translate('2 plus 2'),
                  verbcalc.translate('2 minus 2'),
                  verbcalc.translate('2 times 2'),
                  verbcalc.translate('2 divided by 2'),
                  verbcalc.translate('2 to the power of 2'),
                  verbcalc.translate('absolute of 2'),
                  verbcalc.translate('2 mod 2')]
        self.assertListEqual(self.expected, values)

    def test_translation_with_custom_symbols(self):
        values = [
            verbcalc.translate('2 foo 2', symbols=self._custom_symbols),
            verbcalc.translate('2 bar 2', symbols=self._custom_symbols),
            verbcalc.translate('2 boo 2', symbols=self._custom_symbols),
            verbcalc.translate('2 far 2', symbols=self._custom_symbols),
            verbcalc.translate('2 to the power of 2',
                               symbols=self._custom_symbols),
            verbcalc.translate('absolute of 2', symbols=self._custom_symbols),
            verbcalc.translate('2 mod 2', symbols=self._custom_symbols)
        ]
        self.assertListEqual(self.expected, values)

    def test_txt_to_int(self):
        self.assertEqual(verbcalc.translate("five"), 5)
        self.assertEqual(verbcalc.translate("twelve"), 12)
        self.assertEqual(verbcalc.translate("sixty one"), 61)
        self.assertEqual(verbcalc.translate("sixty-one"), 61)
        self.assertEqual(verbcalc.translate("one thousand eighty nine"), 1089)
        self.assertEqual(verbcalc.translate("five million and two"), 5000002)
        self.assertEqual(verbcalc.translate("eighty three thousand"), 83000)
        self.assertEqual(verbcalc.translate("five million sixty five thousand three hundred and eighty-one"), 5065381)


if __name__ == '__main__':
    unittest.main()
