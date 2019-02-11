"""
Verify all dependencies are met
"""
import sys


def dependencies():

    # Supported Python Version
    python_version_major = 3
    python_version_minor = 5

    errordict = dict()

    # Check Python version is the supported version
    if sys.version_info[0] != python_version_major or sys.version_info[1] != python_version_minor:
        print ('Error: dbbbot only functions on ' + str(python_version_major) + "." + str(python_version_minor))
    else:
        print ('Success: Python version is ' + str(sys.version_info[0]) + "." + str(sys.version_info[1]))
