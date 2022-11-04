import ftplib

# Connection Information
host = "d73kw.ftp.infomaniak.com"
username = "d73kw_proj1_group2_lin"
password = "oN687W8MLKQB"


# Connection to FTP Server
def connection():
    ftp = ftplib.FTP(host, username, password)
    ftp.encoding = "utf-8"
    return ftp
