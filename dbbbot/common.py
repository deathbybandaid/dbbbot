"""
Display Functions
"""


def dbb_avatar(dbbparse):
    filepath = os.path.join(dbbparse.paths['scripts_common'], 'avatar.txt')
    lines = [line.rstrip('\n') for line in open(filepath)]
    osd(textarray=lines)


def humanized_time(countdownseconds):
    time = float(countdownseconds)
    if time == 0:
        return "0 seconds"
    year = time // (365 * 24 * 3600)
    time = time % (365 * 24 * 3600)
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minute = time // 60
    time %= 60
    second = time
    displaymsg = None
    timearray = ['year', 'day', 'hour', 'minute', 'second']
    for x in timearray:
        currenttimevar = eval(x)
        if currenttimevar >= 1:
            timetype = x
            if currenttimevar > 1:
                timetype = str(x+"s")
            if displaymsg:
                displaymsg = str(displaymsg + " " + str(int(currenttimevar)) + " " + timetype)
            else:
                displaymsg = str(str(int(currenttimevar)) + " " + timetype)
    if not displaymsg:
        return "0 seconds"
    return displaymsg


def dividerbar(color='BOLD'):

    osd(textarray=["___________________________________________________________"], color='BOLD')


def osd(textarray=[], indent=0, color='BOLD'):

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
        print indentstr + coloreval + entry + endcolor
