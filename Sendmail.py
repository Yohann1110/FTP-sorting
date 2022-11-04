import smtplib

# Email account with the 2FA authentication
email_adress = "yoch5000@gmail.com"
password = "yapxbpbjykphvrbg"

# Destination mail
destination = "yoch2000@gmail.com"

# Text of the mail
text = "Test de merde"


try:

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    smtp_server.ehlo()

    smtp_server.login(email_adress, password)

    smtp_server.sendmail(email_adress, destination, text)

    smtp_server.close()

    print ("Email sent successfully!")

except Exception as ex:

    print ("Something went wrong….",ex)



