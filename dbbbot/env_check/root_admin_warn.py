"""
Check user running
"""
import sys
import os
import platform


def root_admin_warn():
    errordict = {"error": False, "errormessage": None}
    print (platform.system())
    print (os.name)

    return errordict


def extra():

    errordict = {"error": False, "errormessage": None}

    if not loc[1] or supportedlocale not in loc[1]:
        errordict["errormessage"] = ("Warning: dbbbot should not be run on root")
        errordict["error"] = "WARN"
    else:
        errordict["errormessage"] = ("Success: User is not root!")

    return errordict
