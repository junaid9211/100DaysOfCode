# Sending emails in python

## imports
```python
import os
import smtplib
from email.message import EmailMessage
```

## get login details
```python
email = os.environ['GMAIL1']
password = os.environ['GMAIL1_PASS']
```

## create email message
```python
msg = EmailMessage()
msg['Subject'] = 'Sent from pythonanywhere'
msg['From'] = os.environ['GMAIL1']
msg['To'] = os.environ['GMAIL2']
msg.set_content('This is the body of email')
```

## finally send email
```python
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
    conn.login(email, password)
    conn.send_message(msg)
```

## adding attachments to EmailMessage object
```python
import imghdr
# step 1: get the image data
image = 'img1.jpg'
with open(image, mode='rb') as f:
    image_contents = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    
# step 2 attach the image
msg.add_attachment(image_contents, maintype='image', subtype=file_type, filename=file_name)
```

## adding multiple images
```python
# you can easily attach multiple images using a for loop
import imghdr

images = ['img1.jpg', 'img2.jpg']
for image in images:
    # step 1: get the image data
    with open(image, mode='rb') as f:
        image_contents = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        
    # step 2 attach the image
    msg.add_attachment(image_contents, maintype='image', subtype=file_type, filename=file_name)
```


## Sending email to multiple people
```python
# just set the msg['To'] to a list of emails
contacts = ['a@gmail.com', 'b@gmail.com']
msg['To'] = contacts
# alternatively you can also provide a comma separated string of emails
msg['To'] = ', '.join(contacts)
```



## lastly sending email without using EmailMessage class
```python
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email, password)
    
    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6pm this saturday'
    
    msg = f'Subject: {subject}\n\n{body}'
    
    conn.sendmail(from_addr=email, to_addrs=receiver_email, msg=msg)
```