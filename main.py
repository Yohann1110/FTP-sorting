# Import modules
from ast import Delete
import ftplib
import glob
import fnmatch
from tkinter.tix import IMAGETEXT
import os
from connect import connection

# Connect to ftp via method
ftp = connection()

# Creation of directory

# List folders and directory .nlst returns name of files and directories of list type
dirList = ftp.nlst()

# Permet de controler si on a déjà créer les dossiers
if not "image" in dirList:
    FtpImage = ftp.mkd("image")
    FtpDocument = ftp.mkd("document")
    ftpNote = ftp.mkd("note")
    ftpErreur = ftp.mkd("erreur")
    ftpDivers = ftp.mkd("divers")

filteredList = []
allError = []
allImage = []
allDivers = []

# Entering the filter stage
for file in dirList:
    if fnmatch.fnmatch(file, '*.jpg'):
        ftp.rename(file, "/image/" + file)


# Filter for divers
#for z in dirList:
#    for i in list(z):
#        if i == ".":
#            ftp.rename(z, "/divers/" + z)
#        if z=="image" or z=="document" or z=="note" or z=="divers" or z=="erreur" :
#            pass
#        else  :
#            ftp.rename(z, "/erreur/" + z)

print("end")
ftp.quit()


