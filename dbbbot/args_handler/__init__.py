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
argv = sys.argv[1:] or []

if argv != []:

    print (parser)
    opts = parser.parse_args(argv)

    if opts.version:
        dprint("beta testing")

else:
    dprint("Not arguments passed, continuing.", color="GREEN")

dprint("")
