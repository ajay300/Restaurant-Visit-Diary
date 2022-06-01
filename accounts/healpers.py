from django.core.mail import send_mail
import uuid
from django.conf import settings



def send_forget_password(email):
    
    token = str(uuid.uuid4())
    subject = "Your Forget Password Link "
    message = f"HI , click on the link to reset Your password! http://127.0.0.1:8000/accounts/change-password/{token}/"
    email = settings.EMAIL_HOST_USER
    recipient_list = [email]
