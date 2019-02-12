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

    parser.add_argument('-f', '--fart', action="store_true", dest="fart", help="makes the bot fart")

    return parser


dprint_divider(color='BLUE')

dprint(["Checking For CLI Arguments", ""])

parser = build_parser()
print (parser)
opts = parser.parse_args(sys.argv[1:] or None)

if opts.version:
    dprint("beta testing")

if opts.fart:
    dprint("farting now!")

dprint("")
