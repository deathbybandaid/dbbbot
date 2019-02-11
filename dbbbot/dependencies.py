"""
Verify all dependencies are met
"""
import sys


def dependencies():

    errordict = dict()

    # Check Python version is the supported version
    print (sys.version_info)
    if sys.version_info != (3, 5):
        print ('Error: Testing for dbbbot has only been done on python version 3.5')
        return errordict
    else:
        print ('Success: Python version is good')
