"""
dbbbot
"""

# Common functions
from dbbbot.common import *

import sys
import argparse


def build_parser():
    """Build an ``argparse.ArgumentParser`` for the bot"""

    parser = argparse.ArgumentParser(description='dbbbot', usage='%(prog)s [options]')

    parser.add_argument('-v', '--version', action="store_true", dest="version", help="Show version number and exit")

    return parser


dprint_divider(color='BLUE')

dprint(["Checking For CLI Arguments", ""])

parser = build_parser()
opts = parser.parse_args(sys.argv[1:] or None)
if opts.version:
    dprint(class_directory(opts))

dprint("")


def class_directory(inputclass):

    # make sure input is a class
    if not isinstance(inputclass, class):
        return []

    classdirlistfull, classdirlistclean = dir(inputclass), []
    for classdiritem in classdirlistfull:
        if not classdiritem.startswith("_"):
            classdirlistclean.append(classdiritem)
    return classdirlistclean
