#importing neccessary mods

from cutfunc import cutpaste #local module to cut and paste
from pathhelp import findname #local module for all filename related ops
from pathhelp import findpath #local module for all filename related ops
from pathhelp import findextension #local module for all filename related ops
import glob #to list all files
import extensionbase #local database mod of all sort groups
import foldercreator #local python script which creates all folders needed asper existence


basefolder=foldercreator.basefolder

#lists all files and no folders
listfiles=glob.glob(basefolder+"/*.*")


for i in listfiles:
    
    ext=findextension(i)

    if ext in extensionbase.textextension:
        finalpath=basefolder+'/Text'+findname(i)
        cutpaste(i,finalpath)
    

    elif ext in extensionbase.Executablesextension:
        finalpath=basefolder+'/Executables'+findname(i)
        cutpaste(i,finalpath)
    
    #add here
    #for adder.py

    elif ext in extensionbase.picturesextension:
        finalpath=basefolder+'/Pictures'+findname(i)
        cutpaste(i,finalpath)

    elif ext in extensionbase.vidextension:
        finalpath=basefolder+'/Videos'+findname(i)
        cutpaste(i,finalpath)

    else:
        finalpath=basefolder+'/Misc'+findname(i)
        cutpaste(i,finalpath)





