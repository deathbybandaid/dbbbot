"""
dbbbot
"""

# Common functions
from dbbbot.common import *

print (corememory)
corememory["test"] = 5
print (corememory)

# perform environment checks
import dbbbot.env_check

# Check for, and handle CLI arguments
import dbbbot.args_handler

dprint("Script complete")
