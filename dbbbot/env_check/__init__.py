"""
dbbbot
"""

# Common functions
from dbbbot.common import *

import sys

dprint_divider(color='BLUE')

dprint(["Performing Environment Checks", ""])

dprint("Checking Python Version")
from .py_v_check import py_v_check
versionsuccess = py_v_check()
if versionsuccess["errormessage"]:
    dprint(versionsuccess["errormessage"], color=dprint_error_color(versionsuccess["error"]))
if versionsuccess["error"] and versionsuccess["error"] != "WARN":
    sys.exit(1)
dprint("")

dprint("Checking System Locale")
from .sys_locale_check import sys_locale_check
localesuccess = sys_locale_check()
if localesuccess["errormessage"]:
    dprint(localesuccess["errormessage"], color=dprint_error_color(localesuccess["error"]))
if localesuccess["error"] and localesuccess["error"] != "WARN":
    sys.exit(1)
dprint("")


dprint("Checking Current User")
from .root_admin_warn import root_admin_warn
adminsuccess = root_admin_warn()
if adminsuccess["errormessage"]:
    dprint(adminsuccess["errormessage"], color=dprint_error_color(adminsuccess["error"]))
if adminsuccess["error"] and adminsuccess["error"] != "WARN":
    sys.exit(1)
dprint("")
