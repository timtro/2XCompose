import unittest
from toXComposeTools import *


class toXComposeTests(unittest.TestCase):
    def test_char2uhex(self):
        self.assertEqual(char2uhex(u'→'), 'U2192')

    def test_lookup_char(self):
        self.assertEqual(lookup_char(u'→'),
                         (u'→', 'U2192', 'RIGHTWARDS ARROW'))

    def test_lookup_uhex(self):
        self.assertEqual(lookup_uhex('U2192'),
                         lookup_char(u'→'))
        self.assertEqual(lookup_uhex('U25CB'),
                         lookup_char(u'○'))

    def test_lookup_name(self):
        self.assertEqual(lookup_name('RIGHTWARDS ARROW'),
                         lookup_char(u'→'))
        self.assertEqual(lookup_name('WHITE CIRCLE'),
                         lookup_char(u'○'))

    def test_char2xc(self):
        self.assertEqual(char2xc(u'→'),
                         ': "→" U2192 # RIGHTWARDS ARROW')

    def test_lookup_char_internalVSWeb(self):
        self.assertEqual(lookup_char(u'→'),
                         lookup_char_web(u'→'))

    def test_char2xc_web(self):
        self.assertEqual(char2xc_web(u'→'),
                         ': "→" U2192 # RIGHTWARDS ARROW')

    def test_char2xc_web(self):
        self.assertEqual(char2xc_web(u'𝕇'),
                         ': "𝕇" U1D547 # ERR: Name not found')


if __name__ == '__main__':
    unittest.main()
