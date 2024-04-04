import smtplib
from email.mime.text import MIMEText
import os
import dotenv

# chat logic flow
# 1. if the assistant's response includes a prompt to book an appointment, wait for user's response
# 2. if the user agress, prompt them for a date, time, and email address
# 3. confirm appointment details with user and send an email
def send_appointment_email(email_address, date, time):
    subject = "Appointment Confirmation"
    body = f"Your appointment is scheduled for {date} at {time}"
    sender = "jaydenpiao@gmail.com"
    recipient = email_address
    dotenv.load_dotenv()
    password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")