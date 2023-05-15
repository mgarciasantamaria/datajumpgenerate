#!/usr/bin/env python
#_*_ codig: utf8 _*_
import smtplib, json
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

def Flag_Status(OPTION):
    with open(json_path, "r") as json_file:
            json_data=json.load(json_file)
    if OPTION=="r":
        return json_data["FLAG"]
    elif OPTION=="w":
        json_data["FLAG"]=False
        with open(json_path, "w") as json_file:
            json.dump(json_data, json_file)
    else:
        pass