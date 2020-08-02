
#fullpath is the absolute path of the file

# finds the name of the file with the extension
# user/test/test/python.py becomes python.py
def findname(fullpath):
    start=0
    slashpos=0
    while True:
        if fullpath.find('/',start,len(fullpath))==-1:
            break
        slashpos=fullpath.find('/',start,len(fullpath))
        start=slashpos+1
    filename=fullpath[slashpos:]
    return filename

# finds the path of the file without the filename
# user/test/test/python.py becomes user/test/test
def findpath(fullpath):
    start=0
    slashpos=0
    while True:
        if fullpath.find('/',start,len(fullpath))==-1:
            break
        slashpos=fullpath.find('/',start,len(fullpath))
        start=slashpos+1
    pathname=fullpath[:slashpos]
    return pathname

# finds the extension of file
# user/test/test/python.py become .py
def findextension(fullpath):
    dotpos=fullpath.find('.')
    extname=fullpath[dotpos:]
    return extname


    