import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os.path


def snd():
    input_mail = input("your gmail>")
    input_pass = input("your password>")
    to_send_input = input("reciver>")
    sub_input = input("subject>")
    file_location_in = input("f location>")
    message_in = input("message>")

    email = input_mail
    password = input_pass
    snd_to_email = to_send_input
    subject = sub_input
    if file_location_in == "":
        pass
    else:
        file_location = file_location_in
    message = message_in

    msg = MIMEMultipart("alternative")
    msg["From"] = email
    msg["To"] = snd_to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        file_name = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; file_name= %s" % file_name)
        msg.attach(part)
    except:
        pass

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, snd_to_email, text)
    server.quit()