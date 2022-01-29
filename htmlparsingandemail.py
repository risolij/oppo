url = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=casenumber'
import requests
from bs4 import BeautifulSoup as soup
import smtplib

gmail_user = 'username@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to = ['abc@gmail.com','def@gmail.com']
subject = 'USCIS STATUS'

try:
    reply = requests.get(url)
    page = soup(reply.content,"html.parser")
    rows = page.find("div",{"class":"rows text-center"})
    if 'APPROVED' in  str(rows.h1.text).upper() :
        body = 'APPROVED\nStatus:' + str(rows.h1.text).upper()
        subject = 'Congratulations APPROVED'
    else:
        body = str(rows.h1.text).upper()
except:
    body = 'some error'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong….",ex)
