"""
Verify correct system locale
"""
import sys
import locale


def sys_locale_check():

    # Supported locale
    supportedlocale = 'UTF-8'

    loc = locale.getlocale()

    errordict = {"error": False, "errormessage": None}

    if not loc[1] or 'UTF-8' not in loc[1]:
        if loc[1]:
            errordict["errormessage"] = ('Error: dbbbot only functions on ' + str(supportedlocale) + " locale. You are running a non-UTF8 locale environment")
        else:
            errordict["errormessage"] = ('Error: dbbbot only functions on ' + str(supportedlocale) + " locale. Your locale is not set?")
        errordict["error"] = True
    else:
        errordict["errormessage"] = ('Success: Locale is set to ' + str(loc[1]))

    return errordict
