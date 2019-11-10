import unittest
from toXComposeTools import *


class toXComposeTests(unittest.TestCase):
    def test_hexCodePt(self):
        self.assertEqual(hexCodePt(u'→'), 'U2192')

    def test_charXCInfo(self):
        self.assertEqual(charXCInfo(u'→'),
                         (u'→', 'U2192', 'RIGHTWARDS ARROW'))

    def test_char2XCLine1(self):
        self.assertEqual(char2XCLine(u'→'),
                         '<Multi_key> : "→" U2192 # RIGHTWARDS ARROW')

    def test_char2XCLine2(self):
        self.assertEqual(char2XCLine(u'⦂', ["bar", "colon"]),
                         '<Multi_key> <bar> <colon> : "⦂" U2982 # Z NOTATION TYPE COLON')

    def test_char2XC(self):
        self.assertEqual(char2XC(u'→'),
                         ': "→" U2192 # RIGHTWARDS ARROW')

    def test_char2XCWeb(self):
        self.assertEqual(char2XCWeb(u'→'),
                         ': "→" U2192 # RIGHTWARDS ARROW')

    def test_char2XCWeb(self):
        self.assertEqual(char2XCWeb(u'𝕇'),
                         ': "𝕇" U1D547 # ERR: Name not found')


if __name__ == '__main__':
    unittest.main()
