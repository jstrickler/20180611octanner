#!/usr/bin/env python
import smtplib
import os
from email.mime.multipart import MIMEMultipart  # <1>
from email.mime.text import MIMEText # <2>
from email.mime.image import MIMEImage # <3>

SMTP_SERVER = "smtpcorp.com"
SMTP_PORT = 2525
SMTP_USER = 'jstrickpython'
SMTP_PWD = 'python(monty)'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']

def main():   # <4>
    smtp_server = create_smtp_server()
    msg = create_message(
        'Here is your attachment',
        'Testing email attachments from python class.',
    )
    add_text_attachment('../DATA/parrot.txt', msg)
    add_image_attachment('../DATA/felix_auto.jpeg', msg)
    send_message(smtp_server, msg)


def create_message(subject, body):
    msg = MIMEMultipart(body)  # <5>
    msg['Subject'] = subject   # <6>

    return msg

def add_text_attachment(file_name, message): # <7>
    add_attachment(file_name, message, MIMEText, 'r')

def add_image_attachment(file_name, message): # <8>
    add_attachment(file_name, message, MIMEImage, 'rb')

def add_attachment(file_name, message, mime_type, file_mode):
    with open(file_name, file_mode) as file_in:  # <9>
        attachment_data = file_in.read()

    short_name = os.path.basename(file_name)
    attachment = mime_type(attachment_data)  # <10>
    attachment.add_header(
        'Content-Disposition', 'attachment', filename=short_name
    )

    message.attach(attachment)   # <11>

def create_smtp_server():
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) # <12>
    smtpserver.login(SMTP_USER, SMTP_PWD)

    return smtpserver

def send_message(server, message):
    try:
        server.sendmail(
            SENDER,
            RECIPIENTS,
            message.as_string() # <13>
        )
    finally:
        server.quit()

if __name__ == '__main__':
    main()
