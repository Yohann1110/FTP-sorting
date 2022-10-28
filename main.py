# Import modules
from ast import Delete
import ftplib
import glob
import fnmatch
from tkinter.tix import IMAGETEXT
import os

# Connection Information
host = "d73kw.ftp.infomaniak.com"
username = "d73kw_proj1_group2_lin"
password = "jyDK33a9xY6n"

# Connection to FTP Server
ftp = ftplib.FTP(host, username, password)
ftp.encoding = "utf-8"
#ftp.cwd('in')

# Creation of directory

# List folders and directory .nlst returns name of files and directories of list type
dirList = ftp.nlst()

if not "image" in dirList:
    FtpImage = ftp.mkd("image")
    FtpDocument = ftp.mkd("document")
    ftpNote = ftp.mkd("note")
    ftpErreur = ftp.mkd("erreur")
    ftpDivers = ftp.mkd("divers")

filteredList    = []
allError        = []
allImage        = []
allDivers       = []

# Move folders in the correct directory

#ajout des documents à traiter, si il n'y pas de point alors il n'y a pas d'extentsion et donc c'est une erreur
for z in dirList:
    for i in list(z):
        if i == ".":
            filteredList.append(z)
        else :
            allError.append(z)

print("Entering the filter stage")

for file in filteredList: 
    if fnmatch.fnmatch(file, '*.jpg'):
        ftp.rename(file, "/image/" + file)
        #ftp.delete(file)
 
print("end") 
ftp.quit()