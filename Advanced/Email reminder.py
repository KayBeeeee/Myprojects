"""
Automated Email Reminder Script
--------------------------------
This script sends email reminders for specific tasks based on a list of reminders stored in a text file.
It uses Gmail's SMTP service to send the emails.

Steps:
1. Read reminders from a file
2. Schedule the reminders to be sent at specific times
3. Send the email reminder

Requirements:
- smtplib (to send email)
- email (to construct email messages)
- schedule (for scheduling tasks)

"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime


# Email configuration
SENDER_EMAIL = "youremail@gmail.com"  # Replace with your email address
SENDER_PASSWORD = "yourpassword"      # Replace with your email password (or app password for Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email function to send reminders
def send_email(subject, body, to_email):
    """
    Sends an email with the provided subject and body to the specified recipient.
    """
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            text = msg.as_string()
            server.sendmail(SENDER_EMAIL, to_email, text)
            print(f"Reminder sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Read reminders from a file
def read_reminders():
    """
    Reads the reminders from a text file where each line contains a reminder in the format:
    "YYYY-MM-DD HH:MM - Task Description"
    """
    reminders = []
    with open("reminders.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                date_str, task = line.split(" - ")
                reminder_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                reminders.append((reminder_time, task))
    return reminders


# Function to check for due reminders and send emails
def check_reminders():
    """
    Checks if any reminder is due, and if so, sends an email.
    """
    current_time = datetime.now()
    reminders = read_reminders()

    for reminder_time, task in reminders:
        if current_time >= reminder_time and current_time < reminder_time + timedelta(minutes=5):
            send_email(f"Reminder: {task}", f"Don't forget: {task}", SENDER_EMAIL)


# Schedule reminders to check every minute
schedule.every(1).minute.do(check_reminders)

print("Automated Reminder Script is running...")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
