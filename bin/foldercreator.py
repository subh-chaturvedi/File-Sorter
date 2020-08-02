# Python script to create folders on a requirement basis
# Will create the folder IF it doesnt exist

import os
from os import listdir
from os.path import isfile, join



# obtains the path from pathbase file
pathie=open("pathbase.txt",'r')
basefolderlist=pathie.readlines()
basefolder=basefolderlist[0]
pathie.close


listfolders = []

# lists all files/folders in the base folder
for f in listdir(basefolder):
    listfolders.append(join(basefolder, f))

# A list of all the folders that will be created
# Used by adder.py
defaultfolders=['Pictures','Text','Videos','Misc','Executables']#default

# removes all files from listfolders
# because when we created the list it also included all the files
for i in listfolders:
    if i.find('.')!=-1:
        listfolders.remove(i)

# print(listfolders)

# checks the existence of folder and creates it if it doesnt exist
if (basefolder+'/Pictures') not in listfolders:
    os.mkdir(basefolder+'/Pictures')

if (basefolder+'/Text') not in listfolders:
    os.mkdir(basefolder+'/Text')

if (basefolder+'/Videos') not in listfolders:
    os.mkdir(basefolder+'/Videos')

if (basefolder+'/Misc') not in listfolders:
    os.mkdir(basefolder+'/Misc')

if (basefolder+'/Executables') not in listfolders:
  os.mkdir(basefolder+'/Executables')
#add here
#for adder.py.


















