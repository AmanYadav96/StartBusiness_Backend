from celery import shared_task
from compare.models import Compare
from compare.serializers import CampareSerializer
from cart.models import Cart
from wishlist.models import Wishlist
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bs4 import BeautifulSoup
from pathlib import Path
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string





    


smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "sangeetatraders188@gmail.com"
smtp_password = "ctuvsymsarkuuumg"
from_email = "sangeetatraders188@gmail.com"
BASE_DIR = Path(__file__).resolve().parent.parent

@shared_task

@shared_task
def send_verification_email(otp,user_email):
    html_content = render_to_string('otp.html', {'otp': otp})

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Email"
    message["From"] = from_email
    message["To"] = user_email
    to_email = user_email
    # Attach HTML content
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)
    # body = "here is your one time password (otp)"+str(otp)
    # message.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()

