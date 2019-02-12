"""
dbbbot
"""

# Common functions
from dbbbot.common import *

import sys
import getopt

dprint_divider(color='BLUE')

dprint(["Checking For CLI Arguments", ""])


inputfile, outputfile = '', ''
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
except getopt.GetoptError:
    print ('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
print ('Input file is "', inputfile)
print ('Output file is "', outputfile)

dprint("")
