"""
dbbbot
"""

# Common functions
from dbbbot.common import *

import sys

from .py_v_check import py_v_check
versionsuccess = py_v_check()
if versionsuccess["errormessage"]:
    dprint(versionsuccess["errormessage"], color=dprint_error_color(versionsuccess["error"]))
if versionsuccess["error"] and versionsuccess["error"] != "WARN":
    sys.exit(1)


from .sys_locale_check import sys_locale_check
localesuccess = sys_locale_check()
if localesuccess["errormessage"]:
    dprint(localesuccess["errormessage"], color=dprint_error_color(localesuccess["error"]))
if localesuccess["error"] and localesuccess["error"] != "WARN":
    sys.exit(1)
