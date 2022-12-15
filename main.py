# Import modules
import ftplib       #ftp connection module
import fnmatch      #test whether the filename string matches the pattern string module
import os
from email.message import EmailMessage

from allFunction import findpoint_, removeFolderFromList, renameFileText
from methods import connection
import smtplib      #sending mail module
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
    if fnmatch.fnmatch(file, '*.jpg'):              #If the file extension is .jpg send it to "image" folder
        ftp.rename(file, "/image/" + file)
    if fnmatch.fnmatch(file, '*.png'):              #If the file extension is .png send it to "image" folder
        ftp.rename(file, "/image/" + file)
    if fnmatch.fnmatch(file, '*.jpeg'):             #If the file extension is .jpeg send it to "image" folder
        ftp.rename(file, "/image/" + file)
    if fnmatch.fnmatch(file, '*.docx'):             #If the file extension is .docx send it to "document" folder
        ftp.rename(file, "/document/" + file)
    if fnmatch.fnmatch(file, '*.xlsx'):             #If the file extension is .xlsx send it to "document" folder
        ftp.rename(file, "/document/" + file)
    if fnmatch.fnmatch(file, '*.pptx'):             #If the file extension is .pptx send it to "document" folder
        ftp.rename(file, "/document/" + file)
    if fnmatch.fnmatch(file, '*.txt'):              #If the file extension is .txt rename + send it to "note" folder
        lines = []
        ftp.retrlines("RETR " + file, lines.append) #put the contents of the txt file into a string
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

#if the file has a non recognised extension we send it to "divers" folder
for file in allDivers:
    destination_folder = "/divers/"
    destination        = destination_folder + file
    ftp.rename(file, destination )

#if the file has no extension we send it to "erreur" folder
for file in allErrors:
    destination_folder = "/erreur/"
    destination        = destination_folder + file
    ftp.rename(file, destination )

# Send the mail for the erreurs and divers

if allDivers or allErrors:
    # Method to send mail
    fileName = ""
#We recover the name of the file sent in the "divers" folder
    for file in allDivers:
        fileName += "- "
        fileName += file
        fileName += "\n"

    fileName2 = ""
#We recover the name of the file sent in the "erreur" folder
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


