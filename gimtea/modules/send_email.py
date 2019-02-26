import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
    
    
def send_email(fromaddr,toaddr,msgsubject,body,smtpPassword):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = msgsubject

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('mail.smtp2go.com', 2525)
    server.starttls()
    server.login(smtpUsername, smtpPassword)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
fromaddr = "luka@gmail.com"
smtpUsername = "bvscott66@gmail.com"
smtpPassword = "BYvDfO6t7oZo"
toaddr = "bvscott66@gmail.com"
msgsubject = "Alert Test"
instrumentID = "Piezometer01"
body = """""
<html>
        <head>
        <style>
            body{
            font-family: Arial, sans-serif;
        }
        </style>
        </head>
        <body>        
        <p>Instrument %s is in alarm<br>
            Details can be found <a href="http://www.python.org">here</a>.
        </p>
        </body>
</html>
""" %(instrumentID)

send_email(fromaddr,toaddr,msgsubject,body,smtpPassword)
