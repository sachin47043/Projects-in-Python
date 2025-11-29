import smtplib 
import ssl 
from email.message import EmailMessage
EMAIL = "ghoshdebojit418@gmail.com"
APP_PASSWORD = "ctzf ufbs omcv hemm"
RECEIVER = "debojitg566@gmail.com"

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello for PYTHON.."
msg.set_content("This email was shared by python email..")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as server :
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)