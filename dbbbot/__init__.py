"""
dbbbot
"""
import sys

# Check Python version is the supported version
if sys.version_info != (3, 6):
    print ('Error: Requires Python 3.6 or later.')
    sys.exit(1)

from Mammals import Mammals
