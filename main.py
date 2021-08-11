import smtplib, ssl
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


port = 465
sender_email = input("Enter sender email")
sender_password = getpass.getpass(prompt = "Enter password")
receiver_email = input("Enter receiver email")

message = MIMEMultipart("alternative")
message["Subject"] = "EmailAutomation project"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Hi,
This is my emailautomation project."""

html = """\
<html>
    <body style="background-color:red;">
        <p>Hi,<br>
        This is my <a href="http://www.myproject.com">emailautomation</a> project.
        </p>
    </body>
</html>"""

text_message = MIMEText(text, "text")
html_message = MIMEText(html, "html")

message.attach(text_message)
message.attach(html_message)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
