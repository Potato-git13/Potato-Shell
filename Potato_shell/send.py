# A module for sending emails for Potato shell


import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os.path


def sending(input_mail, input_password, to_send_input, subject_input, message_input, file_location_input):

    email = input_mail
    password = input_password
    snd_to_email = to_send_input
    subject = subject_input
    if file_location_input == "":
        pass
    else:
        file_location = file_location_input
    message = message_input

    msg = MIMEMultipart("alternative")
    msg["From"] = email
    msg["To"] = snd_to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        file_name = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
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
