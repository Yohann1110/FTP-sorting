# Import modules
import ftplib

# Connection Information
host = "d73kw.ftp.infomaniak.com"
username = "d73kw_proj1_group2_lin"
password = "jyDK33a9xY6n"

# Connection to FTP Server
ftp = ftplib.FTP(host, username, password)
ftp.encoding = "utf-8"

# Creation of directory
FtpImage = ftp.mkd("image")
FtpDocument = ftp.mkd("document")
ftpNote = ftp.mkd("note")
ftpErreur = ftp.mkd("erreur")
ftpDivers = ftp.mkd("divers")

# Move folders in the correct directory


# List folders and directory
ftp.dir()

