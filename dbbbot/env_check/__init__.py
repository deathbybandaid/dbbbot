"""
dbbbot
"""

# Common functions
from dbbbot.common import *

import sys

from .py_v_check import py_v_check
versionsuccess = py_v_check()
if versionsuccess["errormessage"]:
    dprint(versionsuccess["errormessage"])
if versionsuccess["error"]:
    sys.exit(1)