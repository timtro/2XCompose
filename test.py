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
                         ' : "→" U2192 # RIGHTWARDS ARROW')

    def test_name2xc(self):
        self.assertEqual(name2xc('RIGHTWARDS ARROW'),
                         ' : "→" U2192 # RIGHTWARDS ARROW')

    def test_uhex2xc(self):
        self.assertEqual(uhex2xc('U2192'),
                         ' : "→" U2192 # RIGHTWARDS ARROW')

    def test_lookup_char_internalVSWeb(self):
        self.assertEqual(lookup_char(u'→'),
                         lookup_char_web(u'→'))

    def test_char2xc_web(self):
        self.assertEqual(char2xc_web(u'→'),
                         ' : "→" U2192 # RIGHTWARDS ARROW')
        self.assertEqual(char2xc_web(u'𝕇'),
                         ' : "𝕇" U1D547 # ERR: Name not found')

    def test_lookup_uhex_web(self):
        self.assertEqual(lookup_uhex_web('U2192'),
                         lookup_char_web(u'→'))
        self.assertEqual(lookup_uhex_web('U25CB'),
                         lookup_char_web(u'○'))
        return 1

    def test_uhex2xc_web(self):
        self.assertEqual(uhex2xc_web('U2192'),
                         ' : "→" U2192 # RIGHTWARDS ARROW')

if __name__ == '__main__':
    unittest.main()
