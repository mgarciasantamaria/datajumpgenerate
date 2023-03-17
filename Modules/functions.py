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
    msg['To'] = ['ingenieriavod@vcmedios.com.co']
    conexion = smtplib.SMTP(host='10.10.122.17', port=25)
    conexion.ehlo()
    conexion.send_message(msg)
    conexion.quit()

