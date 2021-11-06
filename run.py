import csv
#from config import *
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep as delay
import requests

senderEmail = "raf@hackthefog.com"
appPassword = "cemcfscsrmrosqjb"

people = []

with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        person = {
                  'name':row[0] + ' ' + row[1],
                  'email':row[3],
                  'link':row[4]
                 }
        people.append(person)
        line_count += 1
    print(f'Processed {line_count} lines.')

#for person in people:
#    print(person)

for person in people:
    link = person['link']
    name = person['name']

    messageText = f'''
Hello {name}!

Thank you for attending Hack the Cloud 2.0! We hope you enjoyed your time at our event.

We ended up with 281 sign-ups and 52 project submissions. The work you have done is amazing and the team appreciates the creative thinking you have brought to Hack the Cloud 2.0.  

For attending we have created an attendee certificate. If you won your certificate will include your placement. Here is your link: {link}
If this link creates a certificate with the wrong name or there are any problems feel free to email me and we can fix the issue.

All projects can be found at this link: https://htc2.devpost.com/project-gallery

And if you're interested in general programming courses and your in the San Francisco Bay Area check out our partner https://missionbit.org.

We hope you all stay safe during the pandemic and continue your great work in CS.

Thanks,
Hack the Cloud Team
https://hackthefog.com
    '''

    messageHtml = f'''
<p>Hello {name}</p>

<p>Thank you for attending Hack the Cloud 2.0! We hope you enjoyed your time at our event.</p>

<p>We ended up with 281 sign-ups and 52 project submissions. The work you have done is amazing and the team appreciates the creative thinking you have brought to Hack the Cloud 2.0.</p>

<p>For attending we have created an attendee certificate. If you won your certificate will include your placement. Here is your link: <a href="{link}" target="_blank" rel="noopener">{link}</a><br>
If this link creates a certificate with the wrong name or there are any problems feel free to email me and we can fix the issue.</p>

<p>All projects can be found at this link: <a href="https://htc2.devpost.com/project-gallery" target="_blank" rel="noopener">https://htc2.devpost.com/project-gallery</a>.</p>

<p>If you're interested in general programming courses and your in the San Francisco Bay Area check out our partner <a href="https://missionbig.org" target="_blank" rel="noopener">https://missionbit.org</a>.</p>

<p>We hope you all stay safe during the pandemic and continue your great work in CS.</p>

<p>Thanks,<br>
Hack the Cloud Team<br>
<a href="https://hackthefog.com" target="_blank" rel="noopener">https://hackthefog.com</a></p>
    '''

    msg = MIMEMultipart('alternative')
    msg['From'] = f'Hack the Cloud <{senderEmail}>'
    msg['To'] = person['email']
    msg['Subject'] = 'Thank you for attending Hack the Cloud 2.0!'
    part1 = MIMEText(messageText, 'plain')
    part2 = MIMEText(messageHtml, 'html')
    msg.attach(part1)
    msg.attach(part2)
    message = msg.as_string()
    
    recipient = person['email']

    try:
        smtp_server = SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo_or_helo_if_needed()
        smtp_server.starttls()
        smtp_server.ehlo_or_helo_if_needed()
        smtp_server.login(senderEmail, appPassword)
        smtp_server.sendmail(senderEmail, recipient, message)
        smtp_server.quit()
        print(f'Email sent to {recipient}')
    except Exception as e:
        smtp_server.quit()
        print(f'Email couldn\'t be sent to {recipient}')

    delay(5)
    