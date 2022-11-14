import os
import math
import random
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
import sys
otp = 0
def send_otp(receivers_mail):
    global otp
    digits = '0123456789'
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]
    otp = OTP 

    email = receivers_mail

    try:
        msg = MIMEText(f'This is your otp: {otp}')
        msg['Subject'] = 'OTP Verification'
        msg['From'] = 'it@cinegencemedia.com'
        msg['To'] = email

        conn = SMTP('mail.cinegencemedia.com',465)
        conn.set_debuglevel(False)
        conn.login('it@cinegencemedia.com', 'Mikanos@31')
        try:
            conn.sendmail('it@cinegencemedia.com', email, msg.as_string())
        finally:
            conn.quit()

    except Exception as e:
        # sys.exit("mail failed; %s" % "CUSTOM ERROR") 
        print(e)
    