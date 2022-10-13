import smtplib
from email.message import EmailMessage
from datetime import datetime
import random
import os

# send a motivational qoute to yourself every monday

today = datetime.now()

if today.weekday() == 0:
    with open('quotes.txt') as f:
        quotes = f.readlines()
        quote = random.choice(quotes)    


    email = os.environ['GMAIL1']
    password = os.environ['GMAIL1_PASS']

    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = 'Monday Motivation'
    msg.set_content(quote)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
        conn.login(email, password)
        conn.send_message(msg)
    