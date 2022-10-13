import smtplib
from email.message import EmailMessage
from datetime import datetime
import random
import pandas as pd
import os

# read data of birthdays and get today's date
df = pd.read_csv('birthdays.csv')
today = datetime.now().date()


# loop through each row in df
for index, row in df.iterrows():
    # get receiver's name, email and birth_date
    receiver_name = row['name']
    receiver_email = row['email']
    birth_date = datetime(row['year'], row['month'], row['day']).date()
    
    # if today is their birth day
    if today.day == birth_date.day and today.month == birth_date.month:
        
        # step 1: get a random email template
        letter_templates = os.listdir('letter_templates/')
        template = random.choice(letter_templates)
        with open(f'letter_templates/{template}') as f:
            letter_contents = f.read()
            letter_contents = letter_contents.replace('[NAME]', receiver_name)
            
         
        # step 2: send him/her an email
        email = os.environ['GMAIL1']
        password = os.environ['GMAIL1_PASS']

        msg = EmailMessage()
        msg['Subject'] = f'Happy Birthday {receiver_name}!'
        msg['From'] = email
        msg['To'] = receiver_email
        msg.set_content(letter_contents)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
            print(f"Today is {receiver_name}'s birthday, their email is {receiver_email}")
            print(f'sent mail: {letter_contents}')
            conn.login(email, password)
            conn.send_message(msg)
            
          