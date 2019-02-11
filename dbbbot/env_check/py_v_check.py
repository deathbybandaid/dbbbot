"""
Verify correct python version
"""
import sys


def py_v_check():

    # Supported Python Version
    python_version_major, python_version_minor = 3, 9

    errordict = {"error": False, "errormessage": None}

    # Check Python version is the supported version
    if sys.version_info[0] != python_version_major or sys.version_info[1] != python_version_minor:
        errordict["errormessage"] = ('Error: dbbbot only functions on ' + str(python_version_major) + "." + str(python_version_minor) + " Your version is " + str(sys.version_info[0]) + "." + str(sys.version_info[1]))
        errordict["error"] = True
    else:
        errordict["errormessage"] = ('Success: Python version is ' + str(sys.version_info[0]) + "." + str(sys.version_info[1]))

    return errordict
