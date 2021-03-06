import sys
import threading

"""
Memory
"""


class corememoryclass(dict):

    """A simple thread-safe dict implementation.
    In order to prevent exceptions when iterating over the values and changing
    them at the same time from different threads, we use a blocking lock on
    ``__setitem__`` and ``contains``.
    """
    def __init__(self, *args):
        dict.__init__(self, *args)
        self.lock = threading.Lock()

    def __setitem__(self, key, value):
        self.lock.acquire()
        result = dict.__setitem__(self, key, value)
        self.lock.release()
        return result

    def __contains__(self, key):
        """Check if a key is in the dict.
        It locks it for writes when doing so.
        """
        self.lock.acquire()
        result = dict.__contains__(self, key)
        self.lock.release()
        return result

    def contains(self, key):
        return self.__contains__(key)


corememory = corememoryclass()


"""
Display Functions
"""


def dprint_divider(color='BOLD'):

    dprint(textarray=["___________________________________________________________"], color=color)


def dprint(textarray=[], indent=0, color='BOLD'):

    if not isinstance(textarray, list):
        textarray = [str(textarray)]

    if len(textarray) == 0:
        return

    try:
        coloreval = eval('bcolors.' + color.upper())
        endcolor = bcolors.ENDC
    except AttributeError:
        coloreval = ''
        endcolor = ''

    for entry in textarray:
        indentstr = ''
        if indent:
            if not isinstance(indent, int):
                indent = 1
            indentstr = "     " * indent
        print (indentstr + coloreval + entry + endcolor, file=sys.stderr)


def dprint_error_color(color_input):
    if color_input:
        if color_input == "WARN":
            return "YELLOW"
        else:
            return "RED"
    else:
        return "GREEN"


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


"""
Classes
"""


def class_create(classname):
    compiletext = """
        def __init__(self):
            self.default = str(self.__class__.__name__)
        def __repr__(self):
            return repr(self.default)
        def __str__(self):
            return str(self.default)
        def __iter__(self):
            return str(self.default)
        pass
        """
    exec(compile("class class_" + str(classname) + ": " + compiletext, "", "exec"))
    newclass = eval('class_'+classname+"()")
    return newclass


def class_directory(inputclass):

    classdirlistfull, classdirlistclean = dir(inputclass), []
    for classdiritem in classdirlistfull:
        if not classdiritem.startswith("_"):
            classdirlistclean.append(classdiritem)
    return classdirlistclean
