from smtplib import SMTP_SSL as SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os.path

def attach_pdf(phoneNumber):
    
    body = '''Hello Sir,

    Please Find below the signed NDA Pdf  
    
    Thank you
    Ajit Padyal
    '''
    # put your email here
    sender = 'ajit@cinegencemedia.com'
    # get the password in the gmail (manage your google account, click on the avatar on the right)
    # then go to security (right) and app password (center)
    # insert the password and then choose mail and this computer and then generate
    # copy the password generated here
    password = 'Password@312345'
    # put the email of the receiver here
    receiver = 'stephen@cinegencemedia.com'
        
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Signed NDA Pdf'
        
    message.attach(MIMEText(body, 'plain'))
    
    
    

    pdfname = 'C:/signed_nda/' + f'{phoneNumber}' + '.pdf'
    
        
    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')
    
        
        
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())
        
    # enconding the binary into base64
    encoders.encode_base64(payload)
        
    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)
        
    #use gmail with port
    session = SMTP('mail.cinegencemedia.com',465)
        
    #enable security
    session.set_debuglevel(False)
        
    #login with mail_id and password
    session.login(sender, password)
        
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    binary_pdf.close()
    




