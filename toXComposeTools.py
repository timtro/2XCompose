import unicodedata
from typing import Tuple, NewType
import requests
from bs4 import BeautifulSoup

UniTriple = NewType('UniTriple', Tuple[str, str, str])


def hexCodePt(char: str) -> str:
    assert len(char) == 1, 'Must look up single characters.'
    return 'U'+'%04X' % ord(char)


def charXCInfo(char: str) -> UniTriple:
    try:
        charname = unicodedata.name(char)
    except:
        charname = "ERR: Name not found"

    return (char,
            hexCodePt(char),
            charname)


def char2XC(char: str, keyStr=None) -> str:
    chDat = charXCInfo(char)
    if not keyStr:
        keyStr = ""
    return keyStr + ': "' + chDat[0] + '" ' + chDat[1] + ' # ' + chDat[2]


baseURL = 'http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input='


def charLookupURL(char: str) -> str:
    return baseURL + char + '&mode=char'


def scrapeURL(URL: str) -> UniTriple:
    response = requests.get(URL)
    infoTRs = BeautifulSoup(response.text, 'html.parser').findAll('tr')
    charData = {}
    for row in infoTRs:
        cells = row.findAll('td')
        charData[cells[0].find(text=True)] = cells[1].find(text=True)
    if charData['Character name'] == None:
        charData['Character name'] = "ERR: Name not found"
    return (charData['Character'],
            charData['Hex code point'],
            charData['Character name'])


def charXCInfoWeb(char: str) -> UniTriple:
    return scrapeURL(charLookupURL(char))


def char2XCWeb(char: str, keyStr=None) -> str:
    chDat = charXCInfoWeb(char)
    if not keyStr:
        keyStr = ""
    return keyStr + ': "' + chDat[0] + '" U' + chDat[1] + ' # ' + chDat[2]
