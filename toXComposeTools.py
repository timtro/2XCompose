import unicodedata as uc
from typing import Tuple, NewType
import requests
from bs4 import BeautifulSoup
from string import hexdigits

"""
Namin conventions

    uhex—a string formatted "U𝑿",
        where 𝑥 is a string of hexdigits. Eg. '' has uhex 'U2192'

    xCLine—a string formatted '<𝐴> [<𝐵> ⋯ ] : "𝐶" # 𝑁'
        where 𝐴 and 𝐵 are keys, 𝐶 is the unicode char and 𝑁 is 𝐶's unicode name.

"""


ChrUhexName = NewType('ChrUhexName', Tuple[str, str, str])


def char2Uhex(char: str) -> str:
    assert len(char) == 1, 'Must look up single characters.'
    return 'U'+'%04X' % ord(char)


def uhex2int(hx: str) -> int:
    hx = ''.join(c for c in hx if c in hexdigits)
    return int(hx, 16)


def lookupChar(char: str) -> ChrUhexName:
    try:
        charname = uc.name(char)
    except:
        charname = "ERR: Name not found"

    return (char,
            char2Uhex(char),
            charname)


def lookupUhex(uhx: str) -> ChrUhexName:
    char = chr(uhex2int(uhx))
    try:
        charname = uc.name(char)
    except:
        charname = "ERR: Name not found"

    return (char,
            uhx,
            charname)


def lookupName(name: str) -> ChrUhexName:
    char = uc.lookup(name)
    return (char, char2Uhex(char), name)


def char2XCLine(char: str, keyStr=None) -> str:
    (_, uhx, name) = lookupChar(char)
    if not keyStr:
        keyStr = ""
    return keyStr + ': "' + char + '" ' + uhx + ' # ' + name


baseURL = 'http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input='


def charLookupURL(char: str) -> str:
    return baseURL + char + '&mode=char'


def hexLookupURL(hx: str) -> str:
    return baseURL + hx + '&mode=hex'


def scrapeURL(URL: str) -> ChrUhexName:
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


def lookupCharWeb(char: str) -> ChrUhexName:
    return scrapeURL(charLookupURL(char))


def char2XCLineWeb(char: str, keyStr=None) -> str:
    (_, uhx, name) = lookupCharWeb(char)
    if not keyStr:
        keyStr = ""
    return keyStr + ': "' + char + '" ' + uhx + ' # ' + name
