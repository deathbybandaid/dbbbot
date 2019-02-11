"""
dbbbot
"""

# Common functions
import dbbbot.common

import sys

from .py_v_check import py_v_check
versionsuccess = py_v_check()
if versionsuccess["errormessage"]:
    print (versionsuccess["errormessage"])
if versionsuccess["error"]:
    sys.exit(1)
