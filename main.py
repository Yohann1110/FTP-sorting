# Import modules
import ftplib
import fnmatch
import os
from allFunction import findpoint_, removeFolderFromList
from methods import connection

# Connect to ftp via method
ftp = connection()

# List folders and directory .nlst returns name of files and directories of list type
dirList = ftp.nlst()

#if there is no directory, creation of all the new directory
if not "image" in dirList:
    FtpImage = ftp.mkd("image")
    FtpDocument = ftp.mkd("document")
    ftpNote = ftp.mkd("note")
    ftpErreur = ftp.mkd("erreur")
    ftpDivers = ftp.mkd("divers")

#remove the folder from the list
removeFolderFromList(dirList)
dirList.remove('.')
dirList.remove('..')

allDivers = []
allErrors = []

#Entering the filter stage
for file in dirList:
    if fnmatch.fnmatch(file, '*.jpg'):
        ftp.rename(file, "/image/" + file)
    if fnmatch.fnmatch(file, '*.png'):
        ftp.rename(file, "/image/" + file)
    if fnmatch.fnmatch(file, '*.jpeg'):
        ftp.rename(file, "/image/" + file)
    if fnmatch.fnmatch(file, '*.docx'):
        ftp.rename(file, "/document/" + file)
    if fnmatch.fnmatch(file, '*.xlsx'):
        ftp.rename(file, "/document/" + file)
    if fnmatch.fnmatch(file, '*.pptx'):
        ftp.rename(file, "/document/" + file)
    if fnmatch.fnmatch(file, '*.txt'):
        ftp.rename(file, "/note/" + file)

dirList = ftp.nlst()
removeFolderFromList(dirList)
dirList.remove('.')
dirList.remove('..')

for file in dirList:
    if findpoint_(file):
        allDivers.append(file)
    else :
        allErrors.append(file)

for file in allDivers:
    destination_folder = "/divers/"
    destination        = destination_folder + file
    ftp.rename(file, destination )

for file in allErrors:
    destination_folder = "/erreur/"
    destination        = destination_folder + file
    ftp.rename(file, destination )

ftp.quit()


