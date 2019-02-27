import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
    
    
def send_email(fromaddr,toaddr,msgsubject,body,smtpServer,smtpUsername,smtpPassword):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = msgsubject

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP(smtpServer, 2525)
    server.starttls()
    server.login(smtpUsername, smtpPassword)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
