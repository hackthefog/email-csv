import csv
from config import dataFile, appPassword, senderEmail
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep as delay


emails = []

with open('/' + dataFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        #if line_count != 0 and row[0] == 'FALSE':
        if True:
            emails.append(row[4])
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

You haven't filled out our form yet and you need it if you want to join our workshops it takes a couple minutes to fill out and send! If you don't plan on signing the form or want to stop recieving these emails just respond and let us know!

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

<p>You haven't filled out our form yet and you need it if you want to join our workshops it takes a couple minutes to fill out and send! If you don't plan on signing the form or want to stop recieving these emails just respond and let us know!</p>

<p>We have a media release form that we need you to fill out: <a href="https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing">https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing</a></p>

<ol>
  <li>Download the pdf from our link above</li>
  <li>Rename it to your fullname. Example (JohnDoe.pdf)</li>
  <li>Open it and type in your responses and get your parent to review (If you are under 18) in the fields. The form is writable so you should be able to edit it just by opening it.</li>
  <li>Last, save your changes and email it to raf@hackthefog.com with the subject "Attendee Form"</li>
</ol>

<p>Thank you</p>
<p>The Hack the Cloud Team</p>''')

emailMessage2 = ('''
Hello Hack the Cloud Hackers,

We hope that all is well during these tough times!

As a reminder, the hackathon is being held on July 11th - 12th! We have attached an Attendee Packet (https://docs.google.com/document/u/3/d/e/2PACX-1vRQ5xsmrCuB6OdhmiLr1zN5EEn7LPAq40hP51hwkNJMdvJtjKPS1r8HplFizQaa0vKzUYc_ulY0AFQI/pub) so that you all will be prepared for the exciting day. We have amazing workshops planned for both Saturday and Sunday and we hope that you all will enjoy them. We have also been provided with lots of interesting tech resources from major tech companies that we hope you might find useful.

If you haven’t already signed the waiver form (https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing), please do so before the event.

Those of you who do not fill out a waiver will not be able to participate in the workshops on Zoom but are still able to participate in the hackathon after sending a picture of their current student ID to any of us for grade confirmation.

Please complete this form (https://forms.gle/roB1jquATfrg37hM7) before the event as well, this is also where you can submit your waiver forms or student IDs.

The event will be held on Zoom so be sure to have a Zoom account ready to sign on in. The Zoom call will be open on July 11th 9:00 AM Pacific Daylight Time. All Zoom meeting links will be available in the Attendee Packet.

We also highly recommend having a Discord account and joining our Discord server https://discord.com/invite/evJ8fnG, especially if you don’t have a team. Important announcements and resources will be posted on the Discord server. There will also be a team matchmaking session near the beginning of the event.

We want to clarify that only incoming freshmen, highschoolers, or graduating seniors will be eligible for prizes. For special cases, such as middle school students, please shoot us an email.

If you have any questions feel free to email us at contact@hackthefog.com or ping us on Discord!

We can’t wait to see what you make!

Happy 4th of July,
The Hack the Cloud Team
https://cloud.hackthefog.com''')

emailMessageHtml2 = ('''
<!DOCTYPE html>
<html lang="en">
<head></head>
<body>
<p>Hello Hack the Cloud Hackers,</p>

<p>We hope that all is well during these tough times!</p>

<p>As a reminder, the hackathon is being held on <strong>July 11th - 12th!</strong> We have attached an <a target="_blank" href="https://docs.google.com/document/u/3/d/e/2PACX-1vRQ5xsmrCuB6OdhmiLr1zN5EEn7LPAq40hP51hwkNJMdvJtjKPS1r8HplFizQaa0vKzUYc_ulY0AFQI/pub">Attendee Packet</a> so that you all will be prepared for the exciting day. We have <strong>amazing workshops</strong> planned for both <strong>Saturday and Sunday</strong> and we hope that you all will enjoy them. We have also been provided with lots of interesting tech resources from major tech companies that we hope you might find useful.</p>

<p>If you haven’t already signed the <a target="_blank" href="https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing">waiver form</a>, please do so before the event.</p>

<p>Those of you who <strong>do not fill out a waiver</strong> will <strong>not</strong> be able to participate in the workshops on Zoom but are still able to participate in the hackathon after sending a <strong>picture of their current student ID</strong> to any of us for grade confirmation.</p>

<p>Please complete <a target="_blank" href="https://forms.gle/roB1jquATfrg37hM7">this form</a> before the event as well, this is also where you can <strong>submit your waiver forms or student IDs</strong>.</p>

<p>The event will be held on <strong>Zoom</strong> so be sure to have a <strong>Zoom account</strong> ready to sign on in. The Zoom call will be open on <strong>July 11th 9:00 AM Pacific Daylight Time.</strong> <strong>All Zoom meeting links</strong> will be available in the <strong>Attendee Packet</strong>.</p>

<p>We also highly recommend having a <strong>Discord account</strong> and joining our <strong>Discord server</strong> <a target="_blank" href="https://discord.com/invite/evJ8fnG">here</a>, <i>especially if you don’t have a team</i>. <strong>Important announcements and resources</strong> will be posted on the Discord server. There will also be a <strong>team matchmaking session</strong> near the beginning of the event.</p>

<p>We want to clarify that only incoming freshmen, highschoolers, or graduating seniors will be eligible for prizes. For special cases, such as middle school students, please shoot us an email.</p>

<p>If you have any questions feel free to email us at <a target="_blank" href="mailto:contact@hackthefog.com">contact@hackthefog.com</a> or ping us on Discord!</p>

<p>We can’t wait to see what you make!</p>

<p>Happy 4th of July,</p>
<p>The Hack the Cloud Team</p>
<p><a href="https://cloud.hackthefog.com" target="_blank">https://cloud.hackthefog.com</a></p>
</body></html>''')

preEventMessage = ('''
Hello Hackers,

Hack the Cloud is tomorrow!

Just as a reminder the opening ceremony will begin at 9:00 AM Pacific Daylight Time.

If you haven’t already, please fill out the waiver form that we emailed you and check out the attendee packet that we sent with all of the important information about the hackathon. 

Heres our event waiver:
https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing

Please submit that form or your ID to this form:
https://forms.gle/roB1jquATfrg37hM7

Here’s the link to the Attendee Packet:
https://docs.google.com/document/u/1/d/e/2PACX-1vRQ5xsmrCuB6OdhmiLr1zN5EEn7LPAq40hP51hwkNJMdvJtjKPS1r8HplFizQaa0vKzUYc_ulY0AFQI/pub

Last, here is our day of Discord:
https://discord.gg/evJ8fnG

Thanks, 
Hack the Cloud Team
https://cloud.hackthefog.com''')

preEventMessageHTML = ('''
<p>Hello Hackers,</p>

<p>Hack the Cloud is tomorrow!</p>

<p>Just as a reminder the opening ceremony will begin at <strong>9:00 AM Pacific Daylight Time</strong>.</p>

<p>If you haven’t already, <strong>please fill out the waiver form</strong> that we emailed you and check out the attendee packet that we sent with all of the important information about the hackathon.</p>

<p>Heres our <a href="https://drive.google.com/file/d/1KPIQuqX1b1mk7XqMSPq6DsLixDBvn77f/view?usp=sharing" target="_blank">event waiver</a>.</p>

<p>Please submit that waiver or your ID to this <a href="https://forms.gle/roB1jquATfrg37hM7" target="_blank">form</a>.</p>

<p>Here’s the link to the <a href="https://docs.google.com/document/u/1/d/e/2PACX-1vRQ5xsmrCuB6OdhmiLr1zN5EEn7LPAq40hP51hwkNJMdvJtjKPS1r8HplFizQaa0vKzUYc_ulY0AFQI/pub">Attendee Packets</a>.</p>

<p>Last, here is our day of <a href="https://discord.gg/evJ8fnG" target="_blank">Discord</a>.</p>

<p>Thanks,<br>Hack the Cloud Team</p>
<p><a href="https://cloud.hackthefog.com" target="_blank">https://cloud.hackthefog.com</a></p>''')


for recieverEmail in emails:

    msg = MIMEMultipart('alternative')
    msg['From'] = f'Hack the Cloud <{senderEmail}>'
    msg['To'] = recieverEmail
    msg['Subject'] = 'Hack the Cloud is Tomorrow!'
    part1 = MIMEText(preEventMessage, 'plain')
    part2 = MIMEText(preEventMessageHTML, 'html')
    msg.attach(part1)
    msg.attach(part2)
    message = msg.as_string()
    
    try:
        smtp_server = SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo_or_helo_if_needed()
        smtp_server.starttls()
        smtp_server.ehlo_or_helo_if_needed()
        smtp_server.login(senderEmail, appPassword)
        smtp_server.sendmail(senderEmail, recieverEmail, message)
        smtp_server.quit()
        print(f'Email sent to {recieverEmail}')
    except Exception as e:
        smtp_server.quit()
        print(f'Email couldn\'t be sent to {recieverEmail}')

    delay(5)

    