#The email sending App using Python and Email SMTP


import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time
import os

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

# Create the body of the message (a plain-text and an HTML version).
text = """\
Hi!
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi!<br>
       How are you?<br>
       <a href="XXXXXXXXXXXXXXXXXXXXXXXXX">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Setup the MIME
message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html, 'html')])

# Convert it as a plain/html MIMEMultipart object
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    
