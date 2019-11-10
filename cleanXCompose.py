#!/usr/bin/env python3

from argparse import ArgumentParser
from toXComposeTools import charXCInfo, char2XC, char2XCWeb
from functools import partial


def main(xComposeFilePath, charInfoGetter):

    with open(xComposeFilePath) as XCFile:
        XCLines = XCFile.readlines()

    lineProcessor = partial(processLine, charInfoGetter)
    processAndPrint = lambda line : print(lineProcessor(line))
    newXCLines = list(filter(None, map(processAndPrint, XCLines)))


def processLine(charInfoGetter, line):
    """
    process lines of form
        <SOME> <KEYS> : "C" # BLAH
    returning the line linted using "C" as the key for unicode lookup.
    """
    if not line or line == "\n":
        return "\n"
    if is_comment(line) or is_include(line):
        return line.strip()
    [keys, charData] = line.split(":")
    uniChar = charData.strip().split('"')[1]

    return keys + charInfoGetter(uniChar)


def is_include(str):
    if "include" in str:
        return True
    else:
        return False


def is_comment(str):
    if str[0] == '#':
        return True
    else:
        return False


if __name__ == '__main__':
    args = ArgumentParser(
        description="Removes extraneous spaces, verifies hex codes, \
            inserts descriptions from XCompose file")

    args.add_argument('filepath', type=str, help='Path to XCompose file')
    args.add_argument('-w', '--web',
                      action='store_true',
                      help='Use Internet resources to obtain \
                unicode character data.')

    args = args.parse_args()

    if args.web:
        charInfoGetter = char2XCWeb
    else:
        charInfoGetter = char2XC

    main(args.filepath, charInfoGetter)
