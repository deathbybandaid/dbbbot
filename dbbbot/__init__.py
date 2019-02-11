"""
dbbbot
"""
import sys

if sys.version_info != (3, 6):
    stderr('Error: Requires Python 3.6 or later.')
    sys.exit(1)

from Mammals import Mammals
