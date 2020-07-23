import csv
from config import *
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep as delay
import numpy as np
import requests

people = []

with open('/' + dataFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if row[1] != 'INELLIG' and row[6] == 'Yes':
            person = {
                      'name':row[2] + ' ' + row[3],
                      'email':row[4]
                     }
            people.append(person)
        line_count += 1
    print(f'Processed {line_count} lines.')

for person in people:
    print(person)

for person in people:

    name = person['name']
    role = 'Attendee'
    res = requests.get(f'https://certhasher.herokuapp.com/generate?name={name}&role={role}&type={typ}')
    link = res.text
    print(link)

    messageText = f'''
Hello Hackers!

Thank you for attending Hack the Cloud! We hope you all enjoyed your time and had fun making things.

We ended up with 242 sign-ups and 46 project submissions. The work you all have done is amazing and the team appreciates the creative thinking you have brought to Hack the Cloud.  

For attending we have created an attendee certificate. If you won you will receive a separate email with more details and a different certificate. Here is your link: {link}
If this link creates a certificate with the wrong name or there are any problems feel free to email me and we can fix the issue.

Here are the winners of Hack the Cloud:

1st Place: FamJam by Judy Wu, Bonnie Chin, Kailey Chen and Grace Gao
2nd Place: Astr by Alex Wan
3rd Place: exARcise by Nathan Dimmer
Beginner Prize: Liveify by Alexis Fry and Henry Bloom

All projects can be found at this link: https://hack-the-cloud.devpost.com/submissions

If you are interested in learning more about Data Science check out Big Data at Berkeley: https://forms.gle/fEEDq2p3J8Xateuk7!

And if you're interested in general programming courses check out https://missionbit.org.

And if you're interested in publishing your project our partners have a publishing service: https://mindsparkintl.co/submit.html.

We hope you all stay safe.

Thanks,
Hack the Fog Team and MissionBit Student Advisory Board.
https://hackthefog.com
    '''

    messageHtml = f'''
<p>Hello Hackers!</p>

<p>Thank you for attending Hack the Cloud! We hope you all enjoyed your time and had fun making things.</p>

<p>We ended up with 242 sign-ups and 46 project submissions. The work you all have done is amazing and the team appreciates the creative thinking you have brought to Hack the Cloud.</p>

<p>For attending we have created an attendee certificate. If you won you will receive a separate email with more details and a different certificate. Here is your link: <a href="{link}" target="_blank" rel="noopener">{link}</a><br>
If this link creates a certificate with the wrong name or there are any problems feel free to email me and we can fix the issue.</p>

Here are the winners of Hack the Cloud:</p>

<p>1st Place: FamJam by Judy Wu, Bonnie Chin, Kailey Chen and Grace Gao<br>
2nd Place: Astr by Alex Wan<br>
3rd Place: exARcise by Nathan Dimmer<br>
Beginner Prize: Liveify by Alexis Fry and Henry Bloom</p>

<p>All projects can be found at this link: <a href="https://hack-the-cloud.devpost.com/submissions" target="_blank" rel="noopener">https://hack-the-cloud.devpost.com/submissions</a>.</p>

<p>If you are interested in learning more about Data Science check out Big Data at Berkeley: <a href="https://forms.gle/fEEDq2p3J8Xateuk7" target="_blank" rel="noopener">https://forms.gle/fEEDq2p3J8Xateuk7</a>!</p>

<p>And if you're interested in general programming courses check out <a href="https://missionbig.org" target="_blank" rel="noopener">https://missionbit.org</a>.</p>

<p>And if you're interested in publishing your project our partners have a publishing service: <a rel="noopener" target="_blank" href="https://mindsparkintl.co/submit.html">https://mindsparkintl.co/submit.html</a>.</p>

<p>We hope you all stay safe.</p>

<p>Thanks,<br>
Hack the Fog Team and MissionBit Student Advisory Board.<br>
<a href="https://hackthefog.com" target="_blank" rel="noopener">https://hackthefog.com</a></p>
    '''

    msg = MIMEMultipart('alternative')
    msg['From'] = f'Hack the Cloud <{senderEmail}>'
    msg['To'] = person['email']
    msg['Subject'] = 'Thank you for attending Hack the Cloud!'
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
    