"""
Verify correct python version
"""

# Common functions
from dbbbot.common import *

import sys


def py_v_check():

    # Supported Python Version
    python_version_major_sup, python_version_minor_sup = 3, 5
    python_version_major_act, python_version_minor_act = sys.version_info[0], sys.version_info[1]
    corememory["env"]["python"] = str(python_version_major_act) + "." + str(python_version_minor_act)

    errordict = {"error": False, "errormessage": None}

    # Check Python version is the supported version
    if python_version_major_act != python_version_major_sup or python_version_minor_act >= python_version_minor_sup:
        errordict["errormessage"] = ('Error: dbbbot only functions on ' + str(python_version_major_sup) + "." + str(python_version_minor_sup) + " Your version is " + corememory["env"]["python"])
        errordict["error"] = True
    else:
        errordict["errormessage"] = ('Success: Python version is ' + corememory["env"]["python"])

    return errordict
