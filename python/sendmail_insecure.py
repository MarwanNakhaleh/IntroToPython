'''
This application requires you to turn on access for less secure apps. If you want to send email without leaving yourself vulnerable, refer to https://developers.google.com/gmail/api/quickstart/python
'''
import smtplib
import sys, os

smtpObj = None
# SMTP port for Gmail is either 587 or 465
try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
except:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 465)
    
if smtpObj == None:
    print('unable to make SMTP object')
    sys.exit()

smtpObj.starttls() # puts the connection in TLS (Transport Layer Security) mode to encrypt SMTP commands
smtpObj.ehlo() # identifies you to an SMTP server, should be done after starting TLS connection
smtpObj.login('mnakhaleh@gmail.com', os.environ['MAIN_GMAIL_PASSWORD']) # no peeking at my password!
smtpObj.sendmail(from_addr='mnakhaleh@gmail.com', to_addrs='mnakhaleh@gmail.com', msg='Subject: So long.\nDear Marwan, so long and thanks for all the fish. Sincerely, Marwan') # send the email
smtpObj.quit() # kill the SMTP session and close the connection