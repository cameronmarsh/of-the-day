#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from createHtml import constructHtml

def main():
    fromaddr = 'oftheday2018@gmail.com'
    #read addresses from file
    toaddrs = []
    emails = open('mailingList.txt', 'r')
    for email in emails:
        toaddrs.append(email.rstrip())
    emails.close()

    #get today's date
    day = date.today().strftime('%A %b %d')

    #create the message
    msg = MIMEMultipart('alternative')
    msg['subject'] = "Of the Day " + day
    msg['To'] = ', '.join(toaddrs)
    msg['From'] = 'cmarsh10@gmail.com'

    #generate the day's html file
    for i in range(3):
        try:
            constructHtml()
            break
        except AttributeError:
            continue


    #generate the html as a string
    html = open('index.html', 'r')
    msgBodyStr = ''
    for line in html:
        msgBodyStr += line
    html.close()

    #add html string to the email message container
    msgBody = MIMEText(msgBodyStr, 'html')
    msg.attach(msgBody)

    #send the email
    server = smtplib.SMTP('smtp.gmail.com:587')
    credentials = open('credentials.txt', 'r')
    password = credentials.readline()
    credentials.close()

    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()


if __name__ == '__main__': main()
    
