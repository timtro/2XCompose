import unicodedata as uc
from typing import Tuple, NewType
import requests
from bs4 import BeautifulSoup
from string import hexdigits

"""
Naming conventions:

    uhex: a string formatted "U𝑥",
        where 𝑥 is a string of hexdigits. Eg. '→' has uhex 'U2192'

    xCLine: a string formatted '<𝐴> [<𝐵> ⋯ ] : "𝐶" # 𝑁'
        where 𝐴 and 𝐵 are keys, 𝐶 is the unicode char and 𝑁 is 𝐶's unicode name.

"""


ChrUhexName = NewType('ChrUhexName', Tuple[str, str, str])


def char2uhex(char: str) -> str:
    assert len(char) == 1, 'Must look up single characters.'
    return 'U'+'%04X' % ord(char)


def uhex2int(hx: str) -> int:
    hx = ''.join(c for c in hx if c in hexdigits)
    return int(hx, 16)


def lookup_char(char: str) -> ChrUhexName:
    try:
        charname = uc.name(char)
    except:
        charname = "ERR: Name not found"

    return (char,
            char2uhex(char),
            charname)


def lookup_uhex(uhx: str) -> ChrUhexName:
    char = chr(uhex2int(uhx))
    try:
        charname = uc.name(char)
    except:
        charname = "ERR: Name not found"

    return (char,
            uhx.upper(),
            charname)


def lookup_name(name: str) -> ChrUhexName:
    char = uc.lookup(name)
    return (char, char2uhex(char), name)


def ChrUhexName2XCLine(cun: ChrUhexName, keyStr: str = None) -> str:
    (char, uhx, name) = cun
    uhx = uhx.upper()
    if not keyStr:
        keyStr = ""
    return keyStr + ': "' + char + '" ' + uhx + ' # ' + name


def char2xc(char: str, keyStr=None) -> str:
    return ChrUhexName2XCLine(lookup_char(char), keyStr)


def uhex2xc(uhx: str, keyStr=None) -> str:
    return ChrUhexName2XCLine(lookup_uhex(uhx), keyStr)


def name2xc(name: str, keyStr=None) -> str:
    return ChrUhexName2XCLine(lookup_name(name), keyStr)


baseURL = 'http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input='


def char_lookup_url(char: str) -> str:
    return baseURL + char + '&mode=char'


def uhex_lookup_url(hx: str) -> str:
    return baseURL + hx + '&mode=hex'


def scrape_url(URL: str) -> ChrUhexName:
    response = requests.get(URL)
    infoTRs = BeautifulSoup(response.text, 'html.parser').findAll('tr')
    charData = {}
    for row in infoTRs:
        cells = row.findAll('td')
        charData[cells[0].find(text=True)] = cells[1].find(text=True)
    if charData['Character name'] == None:
        charData['Character name'] = "ERR: Name not found"
    return (charData['Character'],
            "U"+charData['Hex code point'],
            charData['Character name'])


def lookup_char_web(char: str) -> ChrUhexName:
    return scrape_url(char_lookup_url(char))


def char2xc_web(char: str, keyStr=None) -> str:
    return ChrUhexName2XCLine(lookup_char_web(char), keyStr)
