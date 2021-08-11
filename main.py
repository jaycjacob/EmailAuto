import smtplib, ssl
from getpass import getpass

message = """\
Subject : Hi,

my name is jacob."""

port = 465
sender_email = input("Enter sender email")
sender_password = input('Enter your password')
receiver_email = input("Enter receiver email")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
