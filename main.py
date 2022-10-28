# Import modules
import ftplib
import os

# Connection Information
host = "d73kw.ftp.infomaniak.com"
username = "d73kw_proj1_group2_lin"
password = "jyDK33a9xY6n"

# Connection to FTP Server
ftp = ftplib.FTP(host, username, password)
ftp.encoding = "utf-8"

# Creation of directory if directory doesn't already exist
ListAll = ftp.nlst()
if not "image" in ListAll:
    ftp.mkd("image")
    ftp.mkd("document")
    ftp.mkd("note")
    ftp.mkd("erreur")
    ftp.mkd("divers")

# Move folders in the correct directory
# ftp.rename("cafe.png", "/image/cafe.png")

# List folders and directory
ftp.dir()
