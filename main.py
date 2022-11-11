# Import modules
import ftplib
import fnmatch
import os
from email.message import EmailMessage

from allFunction import findpoint_, removeFolderFromList, renameFileText
from methods import connection
import smtplib
from methods import mail, email_adress


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
        lines = []
        ftp.retrlines("RETR " + file, lines.append) #place le contenu du fichier txt dans un string
        myString=renameFileText(lines)
        ftp.rename(file, "/note/" + myString + ".txt")


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

# Send the mail for the erreurs and divers

if allDivers or allErrors:
    # Method to send mail
    fileName = ""

    for file in allDivers:
        fileName += "- "
        fileName += file
        fileName += "\n"

    fileName2 = ""

    for file in allErrors:
        fileName2 += "- "
        fileName2 += file
        fileName2 += "\n"

    msg = EmailMessage()
    msg['Subject'] = 'Divers et Erreurs : '
    msg['From'] = 'yoch5000@gmail.com'
    msg['To'] = 'yoch2000@gmail.com'
    msg.set_content(f"\nLes extensions pour les fichiers suivants ne sont pas encore enregistrées :\n{fileName}ces fichiers seront stockés dans le dossier 'divers'.\n\n" \
           f"Il y'a eu une erreur pour les fichiers :\n{fileName2}qui seront stockés dans le dossier 'erreur'.")

    try:
        send = mail()
        send.send_message(msg)
        send.close()

    except Exception as ex:
        print("Something went wrong for the email : ", ex)

else:
    pass

ftp.quit()


