---
title: Texting from a Computer in Python
thumbnail: sms-message.jpg
layout: post
permalink: /texting-from-your-server-in-python/
---

Here's a script to send a text message in Python. It uses the standard library and
is very straightforward. It utilizes the fact that most major carriers allow texting
via email (ie. by [SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)),
so nothing more is needed than an email account and a desired target.

In my work, I use it to tell me when my computational simulations are done running.
Also, it can send to any phone number and can be put in an infinite loop; days of
fun, right there.

```python
import smtplib
from email.mime.text import MIMEText

# Message to be sent
message = MIMEText("Hello, texting!")

# Sending email username/password and receiving phone number
email_username = ""
email_password = ""
phone_number = ""

# Gmail to Verizon. Change here for different combinations.
email_username += "@gmail.com"
phone_number += "@vtext.com"

# Format message to look like an email
message["From"] = email_username
message["To"] = phone_number
message["Subject"] = "From your server!"

# Connect and send
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(email_username, email_password)
s.sendmail(email_username, phone_number, message.as_string())
s.quit()
```
