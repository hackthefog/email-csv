import csv
from config import dataFile, appPassword, senderEmail
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

emails = []
with open('/' + dataFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    '''
    for row in csv_reader:
        if line_count != 0:
            emails.append(row[3])
        line_count += 1
    '''
    for row in csv_reader:
        if line_count != 0 and row[0] == 'FALSE':
            emails.append(row[3])
        line_count += 1
    print(f'Processed {line_count} lines.')

for email in emails:
    print(email)

emailMessage = ('''
Hello Hackers,

As you all may already know, Hack the Fog 2.0 was canceled due to the pandemic. We will be postponing Hack the Fog 2.0 but in the meantime, we are planning to host an online hackathon, and we welcome you all to join Hack the Cloud!

If you're interested in joining us for another hackathon, we are planning to host Hack the Cloud between 9:00 AM PST on July 11th to 12:00 AM PST (midnight) on July 12th.

The top prize is AirPods for the winning team members but there will also be workshops from tech experts through Zoom or live streams. Sign up through our Devpost (https://hack-the-cloud.devpost.com/) and visit our website (https://cloud.hackthefog.com) or contact us (contact@hackthefog.com) if you have any questions!

We hope to see you there
The Hack the Cloud Team''')

emailMessageHtml = ('''
<p>Hello Hackers,</p>

<p>As you all may already know, Hack the Fog 2.0 was canceled due to the pandemic. We will be postponing Hack the Fog 2.0 but in the meantime, we are planning to host an online hackathon, and we welcome you all to join Hack the Cloud!</p>

<p>If you're interested in joining us for (another/an online) hackathon, we are planning to host Hack the Cloud between 9:00 AM PST on July 11th to 12:00 AM PST (midnight) on July 12th.</p>

<p>The top prize is AirPods for the winning team members but there will also be workshops from tech experts through Zoom or live streams. Sign up through our Devpost (<a href="https://hack-the-cloud.devpost.com/">https://hack-the-cloud.devpost.com/</a>) and visit our website (<a href="https://cloud.hackthefog.com">https://cloud.hackthefog.com</a>) or contact us (<a href="mailto:contact@hackthefog.com">contact@hackthefog.com</a>) if you have any questions!</p>

<p>We hope to see you there</p>
<p>The Hack the Cloud Team</p>''')

emailMessage1 = ('''
Hello Hackers,

You haven't filled out our form yet and you need it if you want to join our workshops it takes a couple minutes to fill out and send!

We have a media release form that we need you to fill out: https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing

Here are steps for filling this form out:

1. Download the pdf from our link above
2. Rename it to your fullname. Example (JohnDoe.pdf)
3. Open it and type in your responses and get your parent to review (If you are under 18) in the fields. The form is writable so you should be able to edit it just by opening it.
4. Last, save your changes and email it to raf@hackthefog.com with the subject "Attendee Form"

Thank you!
The Hack the Cloud Team''')

emailMessageHtml1 = ('''
<p>Hello Hackers,</p>

<p>You haven't filled out our form yet and you need it if you want to join our workshops it takes a couple minutes to fill out and send!</p>

<p>We have a media release form that we need you to fill out: <a href="https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing">https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing</a></p>

<ol>
  <li>Download the pdf from our link above</li>
  <li>Rename it to your fullname. Example (JohnDoe.pdf)</li>
  <li>Open it and type in your responses and get your parent to review (If you are under 18) in the fields. The form is writable so you should be able to edit it just by opening it.</li>
  <li>Last, save your changes and email it to raf@hackthefog.com with the subject "Attendee Form"</li>
</ol>

<p>Thank you</p>
<p>The Hack the Cloud Team</p>''')


for recieverEmail in emails:

    msg = MIMEMultipart('alternative')
    msg['From'] = f'Hack the Cloud <{senderEmail}>'
    msg['To'] = recieverEmail
    msg['Subject'] = f'Hack the Cloud - Form'
    part1 = MIMEText(emailMessage1, 'plain')
    part2 = MIMEText(emailMessageHtml1, 'html')
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