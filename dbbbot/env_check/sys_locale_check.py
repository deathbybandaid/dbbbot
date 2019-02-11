"""
Verify correct system locale
"""
import sys
import locale


def sys_locale_check():

    # Supported locale
    supportedlocale = 'UTF-8'

    loc = locale.getlocale()
    print (loc)

    errordict = {"error": False, "errormessage": None}

    if not loc[1] or supportedlocale not in loc[1]:
        errordict["errormessage"] = ('Error: dbbbot only functions on ' + str(supportedlocale) + " locale. You are running a non-" + str(supportedlocale) + " locale environment")
        errordict["error"] = True
    else:
        errordict["errormessage"] = ('Success: Locale is set to ' + str(loc[1]))

    return errordict
