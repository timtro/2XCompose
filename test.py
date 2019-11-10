import unittest
from toXComposeTools import *


class toXComposeTests(unittest.TestCase):
    def test_char2Uhex(self):
        self.assertEqual(char2Uhex(u'→'), 'U2192')

    def test_lookupChar(self):
        self.assertEqual(lookupChar(u'→'),
                         (u'→', 'U2192', 'RIGHTWARDS ARROW'))

    def test_lookupUhex(self):
        self.assertEqual(lookupUhex('U2192'),
                         lookupChar(u'→'))
        self.assertEqual(lookupUhex('U25CB'),
                         lookupChar(u'○'))

    def test_lookupName(self):
        self.assertEqual(lookupName('RIGHTWARDS ARROW'),
                         lookupChar(u'→'))
        self.assertEqual(lookupName('WHITE CIRCLE'),
                         lookupChar(u'○'))

    def test_char2XCLine(self):
        self.assertEqual(char2XCLine(u'→'),
                         ': "→" U2192 # RIGHTWARDS ARROW')

    def test_lookupChar_internalVSWeb(self):
        self.assertEqual(lookupChar(u'→'),
                         lookupCharWeb(u'→'))

    def test_char2XCLineWeb(self):
        self.assertEqual(char2XCLineWeb(u'→'),
                         ': "→" U2192 # RIGHTWARDS ARROW')

    def test_char2XCLineWeb(self):
        self.assertEqual(char2XCLineWeb(u'𝕇'),
                         ': "𝕇" U1D547 # ERR: Name not found')


if __name__ == '__main__':
    unittest.main()
