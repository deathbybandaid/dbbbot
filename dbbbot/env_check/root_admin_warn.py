"""
Check user running
"""

# Common functions
from dbbbot.common import *

import sys
import os
import platform


def root_admin_warn():
    errordict = {"error": False, "errormessage": None}

    # Detect operating system
    opersystem = platform.system()

    # Linux: Linux
    # Mac: Darwin
    # Windows: Windows

    if opersystem in ["Linux", "Darwin"]:
        if os.getuid() == 0 or os.geteuid() == 0:
            errordict["errormessage"] = ("Warning: dbbbot should not be run on root")
            errordict["error"] = "WARN"
        else:
            errordict["errormessage"] = ("Succese: dbbbot is not run on root")
    elif opersystem in ["Windows"]:
        if os.environ.get("USERNAME") == "Administrator":
            errordict["errormessage"] = ("Warning: dbbbot should not be run on administrator")
            errordict["error"] = "WARN"
        else:
            errordict["errormessage"] = ("Succese: dbbbot is not run on administrator")
    else:
        errordict["errormessage"] = ("ERROR: Could not detect Operating Sytem Type, or it is unsupported.")
        errordict["error"] = True

    return errordict
