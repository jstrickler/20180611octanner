#!/usr/bin/env python
import smtplib # <1>

DEBUG = True # set to false for production

smtp_user = 'jstrickpython'
smtp_pwd = 'python(monty)'

sender = 'jstrick@mindspring.com'
recipients = ['jstrickler@gmail.com']
msg = '''Subject: SMTP example
Hello hello?
Testing email from Python
'''

smtpserver = smtplib.SMTP("smtpcorp.com", 2525) # <2>
smtpserver.login(smtp_user, smtp_pwd)  # <3>
smtpserver.set_debuglevel(DEBUG) # <4>

try:
    smtpserver.sendmail(
        sender,
        recipients,
        msg
    )   # <5>
except Exception as e:
    print("Unable to send mail:", e)
finally:
    smtpserver.quit()   # <6>
