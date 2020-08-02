import foldercreator
import os


exttoadd=input('extension => ')
grptoadd=input('group => ')
newbase=0

# ONLY for adding the new group name in the folderlist of foldercreator.py
# does not touch any other code
if grptoadd not in foldercreator.defaultfolders:
    
    print('Not in Base')

    # changes newbase for the following code
    newbase=1

    # creates an absolute path from relative path
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './foldercreator.py')

    eb=open(filename,'r')
    eblines=eb.readlines()

    # finding the line to modify
    for i in range(len(eblines)):
        if eblines[i].find('#default')!=-1:
            modlinepos=i
            break

    #creates the new modified version of the line
    linetorep=eblines[modlinepos]
    endbracpos=linetorep.find(']')
    newline=linetorep[:endbracpos]+',\''+grptoadd+'\''+linetorep[endbracpos:]

    #replaces the line
    eblines[modlinepos]=newline
    eb.close()

    #writes the changes to the file
    eb = open(filename,'w')
    eblines = "".join(eblines)
    eb.write(eblines)
    eb.close()



if newbase==0: #if the required group already exists
    #opens the extensionbase and adds the extension to ALREADY existing group

    # creates an absolute path from relative path
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './extensionbase.py')

    eb=open(filename,'r')
    eblines=eb.readlines()

    # finds the group and the line to be modified
    for i in range(len(eblines)):
        if eblines[i].find(grptoadd)!=-1:
            modlinepos=i
            break

    #creates the new modified version of the line
    linetorep=eblines[modlinepos]
    endbracpos=linetorep.find(']')
    newline=linetorep[:endbracpos]+',\''+exttoadd+'\''+linetorep[endbracpos:]

    #replaces the line with the modified line
    eblines[modlinepos]=newline
    eb.close()

    # writes the changes to the file
    eb = open(filename,'w')
    eblines = "".join(eblines)
    eb.write(eblines)
    eb.close()

    print(' $ MODIFIED EXTENSION BASE')

else: # adding new code for NEW groups

    # EXTENSION BASE MODIFIENG

    # creates an absolute path from relative path
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './extensionbase.py')

    # creating the new group line
    newline=grptoadd+'extension=[\''+ exttoadd +'\']#'+grptoadd+'\n'

    eb = open(filename,'a')
    # appends the new line
    eb.write(newline)
    eb.close()

    print(' $ MODIFIED EXTENSION BASE')


    # SORTER MODIFIENG

    # creates an absolute path from relative path
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './sorter.py')

    eb=open(filename,'r')
    eblines=eb.readlines()

    # finds the add here comment in sorter.py
    for i in range(len(eblines)):
        if eblines[i].find('#add here')!=-1:
            modlinepos=i
            break

    #new modified line
    #multiple lines because needed
    newline1="    elif ext in extensionbase."+grptoadd+"extension:\n"
    newline2="        finalpath=basefolder+'/"+grptoadd+"'+findname(i)\n"
    newline3="        cutpaste(i,finalpath)\n"


    #inserts modified code
    eblines.insert(modlinepos,newline3)
    eblines.insert(modlinepos,newline2)
    eblines.insert(modlinepos,newline1)
    eb.close()

    # writes changes
    eb = open(filename,'w')
    eblines = "".join(eblines)
    eb.write(eblines)
    eb.close()

    print(' $ MODIFIED SORTER PROGRAM')


    # FOLDER CREATOR SCRIPT MODIFIENG

    # creates an absolute path from relative path
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './foldercreator.py')

    eb=open(filename,'r')
    eblines=eb.readlines()

    # finds the add here comment in foldercreator.py
    for i in range(len(eblines)):
        if eblines[i].find('#add here')!=-1:
            modlinepos=i
            break

    #new modified line
    #multiple lines because needed
    newline1="if (basefolder+'/"+grptoadd+"') not in listfolders:\n"
    newline2="  os.mkdir(basefolder+'/"+grptoadd+"')\n"

    #inserts modified code
    eblines.insert(modlinepos,newline2)
    eblines.insert(modlinepos,newline1)
    eb.close()

    #writes changes
    eb = open(filename,'w')
    eblines = "".join(eblines)
    eb.write(eblines)
    eb.close()

    print(' $ MODIFIED FOLDERCREATOR SCRIPT')

