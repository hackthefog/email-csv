import csv
from config import dataFile, appPassword, senderEmail
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

emails = []
with open('/' + dataFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            emails.append(row[3])
        line_count += 1
    print(f'Processed {line_count} lines.')

emailMessage = ('''
Hello Hackers,

As you all may already know, Hack the Fog 2.0 was canceled due to the pandemic. We will be postponing Hack the Fog 2.0 but in the meantime, we are planning to host an online hackathon, and we welcome you all to join Hack the Cloud!

If you're interested in joining us for another hackathon, we are planning to host Hack the Cloud between 9:00 AM PST on June 11th to 12:00 AM PST (midnight) on June 12th.

The top prize is AirPods for the winning team members but there will also be workshops from tech experts through Zoom or live streams. Sign up through our Devpost(https://hack-the-cloud.devpost.com/) and visit our website(https://cloud.hackthefog.com) or contact us if you have any questions!

We hope to see you there
The Hack the Cloud Team''')

emailMessageHtml = ('''
<p>Hello Hackers,</p>

<p>As you all may already know, Hack the Fog 2.0 was canceled due to the pandemic. We will be postponing Hack the Fog 2.0 but in the meantime, we are planning to host an online hackathon, and we welcome you all to join Hack the Cloud!</p>

<p>If you're interested in joining us for (another/an online) hackathon, we are planning to host Hack the Cloud between 9:00 AM PST on June 11th to 12:00 AM PST (midnight) on June 12th.</p>

<p>The top prize is AirPods for the winning team members but there will also be workshops from tech experts through Zoom or live streams. Sign up through our <a href="https://hack-the-cloud.devpost.com/">Devpost</a> and visit our <a href="https://cloud.hackthefog.com">website</a> or <a href="mailto:contact@hackthefog.com">contact us</a> if you have any questions!</p>

<p>We hope to see you there</p>
<p>The Hack the Cloud Team</p>''')

for recieverEmail in emails:

    msg = MIMEMultipart('alternative')
    msg['From'] = f'Hack the Cloud <{senderEmail}>'
    msg['To'] = recieverEmail
    msg['Subject'] = f'Hack the Cloud'
    part1 = MIMEText(emailMessage, 'plain')
    part2 = MIMEText(emailMessageHtml, 'html')
    msg.attach(part1)
    msg.attach(part2)
    message = msg.as_string()

    smtp_server = SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo_or_helo_if_needed()
    smtp_server.starttls()
    smtp_server.ehlo_or_helo_if_needed()
    smtp_server.login(senderEmail, appPassword)
    smtp_server.sendmail(senderEmail, recieverEmail, message)
    smtp_server.quit()

    print(f'Email sent to {recieverEmail}')