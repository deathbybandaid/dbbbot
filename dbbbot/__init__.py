"""
dbbbot
"""

# Common functions
from dbbbot.common import *

corememory = corememoryclass()

print (corememory)

# perform environment checks
import dbbbot.env_check

# Check for, and handle CLI arguments
import dbbbot.args_handler

dprint("Script complete")
