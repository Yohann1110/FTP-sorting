import ftplib

# Connection to FTP Server
def connection():
    ftp = ftplib.FTP(host, username, password)
    ftp.encoding = "utf-8"
    return ftp
