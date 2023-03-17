#!/usr/bin/env python
#_*_ codig: utf8 _*_
import smtplib
from email.message import EmailMessage 
from Modules.Constants import *
        
def Send_Mail(text, Subject):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = Subject
    msg['From'] = 'alarmas-aws@vcmedios.com.co'
    msg['To'] = Mail_to
    conexion = smtplib.SMTP(host='10.10.130.217', port=25)
    conexion.ehlo()
    conexion.send_message(msg)
    conexion.quit()

