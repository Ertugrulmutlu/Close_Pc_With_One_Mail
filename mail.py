
import smtplib
import time
import imaplib 
import email
import traceback
import os



def Deneme(FROM_EMAIL,FROM_PWD):
    ORG_EMAIL = "@gmail.com" 
    

    FROM_EMAILa = FROM_EMAIL + ORG_EMAIL
    FROM_PWDa = FROM_PWD
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(FROM_EMAILa,FROM_PWDa)
        mail.select('inbox')

        data = mail.search(None,'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_mail_id = int(id_list[0])
        latest_mail_id = int(id_list[-1])

        data = mail.fetch(str(int(id_list[-1])), '(RFC822)')
        for response_part in data:
            arr = response_part[0]
            if isinstance(arr,tuple):
                msg = email.message_from_string(str(arr[1],'utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                #İf u change the 'Close' to anything u want, ıt means u can change the key word
                if email_subject == "Close":
                    #İf u change that line u can do anything
                    os.system("shutdown /s /t 1")

                else:
                    pass

    except Exception as e:
        pass

print("Write the e mail which u want to control when program working !!")
a = input("e-Mail adress pls : ")
b = input("E-ma,l password please : ")
while True:
    Deneme(a,b)
    

