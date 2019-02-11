"""
dbbbot
"""
import sys

# Check Python version is the supported version
# print sys.version_info
if sys.version_info != (3, 5):
    print ('Error: Testing for dbbbot has only been done on python version 3.5')
    sys.exit(1)

from Mammals import Mammals
