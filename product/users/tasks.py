from celery import shared_task 
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime

@shared_task 
def send_otp_email(email, code):
    send_mail(
        subject="Registration code", 
        message=f'yuor code {code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )

    
@shared_task 
def send_report_email():
    send_mail(
        subject="Report daily", 
        message='..............',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["aminakirkeeva777@gmail.com"]
    )
    
@shared_task
def write_log(message):
    file = open("log.txt", "a", encoding="utf-8")
    file.write(message + "\n")
    file.close()
    return "Saved: " + message

@shared_task
def save_time():
    now = datetime.now()
    file = open("time.txt", "a", encoding="utf-8")
    file.write("Время: " + str(now) + "\n")
    file.close()
    
@shared_task
def send_welcome_email(email, username):
    send_mail(
        subject="Welcomee!",
        message="Hello, " + username + "! Hell nahhh.",
        from_email=None,
        recipient_list=[email],
    )
    return "Email sent to " + email